from typing import List, Optional, Type, Union
from uuid import UUID
from warnings import warn

from citrine._serialization import properties
from citrine._session import Session
from citrine.informatics.data_sources import DataSource
from citrine.informatics.modules import Module
from citrine.resources.report import ReportResource


__all__ = ['Predictor']


class Predictor(Module):
    """Module that describes the ability to compute/predict properties of materials.

    Abstract type that returns the proper type given a serialized dict. subtype
    based on the 'type' value of the passed in dict.

    """

    _response_key = None
    _project_id: Optional[UUID] = None
    _session: Optional[Session] = None
    uid = properties.Optional(properties.UUID, 'id', serializable=False)
    """UUID of the predictor, if it has been retrieved from the platform."""

    name = properties.String('config.name')
    description = properties.Optional(properties.String(), 'config.description')

    @property
    def report(self):
        """Fetch the predictor report."""
        if self.uid is None or self._session is None or self._project_id is None:
            msg = "Cannot get the report for a predictor that wasn't read from the platform"
            raise ValueError(msg)
        return ReportResource(self._project_id, self._session).get(self.uid)

    @classmethod
    def get_type(cls, data) -> Type['Predictor']:
        """Return the subtype."""
        from .simple_ml_predictor import SimpleMLPredictor
        from .graph_predictor import GraphPredictor
        from .expression_predictor import ExpressionPredictor, DeprecatedExpressionPredictor
        from .molecular_structure_featurizer import MolecularStructureFeaturizer
        from .ingredients_to_simple_mixture_predictor import IngredientsToSimpleMixturePredictor
        from .generalized_mean_property_predictor import GeneralizedMeanPropertyPredictor
        from .label_fractions_predictor import LabelFractionsPredictor
        from .simple_mixture_predictor import SimpleMixturePredictor
        from .ingredient_fractions_predictor import IngredientFractionsPredictor
        from .auto_ml_predictor import AutoMLPredictor
        from .mean_property_predictor import MeanPropertyPredictor
        type_dict = {
            "Simple": SimpleMLPredictor,
            "Graph": GraphPredictor,
            "Expression": DeprecatedExpressionPredictor,
            "AnalyticExpression": ExpressionPredictor,
            "MoleculeFeaturizer": MolecularStructureFeaturizer,
            "IngredientsToSimpleMixture": IngredientsToSimpleMixturePredictor,
            "GeneralizedMeanProperty": GeneralizedMeanPropertyPredictor,
            "MeanProperty": MeanPropertyPredictor,
            "LabelFractions": LabelFractionsPredictor,
            "SimpleMixture": SimpleMixturePredictor,
            "IngredientFractions": IngredientFractionsPredictor,
            "AutoML": AutoMLPredictor,
        }
        typ = type_dict.get(data['config']['type'])

        if typ is not None:
            return typ
        else:
            raise ValueError(
                '{} is not a valid predictor type. '
                'Must be in {}.'.format(data['config']['type'], type_dict.keys())
            )

    def _wrap_training_data(self,
                            training_data: Optional[Union[DataSource, List[DataSource]]]
                            ) -> List[DataSource]:
        """Wraps a single training data source in a list.

        Parameters
        ----------
        training_data: Optional[Union[DataSource, List[DataSource]]]
            Either a single data source, list of data sources or ``None``

        Returns
        -------
        List[DataSource]
            A list of data sources

        """
        if training_data is None:
            return []
        if isinstance(training_data, DataSource):
            warn("Specifying training data as a single data source is deprecated. "
                 "Please use a list of data sources to create {} instead.".format(self),
                 DeprecationWarning)
            return [training_data]
        return training_data
