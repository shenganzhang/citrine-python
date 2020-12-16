"""Tools for working with design spaces."""
from typing import Type

from citrine._serialization.serializable import Serializable
from citrine.informatics.modules import Module

__all__ = ['DesignSpace']


class DesignSpace(Module):
    """[ALPHA] A Citrine Design Space describes the set of materials that can be made.

    Abstract type that returns the proper type given a serialized dict.


    """

    _response_key = None

    @classmethod
    def get_type(cls, data) -> Type[Serializable]:
        """Return the subtype."""
        from .data_source_design_space import DataSourceDesignSpace
        from .enumerated_design_space import EnumeratedDesignSpace
        from .formulation_design_space import FormulationDesignSpace
        from .product_design_space import ProductDesignSpace
        return {
            'Univariate': ProductDesignSpace,
            'ProductDesignSpace': ProductDesignSpace
            'EnumeratedDesignSpace': EnumeratedDesignSpace,
            'FormulationDesignSpace': FormulationDesignSpace,
            'DataSourceDesignSpace': DataSourceDesignSpace
        }[data['config']['type']]
