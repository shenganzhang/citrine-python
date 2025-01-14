import pytest

from tests.utils.factories import GemTableDataFactory

from citrine.resources.gemtables import GemTableCollection, GemTable
from citrine.resources.project import Project
from citrine.informatics.objectives import ScalarMaxObjective, ScalarMinObjective

from citrine.builders.scores import create_default_score


@pytest.fixture
def table_data() -> str:
    """Fake table data with mean/std columns, units, and non-numerical data types."""
    header = "x~Mean (lbs),y~Mean (lbs),z~Mean (lbs),z~Std (lbs), pets~Mean\n"
    row1 = "1.0,0.0,10.0,1.0,dog\n"
    row2 = "0.0,1.0,5.0,0.5,cat"
    return header + row1 + row2


@pytest.fixture
def table():
    url = "http://otherhost:4572/anywhere"
    return GemTable.build(
        GemTableDataFactory(signed_download_url=url, version=2)
    )


@pytest.fixture
def project(table_data):
    """Fake project for table collection"""
    class FakeGemTableCollection(GemTableCollection):
        def __init__(self):
            pass

        def read_to_memory(self, table: GemTable) -> str:
            return table_data

    class FakeProject(Project):
        def __init__(self):
            pass

        @property
        def tables(self) -> FakeGemTableCollection:
            return FakeGemTableCollection()

    return FakeProject()


def test_create_default_score(project, table):
    """Test reading a table to create a default score for some objectives."""
    o1 = ScalarMinObjective(descriptor_key="x")     # Valid numerical with mean
    o2 = ScalarMaxObjective(descriptor_key="y")     # Valid numerical with mean
    o3 = ScalarMaxObjective(descriptor_key="z")     # Has both a Mean and Std column
    o4 = ScalarMaxObjective(descriptor_key="pets")  # Non-numeric
    o5 = ScalarMaxObjective(descriptor_key="bad")   # Not found in the table

    s1 = create_default_score(objectives=o1, project=project, table=table)
    assert s1.baselines[0] == 0.0

    s2 = create_default_score(objectives=o2, project=project, table=table)
    assert s2.baselines[0] == 1.0

    s3 = create_default_score(objectives=[o1, o2], project=project, table=table)
    assert s3.baselines[0] == 0.0
    assert s3.baselines[1] == 1.0

    s4 = create_default_score(objectives=[o3], project=project, table=table)
    assert s4.baselines[0] == 10.0  # Make sure we get the mean column, not std column

    # Check errors for poor descriptor choices
    with pytest.raises(ValueError):
        # Cannot convert data to numeric
        create_default_score(objectives=o4, project=project, table=table)

    with pytest.raises(ValueError):
        # Not found in header
        create_default_score(objectives=o5, project=project, table=table)
