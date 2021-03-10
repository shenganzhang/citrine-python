"""Resources that represent collections of design spaces."""
from uuid import UUID
from typing import TypeVar

from citrine._rest.collection import Collection
from citrine._session import Session
from citrine.informatics.design_spaces import DesignSpace, EnumeratedDesignSpace

CreationType = TypeVar('CreationType', bound=DesignSpace)


class DesignSpaceCollection(Collection[DesignSpace]):
    """Represents the collection of design spaces as well as the resources belonging to it.

    Parameters
    ----------
    project_id: UUID
        the UUID of the project

    """

    _path_template = '/projects/{project_id}/modules'
    _individual_key = None
    _resource = DesignSpace
    _module_type = 'DESIGN_SPACE'
    _enumerated_cell_limit = 128 * 2000

    def __init__(self, project_id: UUID, session: Session = Session()):
        self.project_id = project_id
        self.session: Session = session

    def build(self, data: dict) -> DesignSpace:
        """Build an individual design space."""
        design_space = DesignSpace.build(data)
        design_space.session = self.session
        return design_space

    def validate_write_request(self, design_space: DesignSpace):
        """Perform write-time validations of the design space registration or update.

        EnumeratedDesignSpaces can be pretty big, so we want to return a helpful error message
        rather than let the POST or PUT call fail because the request body is too big.  This
        validation is performed when the design space is sent to the platform in case a user
        creates a large intermediate design space but then filters it down before registering it.
        """
        if isinstance(design_space, EnumeratedDesignSpace):
            width = len(design_space.descriptors)
            length = len(design_space.data)
            if width * length > self._enumerated_cell_limit:
                msg = "EnumeratedDesignSpace only supports up to {} descriptor-values, " \
                      "but {} were given. Please reduce the number of descriptors or candidates " \
                      "in this EnumeratedDesignSpace"
                raise ValueError(msg.format(self._enumerated_cell_limit, width * length))
        return

    def register(self, model: DesignSpace) -> DesignSpace:
        """Create a new design space."""
        self.validate_write_request(model)
        return Collection.register(self, model)

    def update(self, model: DesignSpace) -> DesignSpace:
        """Update an existing design space by uid."""
        self.validate_write_request(model)
        return Collection.update(self, model)

    def create_default(self, predictor_id: UUID) -> DesignSpace:
        """[ALPHA] Create a default design space for a predictor.

        This method will return an unregistered design space for all inputs
        that are not responses of the predictor. The design space will contain a
        :class:`~citrine.informatics.design_spaces.formulation_design_space.FormulationDesignSpace`
        for each formulation input. Dimensions are constructed for all other inputs.
        A :class:`~citrine.informatics.dimensions.ContinuousDimension` is constructed for each
        input that corresponds to a :class:`~citrine.informatics.descriptors.RealDescriptor`.
        An :class:`~citrine.informatics.dimensions.EnumeratedDimension` is constructed for all
        other inputs. Enumerated values taken from the allowed ``categories`` of a
        :class:`~citrine.informatics.descriptors.CategoricalDescriptor` or from the
        unique values from the training data for all other descriptors.

        Parameters
        ----------
        predictor_id: UUID
            UUID of the predictor used to construct the design space

        Returns
        -------
        DesignSpace
            Default design space
        """
        path = f'projects/{self.project_id}/predictors/{predictor_id}/default-design-space'
        data = self.session.get_resource(path)
        return self.build(data)
