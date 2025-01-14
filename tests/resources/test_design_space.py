from copy import deepcopy
import uuid
from random import random

import pytest

from citrine.informatics.descriptors import RealDescriptor
from citrine.informatics.design_spaces import EnumeratedDesignSpace, DesignSpace, ProductDesignSpace
from citrine.resources.design_space import DesignSpaceCollection
from tests.utils.session import FakeSession


@pytest.fixture
def valid_product_design_space(valid_product_design_space_data) -> ProductDesignSpace:
    data = deepcopy(valid_product_design_space_data)
    return DesignSpace.build(data)


def test_design_space_build():
    # Given
    collection = DesignSpaceCollection(uuid.uuid4(), None)
    design_space_id = uuid.uuid4()

    # TODO:  At some point we should create data factories for this
    design_space_data = {
        'id': str(design_space_id),
        'config': {
            'type': 'Univariate',
            'name': 'My Design Space',
            'description': 'For testing',
            'dimensions': [{
                'type': 'ContinuousDimension',
                'descriptor': {
                    'type': 'RealDescriptor',
                    'descriptor_key': 'foo',
                    'lower_bound': 0.0,
                    'upper_bound': 1.0,
                    'units': ""
                },
                'lower_bound': 0.0,
                'upper_bound': 1.0,
            }],
        },
        'status': '',
    }

    # When
    design_space = collection.build(design_space_data)

    # Then
    assert design_space.uid == design_space_id
    assert design_space.name == 'My Design Space'
    assert design_space.dimensions[0].descriptor.key == 'foo'


def test_formulation_build(valid_formulation_design_space_data):
    pc = DesignSpaceCollection(uuid.uuid4(), None)
    design_space = pc.build(valid_formulation_design_space_data)
    assert design_space.archived
    assert design_space.name == 'formulation design space'
    assert design_space.description == 'formulates some things'
    assert design_space.formulation_descriptor.key == 'formulation'
    assert design_space.ingredients == {'foo'}
    assert design_space.labels == {'bar': {'foo'}}
    assert len(design_space.constraints) == 1
    assert design_space.resolution == 0.1


def test_design_space_limits():
    """Test that the validation logic is triggered before post/put-ing enumerated design spaces."""
    # Given
    session = FakeSession()
    collection = DesignSpaceCollection(uuid.uuid4(), session)

    too_big = EnumeratedDesignSpace(
        "foo",
        description="bar",
        descriptors=[RealDescriptor("R-{}".format(i), lower_bound=0, upper_bound=1, units="") for i in range(128)],
        data=[{"R-{}".format(i): random() for i in range(128)} for _ in range(2001)]
    )

    just_right = EnumeratedDesignSpace(
        "foo",
        description="bar",
        descriptors=[RealDescriptor("R-{}".format(i), lower_bound=0, upper_bound=1, units="") for i in range(128)],
        data=[{"R-{}".format(i): random() for i in range(128)} for _ in range(2000)]
    )

    # create mock post response by setting the status
    mock_response = just_right.dump()
    mock_response["status"] = "READY"
    session.responses.append(mock_response)

    # Then
    with pytest.raises(ValueError) as excinfo:
        collection.register(too_big)
    assert "only supports" in str(excinfo.value)

    # test register
    collection.register(just_right)

    # add back the response for the next test
    session.responses.append(mock_response)

    # test update
    collection.update(just_right)


def test_create_default(valid_product_design_space_data,
                        valid_product_design_space):
    # The instance field isn't renamed to config in objects returned from this route
    # This renames the config key to instance to match the data we get from the API
    data_with_instance = deepcopy(valid_product_design_space_data)
    data_with_instance['instance'] = data_with_instance.pop('config')

    session = FakeSession()
    session.set_response(data_with_instance)
    collection = DesignSpaceCollection(
        project_id=uuid.uuid4(),
        session=session
    )
    default_design_space = collection.create_default(predictor_id=uuid.uuid4())
    assert default_design_space.dump() == valid_product_design_space.dump()
