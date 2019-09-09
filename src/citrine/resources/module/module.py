from citrine._serialization.polymorphic_serializable import PolymorphicSerializable
from citrine._serialization.serializable import Serializable

from citrine.resources.module.informatics import Informatics

from typing import Type

class Module(PolymorphicSerializable["Module"]):

    @classmethod
    def get_type(cls, data) -> Type[Serializable]:
        """Return the subtype."""
        return Informatics.get_klass(data["schema_id"])



