from typing import List, Optional

from citrine._rest.resource import Resource, ResourceTypeEnum
from citrine._serialization import properties as _properties
from citrine.informatics.data_sources import DataSource
from citrine.informatics.descriptors import FormulationDescriptor
from citrine.informatics.predictors import Predictor
from citrine._rest.ai_resource_metadata import AIResourceMetadata

__all__ = ['SimpleMixturePredictor']


class SimpleMixturePredictor(Resource['SimpleMixturePredictor'], Predictor, AIResourceMetadata):
    """A predictor interface that flattens a formulation into a simple mixture.

    Parameters
    ----------
    name: str
        name of the configuration
    description: str
        description of the predictor
    input_descriptor: FormulationDescriptor
        input descriptor for the hierarchical (un-mixed) formulation
    output_descriptor: FormulationDescriptor
        output descriptor for the flat (mixed) formulation
    training_data: Optional[List[DataSource]]
        Sources of training data. Each can be either a CSV or an GEM Table. Candidates from
        multiple data sources will be combined into a flattened list and de-duplicated by uid and
        identifiers. De-duplication is performed if a uid or identifier is shared between two or
        more rows. The content of a de-duplicated row will contain the union of data across all
        rows that share the same uid or at least 1 identifier. Training data is unnecessary if the
        predictor is part of a graph that includes all training data required by this predictor.

    """

    _resource_type = ResourceTypeEnum.MODULE

    input_descriptor = _properties.Object(FormulationDescriptor, 'config.input')
    output_descriptor = _properties.Object(FormulationDescriptor, 'config.output')
    training_data = _properties.List(_properties.Object(DataSource),
                                     'config.training_data', default=[])

    typ = _properties.String('config.type', default='SimpleMixture',
                             deserializable=False)
    module_type = _properties.String('module_type', default='PREDICTOR')

    def __init__(self,
                 name: str,
                 *,
                 description: str,
                 input_descriptor: FormulationDescriptor,
                 output_descriptor: FormulationDescriptor,
                 training_data: Optional[List[DataSource]] = None):
        self.name: str = name
        self.description: str = description
        self.input_descriptor: FormulationDescriptor = input_descriptor
        self.output_descriptor: FormulationDescriptor = output_descriptor
        self.training_data: List[DataSource] = training_data or []

    def _post_dump(self, data: dict) -> dict:
        data['display_name'] = data['config']['name']
        return data

    def __str__(self):
        return '<SimpleMixturePredictor {!r}>'.format(self.name)
