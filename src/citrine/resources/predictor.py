"""Resources that represent collections of predictors."""
from uuid import UUID
from typing import TypeVar, Optional, Mapping, List, Any

from citrine._rest.collection import Collection
from citrine._session import Session
from citrine.informatics.predictors import Predictor, GraphPredictor

CreationType = TypeVar('CreationType', bound=Predictor)


class PredictorCollection(Collection[Predictor]):
    """Represents the collection of all predictors for a project.

    Parameters
    ----------
    project_id: UUID
        the UUID of the project

    """

    _path_template = '/projects/{project_id}/modules'
    _individual_key = None
    _resource = Predictor
    _module_type = 'PREDICTOR'

    def __init__(self, project_id: UUID, session: Session):
        self.project_id = project_id
        self.session: Session = session

    def build(self, data: dict) -> Predictor:
        """Build an individual Predictor."""
        predictor: Predictor = Predictor.build(data)
        predictor.session = self.session
        predictor.post_build(self.project_id, data)
        return predictor

    def check_for_update(self, predictor_id: UUID) -> Optional[Predictor]:
        """
        Check if there are updates available for a predictor.

        This check does not update the predictor; it just returns the update that is available.
        To perform the update, the response should then be used to call PredictorCollection.update

        Parameters
        ----------
        predictor_id: UUID
            Unique identifier of the predictor to check

        Returns
        -------
        Optional[Predictor]
            The update, if an update is available; None otherwise.

        """
        path = "/projects/{}/predictors/{}/check-for-update".format(self.project_id, predictor_id)
        data = self.session.get_resource(path)
        if data["updatable"]:
            enveloped = GraphPredictor.stuff_predictor_into_envelope(data["update"])
            return Predictor.build(enveloped)
        else:
            return None

    def get_training_data(self, predictor_id: UUID, labels: List[str]
                          ) -> List[Mapping[str, Any]]:
        path = "/projects/{}/predictors/{}/training-data".format(self.project_id, predictor_id)
        data = self.session.post_resource(path, {"labels": labels}, params={"page": 1, "per_page": 1})
        return data["data"]
