import python_jsonschema_objects as pjs
import humps
from copy import deepcopy
import pdb
from citrine.resources.module.informatics_block import InformaticsBlock
from citrine.resources.module.informatics_module import InformaticsModule
from citrine.resources.module.informatics_loader import load_schemas
from citrine.resources.module.schemas import SCHEMAS

from citrine._utils.classes import AttributeDict
from citrine._serialization import properties


class _Informatics():

    def __init__(self):
        self._module_registry = None
        self.load_informatics()

    @property
    def module_registry(self):
        if self._module_registry is None:
            self.load_informatics()
        return self._module_registry

    def __getattr__(self, item):
        if self._module_registry.get(item) is not None:
            return self._module_registry[item]
        return super().__getattr__(item)

    def get_klass(self, schema_id):
        return self._schema_id_map[schema_id]

    def load_informatics(self):
        self._module_registry = AttributeDict()
        self._schema_id_map = {}

        new_schemas, schema_class_meta_info = load_schemas(SCHEMAS)

        builder = pjs.ObjectBuilder(new_schemas)

        klasses = builder.build_classes(named_only=True, standardize_names=False)

        for klass_name in klasses:
            if klass_name is not 'Module':
                klass = klasses[klass_name]
                meta_info = schema_class_meta_info[klass_name]
                # See if, when we defined this class, it came from a module schema

                informatics_klass = self.build_informatics_klass(
                    klass_name,
                    klass,
                    meta_info
                )
                if meta_info.get("schema_id") is not None:
                    self._schema_id_map[meta_info["schema_id"]] = informatics_klass

                module_type_key = humps.pascalize(meta_info["module_type"].lower())
                if self._module_registry.get(module_type_key) is None:
                    self._module_registry[module_type_key] = AttributeDict()

                self._module_registry[module_type_key][klass_name] = informatics_klass

    def build_informatics_klass(self, klass_name, klass, meta_info):
        schema_id = meta_info.get("schema_id")
        module_type = meta_info.get("module_type")
        if schema_id is not None:

            def constructor(self, *args, **kwargs):
                general_kwargs = kwargs.copy()

                self._set_module_instance(kwargs)

                for attr_name in kwargs.keys():
                    if attr_name not in InformaticsModule.common_attrs:
                        del general_kwargs[attr_name]

                super(type(self), self).__init__(**general_kwargs)

            def _set_klass_instance(self, kwargs):
                module_kwargs = kwargs.copy()
                for attr_name in kwargs.keys():
                    if attr_name in InformaticsModule.common_attrs:
                        del module_kwargs[attr_name]
                self._module_instance = self._module_klass(
                    **module_kwargs
                )
                self._module_instance.validate()

            def _setattr(self, item, value):
                module_instantiated = hasattr(self, "_module_instance")
                if item not in InformaticsModule.common_attrs and module_instantiated:
                    self._module_instance.__setattr__(item, value)
                else:
                    super(type(self), self).__setattr__(item, value)

            def _getattr(self, item):
                if item == "_module_instance":
                    return super(type(self), self).__getattribute__(item)

                module_instantiated = hasattr(self, "_module_instance")
                if item not in InformaticsModule.common_attrs and module_instantiated:
                    return getattr(self._module_instance, item)
                else:
                    return super(type(self), self).__getattribute__(item)

            informatics_klass = type(
                klass_name,
                (InformaticsModule,),
                {
                    "__init__": constructor,
                    "_module_klass": klass,
                    "schema_id": schema_id,
                    "module_type": module_type,
                    "__setattr__": _setattr,
                    "__getattr__": _getattr,
                    "_set_module_instance": _set_klass_instance,
                }
            )

            informatics_klass.uid = properties.Optional(properties.UUID, 'id', serializable=False)
            informatics_klass.source_id = properties.Optional(properties.UUID, 'source_id', serializable=False)
            informatics_klass.display_name = properties.String("display_name")
            informatics_klass.description = properties.Optional(properties.String(), "description")
            informatics_klass.status = properties.Optional(properties.String(), "status", serializable=False)
            informatics_klass.status_info = properties.Optional(
                properties.List(properties.String()),
                'status_info',
                serializable=False
            )
            informatics_klass.tags = properties.Optional(
                properties.List(properties.String()),
                'tags'
            )
            informatics_klass.schema_id = schema_id
            informatics_klass.module_type = module_type
            informatics_klass._module_klass = klass
            return informatics_klass
        else:
            informatics_klass = type(
                klass_name,
                (klass, InformaticsBlock),
                {}
            )
            informatics_klass.module_type = module_type
            return informatics_klass

Informatics = _Informatics()