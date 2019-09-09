from citrine._rest.resource import Resource

from typing import TypeVar, List  # noqa: F401


Self = TypeVar('Self', bound='Resource')

class InformaticsModule(Resource['InformaticsModule']):
    """An abstract module class."""

    common_attrs = ["display_name",
                    "tags",
                    "status",
                    "source_id",
                    "status_info",
                    "id"]

    def __init__(self,
                 id: str = None,
                 display_name: str = None,
                 status: str = None,
                 source_id: str = None,
                 tags: List[str] = [],
                 status_info: List = []):
        self.uid = id
        self.status = status
        self.display_name = display_name
        self.source_id = source_id
        self.tags = tags
        self.status_info = status_info

    @classmethod
    def build(cls, data: dict) -> Self:
        """Build an instance of this object from given data."""
        built = super().build(data)
        built._set_module_instance(data["config"])
        return built

    def _post_dump(self, data):
        data["config"] = self._module_instance.for_json()
        data["schema_id"] = self.schema_id
        data["module_type"] = self.module_type
        return data