from citrine._rest.resource import Resource
from typing import TypeVar  # noqa: F401


Self = TypeVar('Self', bound='Resource')

class InformaticsBlock(Resource['Module']):

    @classmethod
    def build(cls, data: dict) -> Self:
        return cls(**data)

    def dump(self) -> dict:
        return self.for_json()