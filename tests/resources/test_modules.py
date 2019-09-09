from citrine.resources.module.informatics import Informatics
from citrine.resources.module.module import Module
import pdb

univariate_dict = {
            "type": "Univariate",
            "name": "2d grid",
            "dimensions": [
                {
                    "type": "ContinuousDimension",
                    "descriptor": {
                        "type": "Real",
                        "units": "",
                        "lower_bound": 0,
                        "upper_bound": 1000,
                        "descriptor_key": "x"
                    },
                    "lower_bound": 0,
                    "template_id": "d4e058d0-a9b7-4538-b773-ba77274399c5",
                    "upper_bound": 10
                },
                {
                    "type": "ContinuousDimension",
                    "descriptor": {
                        "type": "Real",
                        "units": "",
                        "lower_bound": 0,
                        "upper_bound": 1000,
                        "descriptor_key": "y"
                    },
                    "lower_bound": 0,
                    "template_id": "c71b481f-e69a-46bc-a78e-739c0e9df6d0",
                    "upper_bound": 10
                }
            ],
            "description": "Product of continuous real dimensions x and y"
        }

def test_can_load_informatics():
    print("\n")
    for key, value in Informatics.module_registry.items():
        print("For type {}, there are:".format(key))
        for type in value.keys():
            print(type)
        print("\n")

def test_can_init_cap():

    x = Informatics.Descriptor.Real(
        descriptor_key="x",
        lower_bound=0.0,
        upper_bound=1000.0,
        description=""
    )

    y = Informatics.Descriptor.Real(
        descriptor_key="y",
        lower_bound=0.0,
        upper_bound=1000.0,
        description=""
    )

    dimensions = [
        Informatics.Dimension.ContinuousDimension(
            descriptor=x,
            lower_bound=0,
            upper_bound=10.0,
            template_id="asdf"
        ),
        Informatics.Dimension.ContinuousDimension(
            descriptor=y,
            lower_bound=0,
            upper_bound=10.0,
            template_id="asdf"
        ),
    ]

    capability = Informatics.Capability.Univariate(
        display_name="New Capability",
        name='2d grid',
        description='Product of continuous real dimensions x and y',
        dimensions=dimensions
    )
    pdb.set_trace()

def test_can_deserialize_capability():
    dimension = Informatics.Dimension.ContinuousDimension.build({
                    "descriptor": {
                        "type": "Real",
                        "units": "",
                        "lower_bound": 0,
                        "upper_bound": 1000,
                        "descriptor_key": "y"
                    },
                    "lower_bound": 0,
                    "template_id": "c71b481f-e69a-46bc-a78e-739c0e9df6d0",
                    "upper_bound": 10
                })
    dimension.validate()

def test_can_deserialize():
    module = {
        "display_name": "2d grid",
        "config": univariate_dict,
        "tags": [],
        "source_id": None,
        "schema_id": "6c16d694-d015-42a7-b462-8ef299473c9a",
        "module_type": "CAPABILITY",
        "status": "VALIDATING",
        "status_info": None,
        "id": "7a768b85-5970-4cd9-8dfa-711d2fe2a4b2"
    }
    module = Module.build(module)
    pdb.set_trace()
