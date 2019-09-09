SCHEMAS = [
    {
        "id": "f85e379f-e28b-4d61-8caf-df355e1470e7",
        "module_type": "SCORE",
        "display_name": "OrionMEIScore",
        "schema": {
            "type": "object",
            "title": "MEI",
            "schema": "http://json-schema.org/draft-04/schema#",
            "required": [
                "type",
                "name",
                "description",
                "objectives",
                "constraints",
                "baselines"
            ],
            "properties": {
                "name": {
                    "type": "string"
                },
                "type": {
                    "enum": [
                        "MEI"
                    ],
                    "type": "string",
                    "default": "MEI"
                },
                "baselines": {
                    "type": "array",
                    "items": {
                        "type": "number"
                    }
                },
                "objectives": {
                    "type": "array",
                    "items": {
                        "oneOf": [
                            {
                                "$ref": "#/definitions/OrionScalarMaxObjective"
                            },
                            {
                                "$ref": "#/definitions/OrionScalarMinObjective"
                            },
                            {
                                "$ref": "#/definitions/OrionScalarTuneObjective"
                            }
                        ]
                    }
                },
                "constraints": {
                    "type": "array",
                    "items": {
                        "oneOf": [
                            {
                                "$ref": "#/definitions/OrionRealRangeConstraint"
                            },
                            {
                                "$ref": "#/definitions/OrionElementalConstraint"
                            },
                            {
                                "$ref": "#/definitions/OrionClassMembershipConstraint"
                            },
                            {
                                "$ref": "#/definitions/OrionCompositionRangeConstraint"
                            }
                        ]
                    }
                },
                "description": {
                    "type": "string"
                }
            },
            "definitions": {
                "orion_scalar_max_objective": {
                    "type": "object",
                    "title": "ScalarMax",
                    "required": [
                        "type",
                        "descriptor_key",
                        "lower_bound",
                        "upper_bound"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "ScalarMax"
                            ],
                            "type": "string",
                            "default": "ScalarMax"
                        },
                        "lower_bound": {
                            "type": "number"
                        },
                        "upper_bound": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_scalar_min_objective": {
                    "type": "object",
                    "title": "ScalarMin",
                    "required": [
                        "type",
                        "descriptor_key",
                        "lower_bound",
                        "upper_bound"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "ScalarMin"
                            ],
                            "type": "string",
                            "default": "ScalarMin"
                        },
                        "lower_bound": {
                            "type": "number"
                        },
                        "upper_bound": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_elemental_constraint": {
                    "type": "object",
                    "title": "Elemental",
                    "required": [
                        "type",
                        "descriptor_key",
                        "required_elements",
                        "restricted_elements"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Elemental"
                            ],
                            "type": "string",
                            "default": "Elemental"
                        },
                        "descriptor_key": {
                            "type": "string",
                            "description": "Descriptor key"
                        },
                        "required_elements": {
                            "type": "array",
                            "items": {
                                "enum": [
                                    "HYDROGEN",
                                    "DEUTERIUM",
                                    "TRITIUM",
                                    "HELIUM",
                                    "LITHIUM",
                                    "BERYLLIUM",
                                    "BORON",
                                    "CARBON",
                                    "NITROGEN",
                                    "OXYGEN",
                                    "FLUORINE",
                                    "NEON",
                                    "SODIUM",
                                    "MAGNESIUM",
                                    "ALUMINUM",
                                    "SILICON",
                                    "PHOSPHORUS",
                                    "SULFUR",
                                    "CHLORINE",
                                    "ARGON",
                                    "POTASSIUM",
                                    "CALCIUM",
                                    "SCANDIUM",
                                    "TITANIUM",
                                    "VANADIUM",
                                    "CHROMIUM",
                                    "MANGANESE",
                                    "IRON",
                                    "COBALT",
                                    "NICKEL",
                                    "COPPER",
                                    "ZINC",
                                    "GALLIUM",
                                    "GERMANIUM",
                                    "ARSENIC",
                                    "SELENIUM",
                                    "BROMINE",
                                    "KRYPTON",
                                    "RUBIDIUM",
                                    "STRONTIUM",
                                    "YTTRIUM",
                                    "ZIRCONIUM",
                                    "NIOBIUM",
                                    "MOLYBDENUM",
                                    "TECHNETIUM",
                                    "RUTHENIUM",
                                    "RHODIUM",
                                    "PALLADIUM",
                                    "SILVER",
                                    "CADMIUM",
                                    "INDIUM",
                                    "TIN",
                                    "ANTIMONY",
                                    "TELLURIUM",
                                    "IODINE",
                                    "XENON",
                                    "CESIUM",
                                    "BARIUM",
                                    "LANTHANUM",
                                    "CERIUM",
                                    "PRASEODYMIUM",
                                    "NEODYMIUM",
                                    "PROMETHIUM",
                                    "SAMARIUM",
                                    "EUROPIUM",
                                    "GADOLINIUM",
                                    "TERBIUM",
                                    "DYSPROSIUM",
                                    "HOLMIUM",
                                    "ERBIUM",
                                    "THULIUM",
                                    "YTTERBIUM",
                                    "LUTETIUM",
                                    "HAFNIUM",
                                    "TANTALUM",
                                    "TUNGSTEN",
                                    "RHENIUM",
                                    "OSMIUM",
                                    "IRIDIUM",
                                    "PLATINUM",
                                    "GOLD",
                                    "MERCURY",
                                    "THALLIUM",
                                    "LEAD",
                                    "BISMUTH",
                                    "POLONIUM",
                                    "ASTATINE",
                                    "RADON",
                                    "FRANCIUM",
                                    "RADIUM",
                                    "ACTINIUM",
                                    "THORIUM",
                                    "PROTACTINIUM",
                                    "URANIUM",
                                    "NEPTUNIUM",
                                    "PLUTONIUM",
                                    "AMERICIUM",
                                    "CURIUM",
                                    "BERKELIUM",
                                    "CALIFORNIUM",
                                    "EINSTEINIUM",
                                    "FERMIUM",
                                    "MENDELEVIUM",
                                    "NOBELIUM",
                                    "LAWRENCIUM",
                                    "RUTHERFORDIUM",
                                    "DUBNIUM",
                                    "SEABORGIUM",
                                    "BOHRIUM",
                                    "HASSIUM",
                                    "MEITNERIUM",
                                    "DARMSTADTIUM",
                                    "ROENTGENIUM",
                                    "COPERNICIUM",
                                    "FLEROVIUM",
                                    "LIVERMORIUM",
                                    "WILDCARD"
                                ],
                                "type": "string"
                            }
                        },
                        "restricted_elements": {
                            "type": "array",
                            "items": {
                                "enum": [
                                    "HYDROGEN",
                                    "DEUTERIUM",
                                    "TRITIUM",
                                    "HELIUM",
                                    "LITHIUM",
                                    "BERYLLIUM",
                                    "BORON",
                                    "CARBON",
                                    "NITROGEN",
                                    "OXYGEN",
                                    "FLUORINE",
                                    "NEON",
                                    "SODIUM",
                                    "MAGNESIUM",
                                    "ALUMINUM",
                                    "SILICON",
                                    "PHOSPHORUS",
                                    "SULFUR",
                                    "CHLORINE",
                                    "ARGON",
                                    "POTASSIUM",
                                    "CALCIUM",
                                    "SCANDIUM",
                                    "TITANIUM",
                                    "VANADIUM",
                                    "CHROMIUM",
                                    "MANGANESE",
                                    "IRON",
                                    "COBALT",
                                    "NICKEL",
                                    "COPPER",
                                    "ZINC",
                                    "GALLIUM",
                                    "GERMANIUM",
                                    "ARSENIC",
                                    "SELENIUM",
                                    "BROMINE",
                                    "KRYPTON",
                                    "RUBIDIUM",
                                    "STRONTIUM",
                                    "YTTRIUM",
                                    "ZIRCONIUM",
                                    "NIOBIUM",
                                    "MOLYBDENUM",
                                    "TECHNETIUM",
                                    "RUTHENIUM",
                                    "RHODIUM",
                                    "PALLADIUM",
                                    "SILVER",
                                    "CADMIUM",
                                    "INDIUM",
                                    "TIN",
                                    "ANTIMONY",
                                    "TELLURIUM",
                                    "IODINE",
                                    "XENON",
                                    "CESIUM",
                                    "BARIUM",
                                    "LANTHANUM",
                                    "CERIUM",
                                    "PRASEODYMIUM",
                                    "NEODYMIUM",
                                    "PROMETHIUM",
                                    "SAMARIUM",
                                    "EUROPIUM",
                                    "GADOLINIUM",
                                    "TERBIUM",
                                    "DYSPROSIUM",
                                    "HOLMIUM",
                                    "ERBIUM",
                                    "THULIUM",
                                    "YTTERBIUM",
                                    "LUTETIUM",
                                    "HAFNIUM",
                                    "TANTALUM",
                                    "TUNGSTEN",
                                    "RHENIUM",
                                    "OSMIUM",
                                    "IRIDIUM",
                                    "PLATINUM",
                                    "GOLD",
                                    "MERCURY",
                                    "THALLIUM",
                                    "LEAD",
                                    "BISMUTH",
                                    "POLONIUM",
                                    "ASTATINE",
                                    "RADON",
                                    "FRANCIUM",
                                    "RADIUM",
                                    "ACTINIUM",
                                    "THORIUM",
                                    "PROTACTINIUM",
                                    "URANIUM",
                                    "NEPTUNIUM",
                                    "PLUTONIUM",
                                    "AMERICIUM",
                                    "CURIUM",
                                    "BERKELIUM",
                                    "CALIFORNIUM",
                                    "EINSTEINIUM",
                                    "FERMIUM",
                                    "MENDELEVIUM",
                                    "NOBELIUM",
                                    "LAWRENCIUM",
                                    "RUTHERFORDIUM",
                                    "DUBNIUM",
                                    "SEABORGIUM",
                                    "BOHRIUM",
                                    "HASSIUM",
                                    "MEITNERIUM",
                                    "DARMSTADTIUM",
                                    "ROENTGENIUM",
                                    "COPERNICIUM",
                                    "FLEROVIUM",
                                    "LIVERMORIUM",
                                    "WILDCARD"
                                ],
                                "type": "string"
                            }
                        }
                    },
                    "additional_properties": False
                },
                "orion_real_range_constraint": {
                    "type": "object",
                    "title": "ScalarRange",
                    "required": [
                        "type",
                        "descriptor_key"
                    ],
                    "properties": {
                        "max": {
                            "type": "number"
                        },
                        "min": {
                            "type": "number"
                        },
                        "type": {
                            "enum": [
                                "ScalarRange"
                            ],
                            "type": "string",
                            "default": "ScalarRange"
                        },
                        "max_inclusive": {
                            "type": "boolean"
                        },
                        "min_inclusive": {
                            "type": "boolean"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_scalar_tune_objective": {
                    "type": "object",
                    "title": "TargetValue",
                    "required": [
                        "type",
                        "descriptor_key",
                        "target",
                        "power"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "TargetValue"
                            ],
                            "type": "string",
                            "default": "TargetValue"
                        },
                        "power": {
                            "type": "number"
                        },
                        "target": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_class_membership_constraint": {
                    "type": "object",
                    "title": "ClassMembership",
                    "required": [
                        "type",
                        "descriptor_key",
                        "acceptable_classes"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Categorical"
                            ],
                            "type": "string",
                            "default": "Categorical"
                        },
                        "descriptor_key": {
                            "type": "string"
                        },
                        "acceptable_classes": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        }
                    },
                    "additional_properties": False
                },
                "orion_composition_range_constraint": {
                    "type": "object",
                    "title": "CompositionRange",
                    "required": [
                        "type",
                        "descriptor_key",
                        "element"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "CompositionRange"
                            ],
                            "type": "string",
                            "default": "CompositionRange"
                        },
                        "basis": {
                            "type": "number"
                        },
                        "element": {
                            "enum": [
                                "HYDROGEN",
                                "DEUTERIUM",
                                "TRITIUM",
                                "HELIUM",
                                "LITHIUM",
                                "BERYLLIUM",
                                "BORON",
                                "CARBON",
                                "NITROGEN",
                                "OXYGEN",
                                "FLUORINE",
                                "NEON",
                                "SODIUM",
                                "MAGNESIUM",
                                "ALUMINUM",
                                "SILICON",
                                "PHOSPHORUS",
                                "SULFUR",
                                "CHLORINE",
                                "ARGON",
                                "POTASSIUM",
                                "CALCIUM",
                                "SCANDIUM",
                                "TITANIUM",
                                "VANADIUM",
                                "CHROMIUM",
                                "MANGANESE",
                                "IRON",
                                "COBALT",
                                "NICKEL",
                                "COPPER",
                                "ZINC",
                                "GALLIUM",
                                "GERMANIUM",
                                "ARSENIC",
                                "SELENIUM",
                                "BROMINE",
                                "KRYPTON",
                                "RUBIDIUM",
                                "STRONTIUM",
                                "YTTRIUM",
                                "ZIRCONIUM",
                                "NIOBIUM",
                                "MOLYBDENUM",
                                "TECHNETIUM",
                                "RUTHENIUM",
                                "RHODIUM",
                                "PALLADIUM",
                                "SILVER",
                                "CADMIUM",
                                "INDIUM",
                                "TIN",
                                "ANTIMONY",
                                "TELLURIUM",
                                "IODINE",
                                "XENON",
                                "CESIUM",
                                "BARIUM",
                                "LANTHANUM",
                                "CERIUM",
                                "PRASEODYMIUM",
                                "NEODYMIUM",
                                "PROMETHIUM",
                                "SAMARIUM",
                                "EUROPIUM",
                                "GADOLINIUM",
                                "TERBIUM",
                                "DYSPROSIUM",
                                "HOLMIUM",
                                "ERBIUM",
                                "THULIUM",
                                "YTTERBIUM",
                                "LUTETIUM",
                                "HAFNIUM",
                                "TANTALUM",
                                "TUNGSTEN",
                                "RHENIUM",
                                "OSMIUM",
                                "IRIDIUM",
                                "PLATINUM",
                                "GOLD",
                                "MERCURY",
                                "THALLIUM",
                                "LEAD",
                                "BISMUTH",
                                "POLONIUM",
                                "ASTATINE",
                                "RADON",
                                "FRANCIUM",
                                "RADIUM",
                                "ACTINIUM",
                                "THORIUM",
                                "PROTACTINIUM",
                                "URANIUM",
                                "NEPTUNIUM",
                                "PLUTONIUM",
                                "AMERICIUM",
                                "CURIUM",
                                "BERKELIUM",
                                "CALIFORNIUM",
                                "EINSTEINIUM",
                                "FERMIUM",
                                "MENDELEVIUM",
                                "NOBELIUM",
                                "LAWRENCIUM",
                                "RUTHERFORDIUM",
                                "DUBNIUM",
                                "SEABORGIUM",
                                "BOHRIUM",
                                "HASSIUM",
                                "MEITNERIUM",
                                "DARMSTADTIUM",
                                "ROENTGENIUM",
                                "COPERNICIUM",
                                "FLEROVIUM",
                                "LIVERMORIUM",
                                "WILDCARD"
                            ],
                            "type": "string"
                        },
                        "max_frac": {
                            "type": "number"
                        },
                        "min_frac": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        },
                        "el_is_required": {
                            "type": "boolean"
                        }
                    },
                    "additional_properties": False
                }
            },
            "additional_properties": False
        },
        "tags": []
    },
    {
        "id": "6c16d694-d015-42a7-b462-8ef299473c9a",
        "module_type": "CAPABILITY",
        "display_name": "OrionUnivariateProductCapability",
        "schema": {
            "type": "object",
            "title": "Univariate",
            "schema": "http://json-schema.org/draft-04/schema#",
            "required": [
                "type",
                "name",
                "description",
                "dimensions"
            ],
            "properties": {
                "name": {
                    "type": "string"
                },
                "type": {
                    "enum": [
                        "Univariate"
                    ],
                    "type": "string",
                    "default": "Univariate"
                },
                "dimensions": {
                    "type": "array",
                    "items": {
                        "oneOf": [
                            {
                                "$ref": "#/definitions/OrionContinuousDimension"
                            },
                            {
                                "$ref": "#/definitions/OrionEnumeratedDimension"
                            }
                        ]
                    }
                },
                "description": {
                    "type": "string"
                }
            },
            "definitions": {
                "orion_int_descriptor": {
                    "type": "object",
                    "title": "Integer",
                    "required": [
                        "type",
                        "lower_bound",
                        "upper_bound"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Integer"
                            ],
                            "type": "string",
                            "default": "Integer"
                        },
                        "units": {
                            "type": "string"
                        },
                        "lower_bound": {
                            "type": "integer"
                        },
                        "upper_bound": {
                            "type": "integer"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_real_descriptor": {
                    "type": "object",
                    "title": "Real",
                    "required": [
                        "type",
                        "lower_bound",
                        "upper_bound"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Real"
                            ],
                            "type": "string",
                            "default": "Real"
                        },
                        "units": {
                            "type": "string"
                        },
                        "lower_bound": {
                            "type": "number"
                        },
                        "upper_bound": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_continuous_dimension": {
                    "type": "object",
                    "title": "ContinuousDimension",
                    "required": [
                        "type",
                        "descriptor",
                        "lower_bound",
                        "upper_bound",
                        "template_id"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "ContinuousDimension"
                            ],
                            "type": "string",
                            "default": "ContinuousDimension"
                        },
                        "descriptor": {
                            "$ref": "#/definitions/OrionRealDescriptor"
                        },
                        "lower_bound": {
                            "type": "number"
                        },
                        "upper_bound": {
                            "type": "number"
                        },
                        "template_id": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_enumerated_dimension": {
                    "type": "object",
                    "title": "EnumeratedDimension",
                    "required": [
                        "type",
                        "template_id",
                        "descriptor",
                        "list"
                    ],
                    "properties": {
                        "list": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },
                        "type": {
                            "enum": [
                                "EnumeratedDimension"
                            ],
                            "type": "string",
                            "default": "EnumeratedDimension"
                        },
                        "descriptor": {
                            "oneOf": [
                                {
                                    "$ref": "#/definitions/OrionCategoricalDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionOrganicChemicalFormulaDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionIntDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionRealDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionRealVectorDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionMetalAlloyDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionAlloyCompositionDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionInorganicChemicalFormulaDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionFormulationDescriptor"
                                }
                            ]
                        },
                        "template_id": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_metal_alloy_descriptor": {
                    "type": "object",
                    "title": "MetalAlloy",
                    "required": [
                        "type",
                        "threshold"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Metal Alloy"
                            ],
                            "type": "string",
                            "default": "Metal Alloy"
                        },
                        "threshold": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        },
                        "primary_elements": {
                            "type": "array",
                            "items": {
                                "enum": [
                                    "HYDROGEN",
                                    "DEUTERIUM",
                                    "TRITIUM",
                                    "HELIUM",
                                    "LITHIUM",
                                    "BERYLLIUM",
                                    "BORON",
                                    "CARBON",
                                    "NITROGEN",
                                    "OXYGEN",
                                    "FLUORINE",
                                    "NEON",
                                    "SODIUM",
                                    "MAGNESIUM",
                                    "ALUMINUM",
                                    "SILICON",
                                    "PHOSPHORUS",
                                    "SULFUR",
                                    "CHLORINE",
                                    "ARGON",
                                    "POTASSIUM",
                                    "CALCIUM",
                                    "SCANDIUM",
                                    "TITANIUM",
                                    "VANADIUM",
                                    "CHROMIUM",
                                    "MANGANESE",
                                    "IRON",
                                    "COBALT",
                                    "NICKEL",
                                    "COPPER",
                                    "ZINC",
                                    "GALLIUM",
                                    "GERMANIUM",
                                    "ARSENIC",
                                    "SELENIUM",
                                    "BROMINE",
                                    "KRYPTON",
                                    "RUBIDIUM",
                                    "STRONTIUM",
                                    "YTTRIUM",
                                    "ZIRCONIUM",
                                    "NIOBIUM",
                                    "MOLYBDENUM",
                                    "TECHNETIUM",
                                    "RUTHENIUM",
                                    "RHODIUM",
                                    "PALLADIUM",
                                    "SILVER",
                                    "CADMIUM",
                                    "INDIUM",
                                    "TIN",
                                    "ANTIMONY",
                                    "TELLURIUM",
                                    "IODINE",
                                    "XENON",
                                    "CESIUM",
                                    "BARIUM",
                                    "LANTHANUM",
                                    "CERIUM",
                                    "PRASEODYMIUM",
                                    "NEODYMIUM",
                                    "PROMETHIUM",
                                    "SAMARIUM",
                                    "EUROPIUM",
                                    "GADOLINIUM",
                                    "TERBIUM",
                                    "DYSPROSIUM",
                                    "HOLMIUM",
                                    "ERBIUM",
                                    "THULIUM",
                                    "YTTERBIUM",
                                    "LUTETIUM",
                                    "HAFNIUM",
                                    "TANTALUM",
                                    "TUNGSTEN",
                                    "RHENIUM",
                                    "OSMIUM",
                                    "IRIDIUM",
                                    "PLATINUM",
                                    "GOLD",
                                    "MERCURY",
                                    "THALLIUM",
                                    "LEAD",
                                    "BISMUTH",
                                    "POLONIUM",
                                    "ASTATINE",
                                    "RADON",
                                    "FRANCIUM",
                                    "RADIUM",
                                    "ACTINIUM",
                                    "THORIUM",
                                    "PROTACTINIUM",
                                    "URANIUM",
                                    "NEPTUNIUM",
                                    "PLUTONIUM",
                                    "AMERICIUM",
                                    "CURIUM",
                                    "BERKELIUM",
                                    "CALIFORNIUM",
                                    "EINSTEINIUM",
                                    "FERMIUM",
                                    "MENDELEVIUM",
                                    "NOBELIUM",
                                    "LAWRENCIUM",
                                    "RUTHERFORDIUM",
                                    "DUBNIUM",
                                    "SEABORGIUM",
                                    "BOHRIUM",
                                    "HASSIUM",
                                    "MEITNERIUM",
                                    "DARMSTADTIUM",
                                    "ROENTGENIUM",
                                    "COPERNICIUM",
                                    "FLEROVIUM",
                                    "LIVERMORIUM",
                                    "WILDCARD"
                                ],
                                "type": "string"
                            }
                        }
                    },
                    "additional_properties": False
                },
                "orion_real_vector_descriptor": {
                    "type": "object",
                    "title": "Vector",
                    "required": [
                        "type",
                        "descriptor_key",
                        "length"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Vector"
                            ],
                            "type": "string",
                            "default": "Vector"
                        },
                        "units": {
                            "type": "string"
                        },
                        "length": {
                            "type": "integer"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_categorical_descriptor": {
                    "type": "object",
                    "title": "Categorical",
                    "required": [
                        "type"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Categorical"
                            ],
                            "type": "string",
                            "default": "Categorical"
                        },
                        "descriptor_key": {
                            "type": "string"
                        },
                        "descriptor_values": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        }
                    },
                    "additional_properties": False
                },
                "orion_formulation_descriptor": {
                    "type": "object",
                    "title": "Formulation",
                    "required": [
                        "type"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Formulation"
                            ],
                            "type": "string",
                            "default": "Formulation"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_alloy_composition_descriptor": {
                    "type": "object",
                    "title": "AlloyComposition",
                    "required": [
                        "type",
                        "descriptor_key",
                        "balance_element",
                        "basis",
                        "threshold"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Alloy composition"
                            ],
                            "type": "string",
                            "default": "Alloy composition"
                        },
                        "basis": {
                            "type": "number"
                        },
                        "threshold": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        },
                        "balance_element": {
                            "enum": [
                                "HYDROGEN",
                                "DEUTERIUM",
                                "TRITIUM",
                                "HELIUM",
                                "LITHIUM",
                                "BERYLLIUM",
                                "BORON",
                                "CARBON",
                                "NITROGEN",
                                "OXYGEN",
                                "FLUORINE",
                                "NEON",
                                "SODIUM",
                                "MAGNESIUM",
                                "ALUMINUM",
                                "SILICON",
                                "PHOSPHORUS",
                                "SULFUR",
                                "CHLORINE",
                                "ARGON",
                                "POTASSIUM",
                                "CALCIUM",
                                "SCANDIUM",
                                "TITANIUM",
                                "VANADIUM",
                                "CHROMIUM",
                                "MANGANESE",
                                "IRON",
                                "COBALT",
                                "NICKEL",
                                "COPPER",
                                "ZINC",
                                "GALLIUM",
                                "GERMANIUM",
                                "ARSENIC",
                                "SELENIUM",
                                "BROMINE",
                                "KRYPTON",
                                "RUBIDIUM",
                                "STRONTIUM",
                                "YTTRIUM",
                                "ZIRCONIUM",
                                "NIOBIUM",
                                "MOLYBDENUM",
                                "TECHNETIUM",
                                "RUTHENIUM",
                                "RHODIUM",
                                "PALLADIUM",
                                "SILVER",
                                "CADMIUM",
                                "INDIUM",
                                "TIN",
                                "ANTIMONY",
                                "TELLURIUM",
                                "IODINE",
                                "XENON",
                                "CESIUM",
                                "BARIUM",
                                "LANTHANUM",
                                "CERIUM",
                                "PRASEODYMIUM",
                                "NEODYMIUM",
                                "PROMETHIUM",
                                "SAMARIUM",
                                "EUROPIUM",
                                "GADOLINIUM",
                                "TERBIUM",
                                "DYSPROSIUM",
                                "HOLMIUM",
                                "ERBIUM",
                                "THULIUM",
                                "YTTERBIUM",
                                "LUTETIUM",
                                "HAFNIUM",
                                "TANTALUM",
                                "TUNGSTEN",
                                "RHENIUM",
                                "OSMIUM",
                                "IRIDIUM",
                                "PLATINUM",
                                "GOLD",
                                "MERCURY",
                                "THALLIUM",
                                "LEAD",
                                "BISMUTH",
                                "POLONIUM",
                                "ASTATINE",
                                "RADON",
                                "FRANCIUM",
                                "RADIUM",
                                "ACTINIUM",
                                "THORIUM",
                                "PROTACTINIUM",
                                "URANIUM",
                                "NEPTUNIUM",
                                "PLUTONIUM",
                                "AMERICIUM",
                                "CURIUM",
                                "BERKELIUM",
                                "CALIFORNIUM",
                                "EINSTEINIUM",
                                "FERMIUM",
                                "MENDELEVIUM",
                                "NOBELIUM",
                                "LAWRENCIUM",
                                "RUTHERFORDIUM",
                                "DUBNIUM",
                                "SEABORGIUM",
                                "BOHRIUM",
                                "HASSIUM",
                                "MEITNERIUM",
                                "DARMSTADTIUM",
                                "ROENTGENIUM",
                                "COPERNICIUM",
                                "FLEROVIUM",
                                "LIVERMORIUM",
                                "WILDCARD"
                            ],
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_organic_chemical_formula_descriptor": {
                    "type": "object",
                    "title": "Organic",
                    "required": [
                        "type",
                        "descriptor_key"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Organic"
                            ],
                            "type": "string",
                            "default": "Organic"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_inorganic_chemical_formula_descriptor": {
                    "type": "object",
                    "title": "Inorganic",
                    "required": [
                        "type",
                        "threshold"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Inorganic"
                            ],
                            "type": "string",
                            "default": "Inorganic"
                        },
                        "threshold": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                }
            },
            "additional_properties": False
        },
        "tags": []
    },
    {
        "id": "307b88a2-fd50-4d27-ae91-b8d6282f68f7",
        "module_type": "PROCESSOR",
        "display_name": "OrionEnumeratedProcessor",
        "schema": {
            "type": "object",
            "title": "Enumerated",
            "schema": "http://json-schema.org/draft-04/schema#",
            "required": [
                "type",
                "name",
                "description",
                "max_size"
            ],
            "properties": {
                "name": {
                    "type": "string"
                },
                "type": {
                    "enum": [
                        "Enumerated"
                    ],
                    "type": "string",
                    "default": "Enumerated"
                },
                "max_size": {
                    "type": "integer"
                },
                "description": {
                    "type": "string"
                }
            },
            "additional_properties": False
        },
        "tags": []
    },
    {
        "id": "db515644-4a27-4627-9b96-db661a711766",
        "module_type": "OBJECTIVE",
        "display_name": "OrionScalarMinObjective",
        "schema": {
            "type": "object",
            "title": "ScalarMin",
            "schema": "http://json-schema.org/draft-04/schema#",
            "required": [
                "type",
                "descriptor_key",
                "lower_bound",
                "upper_bound"
            ],
            "properties": {
                "type": {
                    "enum": [
                        "ScalarMin"
                    ],
                    "type": "string",
                    "default": "ScalarMin"
                },
                "lower_bound": {
                    "type": "number"
                },
                "upper_bound": {
                    "type": "number"
                },
                "descriptor_key": {
                    "type": "string"
                }
            },
            "additional_properties": False
        },
        "tags": []
    },
    {
        "id": "ff26b280-8a8b-46ab-b7aa-0c73ff84b0fd",
        "module_type": "PREDICTOR",
        "display_name": "OrionParaboloidPredictorConfiguration",
        "schema": {
            "type": "object",
            "title": "Paraboloid",
            "schema": "http://json-schema.org/draft-04/schema#",
            "required": [
                "type",
                "name",
                "description",
                "inputs",
                "output"
            ],
            "properties": {
                "name": {
                    "type": "string"
                },
                "type": {
                    "enum": [
                        "Paraboloid"
                    ],
                    "type": "string",
                    "default": "Paraboloid"
                },
                "inputs": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/OrionRealDescriptor"
                    }
                },
                "output": {
                    "$ref": "#/definitions/OrionRealDescriptor"
                },
                "description": {
                    "type": "string"
                }
            },
            "definitions": {
                "orion_real_descriptor": {
                    "type": "object",
                    "title": "Real",
                    "required": [
                        "type",
                        "lower_bound",
                        "upper_bound"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Real"
                            ],
                            "type": "string",
                            "default": "Real"
                        },
                        "units": {
                            "type": "string"
                        },
                        "lower_bound": {
                            "type": "number"
                        },
                        "upper_bound": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                }
            },
            "additional_properties": False
        },
        "tags": []
    },
    {
        "id": "3d7bc424-aee7-4386-bdbc-b912acfa89bf",
        "module_type": "PREDICTOR",
        "display_name": "OrionIndependentPropertyPredictorConfiguration",
        "schema": {
            "type": "object",
            "title": "Independent",
            "schema": "http://json-schema.org/draft-04/schema#",
            "required": [
                "type",
                "name",
                "description",
                "predictors"
            ],
            "properties": {
                "name": {
                    "type": "string"
                },
                "type": {
                    "enum": [
                        "Independent"
                    ],
                    "type": "string",
                    "default": "Independent"
                },
                "predictors": {
                    "type": "array",
                    "items": {
                        "oneOf": [
                            {
                                "$ref": "#/definitions/OrionIndependentPropertyPredictorConfiguration"
                            },
                            {
                                "$ref": "#/definitions/OrionRenamePropertyPredictorConfiguration"
                            },
                            {
                                "$ref": "#/definitions/OrionSetValuePredictorConfiguration"
                            },
                            {
                                "$ref": "#/definitions/OrionParaboloidPredictorConfiguration"
                            },
                            {
                                "$ref": "#/definitions/OrionLegacyPropertyPredictorConfiguration"
                            }
                        ]
                    }
                },
                "description": {
                    "type": "string"
                }
            },
            "definitions": {
                "orion_int_descriptor": {
                    "type": "object",
                    "title": "Integer",
                    "required": [
                        "type",
                        "lower_bound",
                        "upper_bound"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Integer"
                            ],
                            "type": "string",
                            "default": "Integer"
                        },
                        "units": {
                            "type": "string"
                        },
                        "lower_bound": {
                            "type": "integer"
                        },
                        "upper_bound": {
                            "type": "integer"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_real_descriptor": {
                    "type": "object",
                    "title": "Real",
                    "required": [
                        "type",
                        "lower_bound",
                        "upper_bound"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Real"
                            ],
                            "type": "string",
                            "default": "Real"
                        },
                        "units": {
                            "type": "string"
                        },
                        "lower_bound": {
                            "type": "number"
                        },
                        "upper_bound": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_metal_alloy_descriptor": {
                    "type": "object",
                    "title": "MetalAlloy",
                    "required": [
                        "type",
                        "threshold"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Metal Alloy"
                            ],
                            "type": "string",
                            "default": "Metal Alloy"
                        },
                        "threshold": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        },
                        "primary_elements": {
                            "type": "array",
                            "items": {
                                "enum": [
                                    "HYDROGEN",
                                    "DEUTERIUM",
                                    "TRITIUM",
                                    "HELIUM",
                                    "LITHIUM",
                                    "BERYLLIUM",
                                    "BORON",
                                    "CARBON",
                                    "NITROGEN",
                                    "OXYGEN",
                                    "FLUORINE",
                                    "NEON",
                                    "SODIUM",
                                    "MAGNESIUM",
                                    "ALUMINUM",
                                    "SILICON",
                                    "PHOSPHORUS",
                                    "SULFUR",
                                    "CHLORINE",
                                    "ARGON",
                                    "POTASSIUM",
                                    "CALCIUM",
                                    "SCANDIUM",
                                    "TITANIUM",
                                    "VANADIUM",
                                    "CHROMIUM",
                                    "MANGANESE",
                                    "IRON",
                                    "COBALT",
                                    "NICKEL",
                                    "COPPER",
                                    "ZINC",
                                    "GALLIUM",
                                    "GERMANIUM",
                                    "ARSENIC",
                                    "SELENIUM",
                                    "BROMINE",
                                    "KRYPTON",
                                    "RUBIDIUM",
                                    "STRONTIUM",
                                    "YTTRIUM",
                                    "ZIRCONIUM",
                                    "NIOBIUM",
                                    "MOLYBDENUM",
                                    "TECHNETIUM",
                                    "RUTHENIUM",
                                    "RHODIUM",
                                    "PALLADIUM",
                                    "SILVER",
                                    "CADMIUM",
                                    "INDIUM",
                                    "TIN",
                                    "ANTIMONY",
                                    "TELLURIUM",
                                    "IODINE",
                                    "XENON",
                                    "CESIUM",
                                    "BARIUM",
                                    "LANTHANUM",
                                    "CERIUM",
                                    "PRASEODYMIUM",
                                    "NEODYMIUM",
                                    "PROMETHIUM",
                                    "SAMARIUM",
                                    "EUROPIUM",
                                    "GADOLINIUM",
                                    "TERBIUM",
                                    "DYSPROSIUM",
                                    "HOLMIUM",
                                    "ERBIUM",
                                    "THULIUM",
                                    "YTTERBIUM",
                                    "LUTETIUM",
                                    "HAFNIUM",
                                    "TANTALUM",
                                    "TUNGSTEN",
                                    "RHENIUM",
                                    "OSMIUM",
                                    "IRIDIUM",
                                    "PLATINUM",
                                    "GOLD",
                                    "MERCURY",
                                    "THALLIUM",
                                    "LEAD",
                                    "BISMUTH",
                                    "POLONIUM",
                                    "ASTATINE",
                                    "RADON",
                                    "FRANCIUM",
                                    "RADIUM",
                                    "ACTINIUM",
                                    "THORIUM",
                                    "PROTACTINIUM",
                                    "URANIUM",
                                    "NEPTUNIUM",
                                    "PLUTONIUM",
                                    "AMERICIUM",
                                    "CURIUM",
                                    "BERKELIUM",
                                    "CALIFORNIUM",
                                    "EINSTEINIUM",
                                    "FERMIUM",
                                    "MENDELEVIUM",
                                    "NOBELIUM",
                                    "LAWRENCIUM",
                                    "RUTHERFORDIUM",
                                    "DUBNIUM",
                                    "SEABORGIUM",
                                    "BOHRIUM",
                                    "HASSIUM",
                                    "MEITNERIUM",
                                    "DARMSTADTIUM",
                                    "ROENTGENIUM",
                                    "COPERNICIUM",
                                    "FLEROVIUM",
                                    "LIVERMORIUM",
                                    "WILDCARD"
                                ],
                                "type": "string"
                            }
                        }
                    },
                    "additional_properties": False
                },
                "orion_real_vector_descriptor": {
                    "type": "object",
                    "title": "Vector",
                    "required": [
                        "type",
                        "descriptor_key",
                        "length"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Vector"
                            ],
                            "type": "string",
                            "default": "Vector"
                        },
                        "units": {
                            "type": "string"
                        },
                        "length": {
                            "type": "integer"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_categorical_descriptor": {
                    "type": "object",
                    "title": "Categorical",
                    "required": [
                        "type"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Categorical"
                            ],
                            "type": "string",
                            "default": "Categorical"
                        },
                        "descriptor_key": {
                            "type": "string"
                        },
                        "descriptor_values": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        }
                    },
                    "additional_properties": False
                },
                "orion_formulation_descriptor": {
                    "type": "object",
                    "title": "Formulation",
                    "required": [
                        "type"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Formulation"
                            ],
                            "type": "string",
                            "default": "Formulation"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_alloy_composition_descriptor": {
                    "type": "object",
                    "title": "AlloyComposition",
                    "required": [
                        "type",
                        "descriptor_key",
                        "balance_element",
                        "basis",
                        "threshold"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Alloy composition"
                            ],
                            "type": "string",
                            "default": "Alloy composition"
                        },
                        "basis": {
                            "type": "number"
                        },
                        "threshold": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        },
                        "balance_element": {
                            "enum": [
                                "HYDROGEN",
                                "DEUTERIUM",
                                "TRITIUM",
                                "HELIUM",
                                "LITHIUM",
                                "BERYLLIUM",
                                "BORON",
                                "CARBON",
                                "NITROGEN",
                                "OXYGEN",
                                "FLUORINE",
                                "NEON",
                                "SODIUM",
                                "MAGNESIUM",
                                "ALUMINUM",
                                "SILICON",
                                "PHOSPHORUS",
                                "SULFUR",
                                "CHLORINE",
                                "ARGON",
                                "POTASSIUM",
                                "CALCIUM",
                                "SCANDIUM",
                                "TITANIUM",
                                "VANADIUM",
                                "CHROMIUM",
                                "MANGANESE",
                                "IRON",
                                "COBALT",
                                "NICKEL",
                                "COPPER",
                                "ZINC",
                                "GALLIUM",
                                "GERMANIUM",
                                "ARSENIC",
                                "SELENIUM",
                                "BROMINE",
                                "KRYPTON",
                                "RUBIDIUM",
                                "STRONTIUM",
                                "YTTRIUM",
                                "ZIRCONIUM",
                                "NIOBIUM",
                                "MOLYBDENUM",
                                "TECHNETIUM",
                                "RUTHENIUM",
                                "RHODIUM",
                                "PALLADIUM",
                                "SILVER",
                                "CADMIUM",
                                "INDIUM",
                                "TIN",
                                "ANTIMONY",
                                "TELLURIUM",
                                "IODINE",
                                "XENON",
                                "CESIUM",
                                "BARIUM",
                                "LANTHANUM",
                                "CERIUM",
                                "PRASEODYMIUM",
                                "NEODYMIUM",
                                "PROMETHIUM",
                                "SAMARIUM",
                                "EUROPIUM",
                                "GADOLINIUM",
                                "TERBIUM",
                                "DYSPROSIUM",
                                "HOLMIUM",
                                "ERBIUM",
                                "THULIUM",
                                "YTTERBIUM",
                                "LUTETIUM",
                                "HAFNIUM",
                                "TANTALUM",
                                "TUNGSTEN",
                                "RHENIUM",
                                "OSMIUM",
                                "IRIDIUM",
                                "PLATINUM",
                                "GOLD",
                                "MERCURY",
                                "THALLIUM",
                                "LEAD",
                                "BISMUTH",
                                "POLONIUM",
                                "ASTATINE",
                                "RADON",
                                "FRANCIUM",
                                "RADIUM",
                                "ACTINIUM",
                                "THORIUM",
                                "PROTACTINIUM",
                                "URANIUM",
                                "NEPTUNIUM",
                                "PLUTONIUM",
                                "AMERICIUM",
                                "CURIUM",
                                "BERKELIUM",
                                "CALIFORNIUM",
                                "EINSTEINIUM",
                                "FERMIUM",
                                "MENDELEVIUM",
                                "NOBELIUM",
                                "LAWRENCIUM",
                                "RUTHERFORDIUM",
                                "DUBNIUM",
                                "SEABORGIUM",
                                "BOHRIUM",
                                "HASSIUM",
                                "MEITNERIUM",
                                "DARMSTADTIUM",
                                "ROENTGENIUM",
                                "COPERNICIUM",
                                "FLEROVIUM",
                                "LIVERMORIUM",
                                "WILDCARD"
                            ],
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_set_value_predictor_configuration": {
                    "type": "object",
                    "title": "SetValue",
                    "required": [
                        "type",
                        "name",
                        "description",
                        "descriptor",
                        "value"
                    ],
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "type": {
                            "enum": [
                                "SetValue"
                            ],
                            "type": "string",
                            "default": "SetValue"
                        },
                        "value": {
                            "type": "string"
                        },
                        "descriptor": {
                            "oneOf": [
                                {
                                    "$ref": "#/definitions/OrionCategoricalDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionOrganicChemicalFormulaDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionIntDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionRealDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionRealVectorDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionMetalAlloyDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionAlloyCompositionDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionInorganicChemicalFormulaDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionFormulationDescriptor"
                                }
                            ]
                        },
                        "description": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_organic_chemical_formula_descriptor": {
                    "type": "object",
                    "title": "Organic",
                    "required": [
                        "type",
                        "descriptor_key"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Organic"
                            ],
                            "type": "string",
                            "default": "Organic"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_paraboloid_predictor_configuration": {
                    "type": "object",
                    "title": "Paraboloid",
                    "required": [
                        "type",
                        "name",
                        "description",
                        "inputs",
                        "output"
                    ],
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "type": {
                            "enum": [
                                "Paraboloid"
                            ],
                            "type": "string",
                            "default": "Paraboloid"
                        },
                        "inputs": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/OrionRealDescriptor"
                            }
                        },
                        "output": {
                            "$ref": "#/definitions/OrionRealDescriptor"
                        },
                        "description": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_inorganic_chemical_formula_descriptor": {
                    "type": "object",
                    "title": "Inorganic",
                    "required": [
                        "type",
                        "threshold"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Inorganic"
                            ],
                            "type": "string",
                            "default": "Inorganic"
                        },
                        "threshold": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_legacy_property_predictor_configuration": {
                    "type": "object",
                    "title": "Legacy",
                    "required": [
                        "type",
                        "name",
                        "description",
                        "inputs",
                        "outputs",
                        "latent_variables",
                        "training_data"
                    ],
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "type": {
                            "enum": [
                                "Legacy"
                            ],
                            "type": "string",
                            "default": "Legacy"
                        },
                        "inputs": {
                            "type": "array",
                            "items": {
                                "oneOf": [
                                    {
                                        "$ref": "#/definitions/OrionCategoricalDescriptor"
                                    },
                                    {
                                        "$ref": "#/definitions/OrionOrganicChemicalFormulaDescriptor"
                                    },
                                    {
                                        "$ref": "#/definitions/OrionIntDescriptor"
                                    },
                                    {
                                        "$ref": "#/definitions/OrionRealDescriptor"
                                    },
                                    {
                                        "$ref": "#/definitions/OrionRealVectorDescriptor"
                                    },
                                    {
                                        "$ref": "#/definitions/OrionMetalAlloyDescriptor"
                                    },
                                    {
                                        "$ref": "#/definitions/OrionAlloyCompositionDescriptor"
                                    },
                                    {
                                        "$ref": "#/definitions/OrionInorganicChemicalFormulaDescriptor"
                                    },
                                    {
                                        "$ref": "#/definitions/OrionFormulationDescriptor"
                                    }
                                ]
                            }
                        },
                        "outputs": {
                            "type": "array",
                            "items": {
                                "oneOf": [
                                    {
                                        "$ref": "#/definitions/OrionCategoricalDescriptor"
                                    },
                                    {
                                        "$ref": "#/definitions/OrionOrganicChemicalFormulaDescriptor"
                                    },
                                    {
                                        "$ref": "#/definitions/OrionIntDescriptor"
                                    },
                                    {
                                        "$ref": "#/definitions/OrionRealDescriptor"
                                    },
                                    {
                                        "$ref": "#/definitions/OrionRealVectorDescriptor"
                                    },
                                    {
                                        "$ref": "#/definitions/OrionMetalAlloyDescriptor"
                                    },
                                    {
                                        "$ref": "#/definitions/OrionAlloyCompositionDescriptor"
                                    },
                                    {
                                        "$ref": "#/definitions/OrionInorganicChemicalFormulaDescriptor"
                                    },
                                    {
                                        "$ref": "#/definitions/OrionFormulationDescriptor"
                                    }
                                ]
                            }
                        },
                        "description": {
                            "type": "string"
                        },
                        "training_data": {
                            "type": "string"
                        },
                        "latent_variables": {
                            "type": "array",
                            "items": {
                                "oneOf": [
                                    {
                                        "$ref": "#/definitions/OrionCategoricalDescriptor"
                                    },
                                    {
                                        "$ref": "#/definitions/OrionOrganicChemicalFormulaDescriptor"
                                    },
                                    {
                                        "$ref": "#/definitions/OrionIntDescriptor"
                                    },
                                    {
                                        "$ref": "#/definitions/OrionRealDescriptor"
                                    },
                                    {
                                        "$ref": "#/definitions/OrionRealVectorDescriptor"
                                    },
                                    {
                                        "$ref": "#/definitions/OrionMetalAlloyDescriptor"
                                    },
                                    {
                                        "$ref": "#/definitions/OrionAlloyCompositionDescriptor"
                                    },
                                    {
                                        "$ref": "#/definitions/OrionInorganicChemicalFormulaDescriptor"
                                    },
                                    {
                                        "$ref": "#/definitions/OrionFormulationDescriptor"
                                    }
                                ]
                            }
                        }
                    },
                    "additional_properties": False
                },
                "orion_rename_property_predictor_configuration": {
                    "type": "object",
                    "title": "Rename",
                    "required": [
                        "type",
                        "name",
                        "description",
                        "source",
                        "dest"
                    ],
                    "properties": {
                        "dest": {
                            "oneOf": [
                                {
                                    "$ref": "#/definitions/OrionCategoricalDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionOrganicChemicalFormulaDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionIntDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionRealDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionRealVectorDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionMetalAlloyDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionAlloyCompositionDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionInorganicChemicalFormulaDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionFormulationDescriptor"
                                }
                            ]
                        },
                        "name": {
                            "type": "string"
                        },
                        "type": {
                            "enum": [
                                "Rename"
                            ],
                            "type": "string",
                            "default": "Rename"
                        },
                        "source": {
                            "oneOf": [
                                {
                                    "$ref": "#/definitions/OrionCategoricalDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionOrganicChemicalFormulaDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionIntDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionRealDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionRealVectorDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionMetalAlloyDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionAlloyCompositionDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionInorganicChemicalFormulaDescriptor"
                                },
                                {
                                    "$ref": "#/definitions/OrionFormulationDescriptor"
                                }
                            ]
                        },
                        "description": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_independent_property_predictor_configuration": {
                    "type": "object",
                    "title": "Independent",
                    "required": [
                        "type",
                        "name",
                        "description",
                        "predictors"
                    ],
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "type": {
                            "enum": [
                                "Independent"
                            ],
                            "type": "string",
                            "default": "Independent"
                        },
                        "predictors": {
                            "type": "array",
                            "items": {
                                "oneOf": [
                                    {
                                        "$ref": "#/definitions/OrionIndependentPropertyPredictorConfiguration"
                                    },
                                    {
                                        "$ref": "#/definitions/OrionRenamePropertyPredictorConfiguration"
                                    },
                                    {
                                        "$ref": "#/definitions/OrionSetValuePredictorConfiguration"
                                    },
                                    {
                                        "$ref": "#/definitions/OrionParaboloidPredictorConfiguration"
                                    },
                                    {
                                        "$ref": "#/definitions/OrionLegacyPropertyPredictorConfiguration"
                                    }
                                ]
                            }
                        },
                        "description": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                }
            },
            "additional_properties": False
        },
        "tags": []
    },
    {
        "id": "d4b644e1-a86c-438c-9d2f-8c93e1479f9f",
        "module_type": "SCORE",
        "display_name": "OrionMLIScore",
        "schema": {
            "type": "object",
            "title": "MLI",
            "schema": "http://json-schema.org/draft-04/schema#",
            "required": [
                "type",
                "name",
                "description",
                "objectives",
                "constraints",
                "baselines"
            ],
            "properties": {
                "name": {
                    "type": "string"
                },
                "type": {
                    "enum": [
                        "MLI"
                    ],
                    "type": "string",
                    "default": "MLI"
                },
                "baselines": {
                    "type": "array",
                    "items": {
                        "type": "number"
                    }
                },
                "objectives": {
                    "type": "array",
                    "items": {
                        "oneOf": [
                            {
                                "$ref": "#/definitions/OrionScalarMaxObjective"
                            },
                            {
                                "$ref": "#/definitions/OrionScalarMinObjective"
                            },
                            {
                                "$ref": "#/definitions/OrionScalarTuneObjective"
                            }
                        ]
                    }
                },
                "constraints": {
                    "type": "array",
                    "items": {
                        "oneOf": [
                            {
                                "$ref": "#/definitions/OrionRealRangeConstraint"
                            },
                            {
                                "$ref": "#/definitions/OrionElementalConstraint"
                            },
                            {
                                "$ref": "#/definitions/OrionClassMembershipConstraint"
                            },
                            {
                                "$ref": "#/definitions/OrionCompositionRangeConstraint"
                            }
                        ]
                    }
                },
                "description": {
                    "type": "string"
                }
            },
            "definitions": {
                "orion_scalar_max_objective": {
                    "type": "object",
                    "title": "ScalarMax",
                    "required": [
                        "type",
                        "descriptor_key",
                        "lower_bound",
                        "upper_bound"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "ScalarMax"
                            ],
                            "type": "string",
                            "default": "ScalarMax"
                        },
                        "lower_bound": {
                            "type": "number"
                        },
                        "upper_bound": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_scalar_min_objective": {
                    "type": "object",
                    "title": "ScalarMin",
                    "required": [
                        "type",
                        "descriptor_key",
                        "lower_bound",
                        "upper_bound"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "ScalarMin"
                            ],
                            "type": "string",
                            "default": "ScalarMin"
                        },
                        "lower_bound": {
                            "type": "number"
                        },
                        "upper_bound": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_elemental_constraint": {
                    "type": "object",
                    "title": "Elemental",
                    "required": [
                        "type",
                        "descriptor_key",
                        "required_elements",
                        "restricted_elements"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Elemental"
                            ],
                            "type": "string",
                            "default": "Elemental"
                        },
                        "descriptor_key": {
                            "type": "string",
                            "description": "Descriptor key"
                        },
                        "required_elements": {
                            "type": "array",
                            "items": {
                                "enum": [
                                    "HYDROGEN",
                                    "DEUTERIUM",
                                    "TRITIUM",
                                    "HELIUM",
                                    "LITHIUM",
                                    "BERYLLIUM",
                                    "BORON",
                                    "CARBON",
                                    "NITROGEN",
                                    "OXYGEN",
                                    "FLUORINE",
                                    "NEON",
                                    "SODIUM",
                                    "MAGNESIUM",
                                    "ALUMINUM",
                                    "SILICON",
                                    "PHOSPHORUS",
                                    "SULFUR",
                                    "CHLORINE",
                                    "ARGON",
                                    "POTASSIUM",
                                    "CALCIUM",
                                    "SCANDIUM",
                                    "TITANIUM",
                                    "VANADIUM",
                                    "CHROMIUM",
                                    "MANGANESE",
                                    "IRON",
                                    "COBALT",
                                    "NICKEL",
                                    "COPPER",
                                    "ZINC",
                                    "GALLIUM",
                                    "GERMANIUM",
                                    "ARSENIC",
                                    "SELENIUM",
                                    "BROMINE",
                                    "KRYPTON",
                                    "RUBIDIUM",
                                    "STRONTIUM",
                                    "YTTRIUM",
                                    "ZIRCONIUM",
                                    "NIOBIUM",
                                    "MOLYBDENUM",
                                    "TECHNETIUM",
                                    "RUTHENIUM",
                                    "RHODIUM",
                                    "PALLADIUM",
                                    "SILVER",
                                    "CADMIUM",
                                    "INDIUM",
                                    "TIN",
                                    "ANTIMONY",
                                    "TELLURIUM",
                                    "IODINE",
                                    "XENON",
                                    "CESIUM",
                                    "BARIUM",
                                    "LANTHANUM",
                                    "CERIUM",
                                    "PRASEODYMIUM",
                                    "NEODYMIUM",
                                    "PROMETHIUM",
                                    "SAMARIUM",
                                    "EUROPIUM",
                                    "GADOLINIUM",
                                    "TERBIUM",
                                    "DYSPROSIUM",
                                    "HOLMIUM",
                                    "ERBIUM",
                                    "THULIUM",
                                    "YTTERBIUM",
                                    "LUTETIUM",
                                    "HAFNIUM",
                                    "TANTALUM",
                                    "TUNGSTEN",
                                    "RHENIUM",
                                    "OSMIUM",
                                    "IRIDIUM",
                                    "PLATINUM",
                                    "GOLD",
                                    "MERCURY",
                                    "THALLIUM",
                                    "LEAD",
                                    "BISMUTH",
                                    "POLONIUM",
                                    "ASTATINE",
                                    "RADON",
                                    "FRANCIUM",
                                    "RADIUM",
                                    "ACTINIUM",
                                    "THORIUM",
                                    "PROTACTINIUM",
                                    "URANIUM",
                                    "NEPTUNIUM",
                                    "PLUTONIUM",
                                    "AMERICIUM",
                                    "CURIUM",
                                    "BERKELIUM",
                                    "CALIFORNIUM",
                                    "EINSTEINIUM",
                                    "FERMIUM",
                                    "MENDELEVIUM",
                                    "NOBELIUM",
                                    "LAWRENCIUM",
                                    "RUTHERFORDIUM",
                                    "DUBNIUM",
                                    "SEABORGIUM",
                                    "BOHRIUM",
                                    "HASSIUM",
                                    "MEITNERIUM",
                                    "DARMSTADTIUM",
                                    "ROENTGENIUM",
                                    "COPERNICIUM",
                                    "FLEROVIUM",
                                    "LIVERMORIUM",
                                    "WILDCARD"
                                ],
                                "type": "string"
                            }
                        },
                        "restricted_elements": {
                            "type": "array",
                            "items": {
                                "enum": [
                                    "HYDROGEN",
                                    "DEUTERIUM",
                                    "TRITIUM",
                                    "HELIUM",
                                    "LITHIUM",
                                    "BERYLLIUM",
                                    "BORON",
                                    "CARBON",
                                    "NITROGEN",
                                    "OXYGEN",
                                    "FLUORINE",
                                    "NEON",
                                    "SODIUM",
                                    "MAGNESIUM",
                                    "ALUMINUM",
                                    "SILICON",
                                    "PHOSPHORUS",
                                    "SULFUR",
                                    "CHLORINE",
                                    "ARGON",
                                    "POTASSIUM",
                                    "CALCIUM",
                                    "SCANDIUM",
                                    "TITANIUM",
                                    "VANADIUM",
                                    "CHROMIUM",
                                    "MANGANESE",
                                    "IRON",
                                    "COBALT",
                                    "NICKEL",
                                    "COPPER",
                                    "ZINC",
                                    "GALLIUM",
                                    "GERMANIUM",
                                    "ARSENIC",
                                    "SELENIUM",
                                    "BROMINE",
                                    "KRYPTON",
                                    "RUBIDIUM",
                                    "STRONTIUM",
                                    "YTTRIUM",
                                    "ZIRCONIUM",
                                    "NIOBIUM",
                                    "MOLYBDENUM",
                                    "TECHNETIUM",
                                    "RUTHENIUM",
                                    "RHODIUM",
                                    "PALLADIUM",
                                    "SILVER",
                                    "CADMIUM",
                                    "INDIUM",
                                    "TIN",
                                    "ANTIMONY",
                                    "TELLURIUM",
                                    "IODINE",
                                    "XENON",
                                    "CESIUM",
                                    "BARIUM",
                                    "LANTHANUM",
                                    "CERIUM",
                                    "PRASEODYMIUM",
                                    "NEODYMIUM",
                                    "PROMETHIUM",
                                    "SAMARIUM",
                                    "EUROPIUM",
                                    "GADOLINIUM",
                                    "TERBIUM",
                                    "DYSPROSIUM",
                                    "HOLMIUM",
                                    "ERBIUM",
                                    "THULIUM",
                                    "YTTERBIUM",
                                    "LUTETIUM",
                                    "HAFNIUM",
                                    "TANTALUM",
                                    "TUNGSTEN",
                                    "RHENIUM",
                                    "OSMIUM",
                                    "IRIDIUM",
                                    "PLATINUM",
                                    "GOLD",
                                    "MERCURY",
                                    "THALLIUM",
                                    "LEAD",
                                    "BISMUTH",
                                    "POLONIUM",
                                    "ASTATINE",
                                    "RADON",
                                    "FRANCIUM",
                                    "RADIUM",
                                    "ACTINIUM",
                                    "THORIUM",
                                    "PROTACTINIUM",
                                    "URANIUM",
                                    "NEPTUNIUM",
                                    "PLUTONIUM",
                                    "AMERICIUM",
                                    "CURIUM",
                                    "BERKELIUM",
                                    "CALIFORNIUM",
                                    "EINSTEINIUM",
                                    "FERMIUM",
                                    "MENDELEVIUM",
                                    "NOBELIUM",
                                    "LAWRENCIUM",
                                    "RUTHERFORDIUM",
                                    "DUBNIUM",
                                    "SEABORGIUM",
                                    "BOHRIUM",
                                    "HASSIUM",
                                    "MEITNERIUM",
                                    "DARMSTADTIUM",
                                    "ROENTGENIUM",
                                    "COPERNICIUM",
                                    "FLEROVIUM",
                                    "LIVERMORIUM",
                                    "WILDCARD"
                                ],
                                "type": "string"
                            }
                        }
                    },
                    "additional_properties": False
                },
                "orion_real_range_constraint": {
                    "type": "object",
                    "title": "ScalarRange",
                    "required": [
                        "type",
                        "descriptor_key"
                    ],
                    "properties": {
                        "max": {
                            "type": "number"
                        },
                        "min": {
                            "type": "number"
                        },
                        "type": {
                            "enum": [
                                "ScalarRange"
                            ],
                            "type": "string",
                            "default": "ScalarRange"
                        },
                        "max_inclusive": {
                            "type": "boolean"
                        },
                        "min_inclusive": {
                            "type": "boolean"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_scalar_tune_objective": {
                    "type": "object",
                    "title": "TargetValue",
                    "required": [
                        "type",
                        "descriptor_key",
                        "target",
                        "power"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "TargetValue"
                            ],
                            "type": "string",
                            "default": "TargetValue"
                        },
                        "power": {
                            "type": "number"
                        },
                        "target": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_class_membership_constraint": {
                    "type": "object",
                    "title": "ClassMembership",
                    "required": [
                        "type",
                        "descriptor_key",
                        "acceptable_classes"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Categorical"
                            ],
                            "type": "string",
                            "default": "Categorical"
                        },
                        "descriptor_key": {
                            "type": "string"
                        },
                        "acceptable_classes": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        }
                    },
                    "additional_properties": False
                },
                "orion_composition_range_constraint": {
                    "type": "object",
                    "title": "CompositionRange",
                    "required": [
                        "type",
                        "descriptor_key",
                        "element"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "CompositionRange"
                            ],
                            "type": "string",
                            "default": "CompositionRange"
                        },
                        "basis": {
                            "type": "number"
                        },
                        "element": {
                            "enum": [
                                "HYDROGEN",
                                "DEUTERIUM",
                                "TRITIUM",
                                "HELIUM",
                                "LITHIUM",
                                "BERYLLIUM",
                                "BORON",
                                "CARBON",
                                "NITROGEN",
                                "OXYGEN",
                                "FLUORINE",
                                "NEON",
                                "SODIUM",
                                "MAGNESIUM",
                                "ALUMINUM",
                                "SILICON",
                                "PHOSPHORUS",
                                "SULFUR",
                                "CHLORINE",
                                "ARGON",
                                "POTASSIUM",
                                "CALCIUM",
                                "SCANDIUM",
                                "TITANIUM",
                                "VANADIUM",
                                "CHROMIUM",
                                "MANGANESE",
                                "IRON",
                                "COBALT",
                                "NICKEL",
                                "COPPER",
                                "ZINC",
                                "GALLIUM",
                                "GERMANIUM",
                                "ARSENIC",
                                "SELENIUM",
                                "BROMINE",
                                "KRYPTON",
                                "RUBIDIUM",
                                "STRONTIUM",
                                "YTTRIUM",
                                "ZIRCONIUM",
                                "NIOBIUM",
                                "MOLYBDENUM",
                                "TECHNETIUM",
                                "RUTHENIUM",
                                "RHODIUM",
                                "PALLADIUM",
                                "SILVER",
                                "CADMIUM",
                                "INDIUM",
                                "TIN",
                                "ANTIMONY",
                                "TELLURIUM",
                                "IODINE",
                                "XENON",
                                "CESIUM",
                                "BARIUM",
                                "LANTHANUM",
                                "CERIUM",
                                "PRASEODYMIUM",
                                "NEODYMIUM",
                                "PROMETHIUM",
                                "SAMARIUM",
                                "EUROPIUM",
                                "GADOLINIUM",
                                "TERBIUM",
                                "DYSPROSIUM",
                                "HOLMIUM",
                                "ERBIUM",
                                "THULIUM",
                                "YTTERBIUM",
                                "LUTETIUM",
                                "HAFNIUM",
                                "TANTALUM",
                                "TUNGSTEN",
                                "RHENIUM",
                                "OSMIUM",
                                "IRIDIUM",
                                "PLATINUM",
                                "GOLD",
                                "MERCURY",
                                "THALLIUM",
                                "LEAD",
                                "BISMUTH",
                                "POLONIUM",
                                "ASTATINE",
                                "RADON",
                                "FRANCIUM",
                                "RADIUM",
                                "ACTINIUM",
                                "THORIUM",
                                "PROTACTINIUM",
                                "URANIUM",
                                "NEPTUNIUM",
                                "PLUTONIUM",
                                "AMERICIUM",
                                "CURIUM",
                                "BERKELIUM",
                                "CALIFORNIUM",
                                "EINSTEINIUM",
                                "FERMIUM",
                                "MENDELEVIUM",
                                "NOBELIUM",
                                "LAWRENCIUM",
                                "RUTHERFORDIUM",
                                "DUBNIUM",
                                "SEABORGIUM",
                                "BOHRIUM",
                                "HASSIUM",
                                "MEITNERIUM",
                                "DARMSTADTIUM",
                                "ROENTGENIUM",
                                "COPERNICIUM",
                                "FLEROVIUM",
                                "LIVERMORIUM",
                                "WILDCARD"
                            ],
                            "type": "string"
                        },
                        "max_frac": {
                            "type": "number"
                        },
                        "min_frac": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        },
                        "el_is_required": {
                            "type": "boolean"
                        }
                    },
                    "additional_properties": False
                }
            },
            "additional_properties": False
        },
        "tags": []
    },
    {
        "id": "d8ddfe73-10f7-4456-9de9-9a1638bae403",
        "module_type": "PROCESSOR",
        "display_name": "OrionContinuousSearchProcessor",
        "schema": {
            "type": "object",
            "title": "ContinuousSearch",
            "schema": "http://json-schema.org/draft-04/schema#",
            "required": [
                "type",
                "name",
                "description"
            ],
            "properties": {
                "name": {
                    "type": "string"
                },
                "type": {
                    "enum": [
                        "ContinuousSearch"
                    ],
                    "type": "string",
                    "default": "ContinuousSearch"
                },
                "description": {
                    "type": "string"
                }
            },
            "additional_properties": False
        },
        "tags": []
    },
    {
        "id": "272791a5-5468-4344-ac9f-2811d9266a4d",
        "module_type": "PROCESSOR",
        "display_name": "OrionGridProcessor",
        "schema": {
            "type": "object",
            "title": "Grid",
            "schema": "http://json-schema.org/draft-04/schema#",
            "required": [
                "type",
                "name",
                "description",
                "grid_dimensions"
            ],
            "properties": {
                "name": {
                    "type": "string"
                },
                "type": {
                    "enum": [
                        "Grid"
                    ],
                    "type": "string",
                    "default": "Grid"
                },
                "description": {
                    "type": "string"
                },
                "grid_dimensions": {
                    "type": "object"
                }
            },
            "additional_properties": False
        },
        "tags": []
    },
    {
        "id": "c1940483-d034-4782-9c90-aee38dacc6d1",
        "module_type": "PREDICTOR",
        "display_name": "OrionRenamePropertyPredictorConfiguration",
        "schema": {
            "type": "object",
            "title": "Rename",
            "schema": "http://json-schema.org/draft-04/schema#",
            "required": [
                "type",
                "name",
                "description",
                "source",
                "dest"
            ],
            "properties": {
                "dest": {
                    "oneOf": [
                        {
                            "$ref": "#/definitions/OrionCategoricalDescriptor"
                        },
                        {
                            "$ref": "#/definitions/OrionOrganicChemicalFormulaDescriptor"
                        },
                        {
                            "$ref": "#/definitions/OrionIntDescriptor"
                        },
                        {
                            "$ref": "#/definitions/OrionRealDescriptor"
                        },
                        {
                            "$ref": "#/definitions/OrionRealVectorDescriptor"
                        },
                        {
                            "$ref": "#/definitions/OrionMetalAlloyDescriptor"
                        },
                        {
                            "$ref": "#/definitions/OrionAlloyCompositionDescriptor"
                        },
                        {
                            "$ref": "#/definitions/OrionInorganicChemicalFormulaDescriptor"
                        },
                        {
                            "$ref": "#/definitions/OrionFormulationDescriptor"
                        }
                    ]
                },
                "name": {
                    "type": "string"
                },
                "type": {
                    "enum": [
                        "Rename"
                    ],
                    "type": "string",
                    "default": "Rename"
                },
                "source": {
                    "oneOf": [
                        {
                            "$ref": "#/definitions/OrionCategoricalDescriptor"
                        },
                        {
                            "$ref": "#/definitions/OrionOrganicChemicalFormulaDescriptor"
                        },
                        {
                            "$ref": "#/definitions/OrionIntDescriptor"
                        },
                        {
                            "$ref": "#/definitions/OrionRealDescriptor"
                        },
                        {
                            "$ref": "#/definitions/OrionRealVectorDescriptor"
                        },
                        {
                            "$ref": "#/definitions/OrionMetalAlloyDescriptor"
                        },
                        {
                            "$ref": "#/definitions/OrionAlloyCompositionDescriptor"
                        },
                        {
                            "$ref": "#/definitions/OrionInorganicChemicalFormulaDescriptor"
                        },
                        {
                            "$ref": "#/definitions/OrionFormulationDescriptor"
                        }
                    ]
                },
                "description": {
                    "type": "string"
                }
            },
            "definitions": {
                "orion_int_descriptor": {
                    "type": "object",
                    "title": "Integer",
                    "required": [
                        "type",
                        "lower_bound",
                        "upper_bound"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Integer"
                            ],
                            "type": "string",
                            "default": "Integer"
                        },
                        "units": {
                            "type": "string"
                        },
                        "lower_bound": {
                            "type": "integer"
                        },
                        "upper_bound": {
                            "type": "integer"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_real_descriptor": {
                    "type": "object",
                    "title": "Real",
                    "required": [
                        "type",
                        "lower_bound",
                        "upper_bound"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Real"
                            ],
                            "type": "string",
                            "default": "Real"
                        },
                        "units": {
                            "type": "string"
                        },
                        "lower_bound": {
                            "type": "number"
                        },
                        "upper_bound": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_metal_alloy_descriptor": {
                    "type": "object",
                    "title": "MetalAlloy",
                    "required": [
                        "type",
                        "threshold"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Metal Alloy"
                            ],
                            "type": "string",
                            "default": "Metal Alloy"
                        },
                        "threshold": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        },
                        "primary_elements": {
                            "type": "array",
                            "items": {
                                "enum": [
                                    "HYDROGEN",
                                    "DEUTERIUM",
                                    "TRITIUM",
                                    "HELIUM",
                                    "LITHIUM",
                                    "BERYLLIUM",
                                    "BORON",
                                    "CARBON",
                                    "NITROGEN",
                                    "OXYGEN",
                                    "FLUORINE",
                                    "NEON",
                                    "SODIUM",
                                    "MAGNESIUM",
                                    "ALUMINUM",
                                    "SILICON",
                                    "PHOSPHORUS",
                                    "SULFUR",
                                    "CHLORINE",
                                    "ARGON",
                                    "POTASSIUM",
                                    "CALCIUM",
                                    "SCANDIUM",
                                    "TITANIUM",
                                    "VANADIUM",
                                    "CHROMIUM",
                                    "MANGANESE",
                                    "IRON",
                                    "COBALT",
                                    "NICKEL",
                                    "COPPER",
                                    "ZINC",
                                    "GALLIUM",
                                    "GERMANIUM",
                                    "ARSENIC",
                                    "SELENIUM",
                                    "BROMINE",
                                    "KRYPTON",
                                    "RUBIDIUM",
                                    "STRONTIUM",
                                    "YTTRIUM",
                                    "ZIRCONIUM",
                                    "NIOBIUM",
                                    "MOLYBDENUM",
                                    "TECHNETIUM",
                                    "RUTHENIUM",
                                    "RHODIUM",
                                    "PALLADIUM",
                                    "SILVER",
                                    "CADMIUM",
                                    "INDIUM",
                                    "TIN",
                                    "ANTIMONY",
                                    "TELLURIUM",
                                    "IODINE",
                                    "XENON",
                                    "CESIUM",
                                    "BARIUM",
                                    "LANTHANUM",
                                    "CERIUM",
                                    "PRASEODYMIUM",
                                    "NEODYMIUM",
                                    "PROMETHIUM",
                                    "SAMARIUM",
                                    "EUROPIUM",
                                    "GADOLINIUM",
                                    "TERBIUM",
                                    "DYSPROSIUM",
                                    "HOLMIUM",
                                    "ERBIUM",
                                    "THULIUM",
                                    "YTTERBIUM",
                                    "LUTETIUM",
                                    "HAFNIUM",
                                    "TANTALUM",
                                    "TUNGSTEN",
                                    "RHENIUM",
                                    "OSMIUM",
                                    "IRIDIUM",
                                    "PLATINUM",
                                    "GOLD",
                                    "MERCURY",
                                    "THALLIUM",
                                    "LEAD",
                                    "BISMUTH",
                                    "POLONIUM",
                                    "ASTATINE",
                                    "RADON",
                                    "FRANCIUM",
                                    "RADIUM",
                                    "ACTINIUM",
                                    "THORIUM",
                                    "PROTACTINIUM",
                                    "URANIUM",
                                    "NEPTUNIUM",
                                    "PLUTONIUM",
                                    "AMERICIUM",
                                    "CURIUM",
                                    "BERKELIUM",
                                    "CALIFORNIUM",
                                    "EINSTEINIUM",
                                    "FERMIUM",
                                    "MENDELEVIUM",
                                    "NOBELIUM",
                                    "LAWRENCIUM",
                                    "RUTHERFORDIUM",
                                    "DUBNIUM",
                                    "SEABORGIUM",
                                    "BOHRIUM",
                                    "HASSIUM",
                                    "MEITNERIUM",
                                    "DARMSTADTIUM",
                                    "ROENTGENIUM",
                                    "COPERNICIUM",
                                    "FLEROVIUM",
                                    "LIVERMORIUM",
                                    "WILDCARD"
                                ],
                                "type": "string"
                            }
                        }
                    },
                    "additional_properties": False
                },
                "orion_real_vector_descriptor": {
                    "type": "object",
                    "title": "Vector",
                    "required": [
                        "type",
                        "descriptor_key",
                        "length"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Vector"
                            ],
                            "type": "string",
                            "default": "Vector"
                        },
                        "units": {
                            "type": "string"
                        },
                        "length": {
                            "type": "integer"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_categorical_descriptor": {
                    "type": "object",
                    "title": "Categorical",
                    "required": [
                        "type"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Categorical"
                            ],
                            "type": "string",
                            "default": "Categorical"
                        },
                        "descriptor_key": {
                            "type": "string"
                        },
                        "descriptor_values": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        }
                    },
                    "additional_properties": False
                },
                "orion_formulation_descriptor": {
                    "type": "object",
                    "title": "Formulation",
                    "required": [
                        "type"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Formulation"
                            ],
                            "type": "string",
                            "default": "Formulation"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_alloy_composition_descriptor": {
                    "type": "object",
                    "title": "AlloyComposition",
                    "required": [
                        "type",
                        "descriptor_key",
                        "balance_element",
                        "basis",
                        "threshold"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Alloy composition"
                            ],
                            "type": "string",
                            "default": "Alloy composition"
                        },
                        "basis": {
                            "type": "number"
                        },
                        "threshold": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        },
                        "balance_element": {
                            "enum": [
                                "HYDROGEN",
                                "DEUTERIUM",
                                "TRITIUM",
                                "HELIUM",
                                "LITHIUM",
                                "BERYLLIUM",
                                "BORON",
                                "CARBON",
                                "NITROGEN",
                                "OXYGEN",
                                "FLUORINE",
                                "NEON",
                                "SODIUM",
                                "MAGNESIUM",
                                "ALUMINUM",
                                "SILICON",
                                "PHOSPHORUS",
                                "SULFUR",
                                "CHLORINE",
                                "ARGON",
                                "POTASSIUM",
                                "CALCIUM",
                                "SCANDIUM",
                                "TITANIUM",
                                "VANADIUM",
                                "CHROMIUM",
                                "MANGANESE",
                                "IRON",
                                "COBALT",
                                "NICKEL",
                                "COPPER",
                                "ZINC",
                                "GALLIUM",
                                "GERMANIUM",
                                "ARSENIC",
                                "SELENIUM",
                                "BROMINE",
                                "KRYPTON",
                                "RUBIDIUM",
                                "STRONTIUM",
                                "YTTRIUM",
                                "ZIRCONIUM",
                                "NIOBIUM",
                                "MOLYBDENUM",
                                "TECHNETIUM",
                                "RUTHENIUM",
                                "RHODIUM",
                                "PALLADIUM",
                                "SILVER",
                                "CADMIUM",
                                "INDIUM",
                                "TIN",
                                "ANTIMONY",
                                "TELLURIUM",
                                "IODINE",
                                "XENON",
                                "CESIUM",
                                "BARIUM",
                                "LANTHANUM",
                                "CERIUM",
                                "PRASEODYMIUM",
                                "NEODYMIUM",
                                "PROMETHIUM",
                                "SAMARIUM",
                                "EUROPIUM",
                                "GADOLINIUM",
                                "TERBIUM",
                                "DYSPROSIUM",
                                "HOLMIUM",
                                "ERBIUM",
                                "THULIUM",
                                "YTTERBIUM",
                                "LUTETIUM",
                                "HAFNIUM",
                                "TANTALUM",
                                "TUNGSTEN",
                                "RHENIUM",
                                "OSMIUM",
                                "IRIDIUM",
                                "PLATINUM",
                                "GOLD",
                                "MERCURY",
                                "THALLIUM",
                                "LEAD",
                                "BISMUTH",
                                "POLONIUM",
                                "ASTATINE",
                                "RADON",
                                "FRANCIUM",
                                "RADIUM",
                                "ACTINIUM",
                                "THORIUM",
                                "PROTACTINIUM",
                                "URANIUM",
                                "NEPTUNIUM",
                                "PLUTONIUM",
                                "AMERICIUM",
                                "CURIUM",
                                "BERKELIUM",
                                "CALIFORNIUM",
                                "EINSTEINIUM",
                                "FERMIUM",
                                "MENDELEVIUM",
                                "NOBELIUM",
                                "LAWRENCIUM",
                                "RUTHERFORDIUM",
                                "DUBNIUM",
                                "SEABORGIUM",
                                "BOHRIUM",
                                "HASSIUM",
                                "MEITNERIUM",
                                "DARMSTADTIUM",
                                "ROENTGENIUM",
                                "COPERNICIUM",
                                "FLEROVIUM",
                                "LIVERMORIUM",
                                "WILDCARD"
                            ],
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_organic_chemical_formula_descriptor": {
                    "type": "object",
                    "title": "Organic",
                    "required": [
                        "type",
                        "descriptor_key"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Organic"
                            ],
                            "type": "string",
                            "default": "Organic"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_inorganic_chemical_formula_descriptor": {
                    "type": "object",
                    "title": "Inorganic",
                    "required": [
                        "type",
                        "threshold"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Inorganic"
                            ],
                            "type": "string",
                            "default": "Inorganic"
                        },
                        "threshold": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                }
            },
            "additional_properties": False
        },
        "tags": []
    },
    {
        "id": "c1c51fb4-3819-460e-b959-6d51d5be034f",
        "module_type": "PREDICTOR",
        "display_name": "OrionSetValuePredictorConfiguration",
        "schema": {
            "type": "object",
            "title": "SetValue",
            "schema": "http://json-schema.org/draft-04/schema#",
            "required": [
                "type",
                "name",
                "description",
                "descriptor",
                "value"
            ],
            "properties": {
                "name": {
                    "type": "string"
                },
                "type": {
                    "enum": [
                        "SetValue"
                    ],
                    "type": "string",
                    "default": "SetValue"
                },
                "value": {
                    "type": "string"
                },
                "descriptor": {
                    "oneOf": [
                        {
                            "$ref": "#/definitions/OrionCategoricalDescriptor"
                        },
                        {
                            "$ref": "#/definitions/OrionOrganicChemicalFormulaDescriptor"
                        },
                        {
                            "$ref": "#/definitions/OrionIntDescriptor"
                        },
                        {
                            "$ref": "#/definitions/OrionRealDescriptor"
                        },
                        {
                            "$ref": "#/definitions/OrionRealVectorDescriptor"
                        },
                        {
                            "$ref": "#/definitions/OrionMetalAlloyDescriptor"
                        },
                        {
                            "$ref": "#/definitions/OrionAlloyCompositionDescriptor"
                        },
                        {
                            "$ref": "#/definitions/OrionInorganicChemicalFormulaDescriptor"
                        },
                        {
                            "$ref": "#/definitions/OrionFormulationDescriptor"
                        }
                    ]
                },
                "description": {
                    "type": "string"
                }
            },
            "definitions": {
                "orion_int_descriptor": {
                    "type": "object",
                    "title": "Integer",
                    "required": [
                        "type",
                        "lower_bound",
                        "upper_bound"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Integer"
                            ],
                            "type": "string",
                            "default": "Integer"
                        },
                        "units": {
                            "type": "string"
                        },
                        "lower_bound": {
                            "type": "integer"
                        },
                        "upper_bound": {
                            "type": "integer"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_real_descriptor": {
                    "type": "object",
                    "title": "Real",
                    "required": [
                        "type",
                        "lower_bound",
                        "upper_bound"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Real"
                            ],
                            "type": "string",
                            "default": "Real"
                        },
                        "units": {
                            "type": "string"
                        },
                        "lower_bound": {
                            "type": "number"
                        },
                        "upper_bound": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_metal_alloy_descriptor": {
                    "type": "object",
                    "title": "MetalAlloy",
                    "required": [
                        "type",
                        "threshold"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Metal Alloy"
                            ],
                            "type": "string",
                            "default": "Metal Alloy"
                        },
                        "threshold": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        },
                        "primary_elements": {
                            "type": "array",
                            "items": {
                                "enum": [
                                    "HYDROGEN",
                                    "DEUTERIUM",
                                    "TRITIUM",
                                    "HELIUM",
                                    "LITHIUM",
                                    "BERYLLIUM",
                                    "BORON",
                                    "CARBON",
                                    "NITROGEN",
                                    "OXYGEN",
                                    "FLUORINE",
                                    "NEON",
                                    "SODIUM",
                                    "MAGNESIUM",
                                    "ALUMINUM",
                                    "SILICON",
                                    "PHOSPHORUS",
                                    "SULFUR",
                                    "CHLORINE",
                                    "ARGON",
                                    "POTASSIUM",
                                    "CALCIUM",
                                    "SCANDIUM",
                                    "TITANIUM",
                                    "VANADIUM",
                                    "CHROMIUM",
                                    "MANGANESE",
                                    "IRON",
                                    "COBALT",
                                    "NICKEL",
                                    "COPPER",
                                    "ZINC",
                                    "GALLIUM",
                                    "GERMANIUM",
                                    "ARSENIC",
                                    "SELENIUM",
                                    "BROMINE",
                                    "KRYPTON",
                                    "RUBIDIUM",
                                    "STRONTIUM",
                                    "YTTRIUM",
                                    "ZIRCONIUM",
                                    "NIOBIUM",
                                    "MOLYBDENUM",
                                    "TECHNETIUM",
                                    "RUTHENIUM",
                                    "RHODIUM",
                                    "PALLADIUM",
                                    "SILVER",
                                    "CADMIUM",
                                    "INDIUM",
                                    "TIN",
                                    "ANTIMONY",
                                    "TELLURIUM",
                                    "IODINE",
                                    "XENON",
                                    "CESIUM",
                                    "BARIUM",
                                    "LANTHANUM",
                                    "CERIUM",
                                    "PRASEODYMIUM",
                                    "NEODYMIUM",
                                    "PROMETHIUM",
                                    "SAMARIUM",
                                    "EUROPIUM",
                                    "GADOLINIUM",
                                    "TERBIUM",
                                    "DYSPROSIUM",
                                    "HOLMIUM",
                                    "ERBIUM",
                                    "THULIUM",
                                    "YTTERBIUM",
                                    "LUTETIUM",
                                    "HAFNIUM",
                                    "TANTALUM",
                                    "TUNGSTEN",
                                    "RHENIUM",
                                    "OSMIUM",
                                    "IRIDIUM",
                                    "PLATINUM",
                                    "GOLD",
                                    "MERCURY",
                                    "THALLIUM",
                                    "LEAD",
                                    "BISMUTH",
                                    "POLONIUM",
                                    "ASTATINE",
                                    "RADON",
                                    "FRANCIUM",
                                    "RADIUM",
                                    "ACTINIUM",
                                    "THORIUM",
                                    "PROTACTINIUM",
                                    "URANIUM",
                                    "NEPTUNIUM",
                                    "PLUTONIUM",
                                    "AMERICIUM",
                                    "CURIUM",
                                    "BERKELIUM",
                                    "CALIFORNIUM",
                                    "EINSTEINIUM",
                                    "FERMIUM",
                                    "MENDELEVIUM",
                                    "NOBELIUM",
                                    "LAWRENCIUM",
                                    "RUTHERFORDIUM",
                                    "DUBNIUM",
                                    "SEABORGIUM",
                                    "BOHRIUM",
                                    "HASSIUM",
                                    "MEITNERIUM",
                                    "DARMSTADTIUM",
                                    "ROENTGENIUM",
                                    "COPERNICIUM",
                                    "FLEROVIUM",
                                    "LIVERMORIUM",
                                    "WILDCARD"
                                ],
                                "type": "string"
                            }
                        }
                    },
                    "additional_properties": False
                },
                "orion_real_vector_descriptor": {
                    "type": "object",
                    "title": "Vector",
                    "required": [
                        "type",
                        "descriptor_key",
                        "length"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Vector"
                            ],
                            "type": "string",
                            "default": "Vector"
                        },
                        "units": {
                            "type": "string"
                        },
                        "length": {
                            "type": "integer"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_categorical_descriptor": {
                    "type": "object",
                    "title": "Categorical",
                    "required": [
                        "type"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Categorical"
                            ],
                            "type": "string",
                            "default": "Categorical"
                        },
                        "descriptor_key": {
                            "type": "string"
                        },
                        "descriptor_values": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        }
                    },
                    "additional_properties": False
                },
                "orion_formulation_descriptor": {
                    "type": "object",
                    "title": "Formulation",
                    "required": [
                        "type"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Formulation"
                            ],
                            "type": "string",
                            "default": "Formulation"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_alloy_composition_descriptor": {
                    "type": "object",
                    "title": "AlloyComposition",
                    "required": [
                        "type",
                        "descriptor_key",
                        "balance_element",
                        "basis",
                        "threshold"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Alloy composition"
                            ],
                            "type": "string",
                            "default": "Alloy composition"
                        },
                        "basis": {
                            "type": "number"
                        },
                        "threshold": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        },
                        "balance_element": {
                            "enum": [
                                "HYDROGEN",
                                "DEUTERIUM",
                                "TRITIUM",
                                "HELIUM",
                                "LITHIUM",
                                "BERYLLIUM",
                                "BORON",
                                "CARBON",
                                "NITROGEN",
                                "OXYGEN",
                                "FLUORINE",
                                "NEON",
                                "SODIUM",
                                "MAGNESIUM",
                                "ALUMINUM",
                                "SILICON",
                                "PHOSPHORUS",
                                "SULFUR",
                                "CHLORINE",
                                "ARGON",
                                "POTASSIUM",
                                "CALCIUM",
                                "SCANDIUM",
                                "TITANIUM",
                                "VANADIUM",
                                "CHROMIUM",
                                "MANGANESE",
                                "IRON",
                                "COBALT",
                                "NICKEL",
                                "COPPER",
                                "ZINC",
                                "GALLIUM",
                                "GERMANIUM",
                                "ARSENIC",
                                "SELENIUM",
                                "BROMINE",
                                "KRYPTON",
                                "RUBIDIUM",
                                "STRONTIUM",
                                "YTTRIUM",
                                "ZIRCONIUM",
                                "NIOBIUM",
                                "MOLYBDENUM",
                                "TECHNETIUM",
                                "RUTHENIUM",
                                "RHODIUM",
                                "PALLADIUM",
                                "SILVER",
                                "CADMIUM",
                                "INDIUM",
                                "TIN",
                                "ANTIMONY",
                                "TELLURIUM",
                                "IODINE",
                                "XENON",
                                "CESIUM",
                                "BARIUM",
                                "LANTHANUM",
                                "CERIUM",
                                "PRASEODYMIUM",
                                "NEODYMIUM",
                                "PROMETHIUM",
                                "SAMARIUM",
                                "EUROPIUM",
                                "GADOLINIUM",
                                "TERBIUM",
                                "DYSPROSIUM",
                                "HOLMIUM",
                                "ERBIUM",
                                "THULIUM",
                                "YTTERBIUM",
                                "LUTETIUM",
                                "HAFNIUM",
                                "TANTALUM",
                                "TUNGSTEN",
                                "RHENIUM",
                                "OSMIUM",
                                "IRIDIUM",
                                "PLATINUM",
                                "GOLD",
                                "MERCURY",
                                "THALLIUM",
                                "LEAD",
                                "BISMUTH",
                                "POLONIUM",
                                "ASTATINE",
                                "RADON",
                                "FRANCIUM",
                                "RADIUM",
                                "ACTINIUM",
                                "THORIUM",
                                "PROTACTINIUM",
                                "URANIUM",
                                "NEPTUNIUM",
                                "PLUTONIUM",
                                "AMERICIUM",
                                "CURIUM",
                                "BERKELIUM",
                                "CALIFORNIUM",
                                "EINSTEINIUM",
                                "FERMIUM",
                                "MENDELEVIUM",
                                "NOBELIUM",
                                "LAWRENCIUM",
                                "RUTHERFORDIUM",
                                "DUBNIUM",
                                "SEABORGIUM",
                                "BOHRIUM",
                                "HASSIUM",
                                "MEITNERIUM",
                                "DARMSTADTIUM",
                                "ROENTGENIUM",
                                "COPERNICIUM",
                                "FLEROVIUM",
                                "LIVERMORIUM",
                                "WILDCARD"
                            ],
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_organic_chemical_formula_descriptor": {
                    "type": "object",
                    "title": "Organic",
                    "required": [
                        "type",
                        "descriptor_key"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Organic"
                            ],
                            "type": "string",
                            "default": "Organic"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_inorganic_chemical_formula_descriptor": {
                    "type": "object",
                    "title": "Inorganic",
                    "required": [
                        "type",
                        "threshold"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Inorganic"
                            ],
                            "type": "string",
                            "default": "Inorganic"
                        },
                        "threshold": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                }
            },
            "additional_properties": False
        },
        "tags": []
    },
    {
        "id": "a294473c-7592-4fbe-86f2-37974352ca2b",
        "module_type": "SCORE",
        "display_name": "OrionMPVScore",
        "schema": {
            "type": "object",
            "title": "MPV",
            "schema": "http://json-schema.org/draft-04/schema#",
            "required": [
                "type",
                "name",
                "description",
                "objectives",
                "constraints"
            ],
            "properties": {
                "name": {
                    "type": "string"
                },
                "type": {
                    "enum": [
                        "MPV"
                    ],
                    "type": "string",
                    "default": "MPV"
                },
                "objectives": {
                    "type": "array",
                    "items": {
                        "oneOf": [
                            {
                                "$ref": "#/definitions/OrionScalarMaxObjective"
                            },
                            {
                                "$ref": "#/definitions/OrionScalarMinObjective"
                            },
                            {
                                "$ref": "#/definitions/OrionScalarTuneObjective"
                            }
                        ]
                    }
                },
                "constraints": {
                    "type": "array",
                    "items": {
                        "oneOf": [
                            {
                                "$ref": "#/definitions/OrionRealRangeConstraint"
                            },
                            {
                                "$ref": "#/definitions/OrionElementalConstraint"
                            },
                            {
                                "$ref": "#/definitions/OrionClassMembershipConstraint"
                            },
                            {
                                "$ref": "#/definitions/OrionCompositionRangeConstraint"
                            }
                        ]
                    }
                },
                "description": {
                    "type": "string"
                }
            },
            "definitions": {
                "orion_scalar_max_objective": {
                    "type": "object",
                    "title": "ScalarMax",
                    "required": [
                        "type",
                        "descriptor_key",
                        "lower_bound",
                        "upper_bound"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "ScalarMax"
                            ],
                            "type": "string",
                            "default": "ScalarMax"
                        },
                        "lower_bound": {
                            "type": "number"
                        },
                        "upper_bound": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_scalar_min_objective": {
                    "type": "object",
                    "title": "ScalarMin",
                    "required": [
                        "type",
                        "descriptor_key",
                        "lower_bound",
                        "upper_bound"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "ScalarMin"
                            ],
                            "type": "string",
                            "default": "ScalarMin"
                        },
                        "lower_bound": {
                            "type": "number"
                        },
                        "upper_bound": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_elemental_constraint": {
                    "type": "object",
                    "title": "Elemental",
                    "required": [
                        "type",
                        "descriptor_key",
                        "required_elements",
                        "restricted_elements"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Elemental"
                            ],
                            "type": "string",
                            "default": "Elemental"
                        },
                        "descriptor_key": {
                            "type": "string",
                            "description": "Descriptor key"
                        },
                        "required_elements": {
                            "type": "array",
                            "items": {
                                "enum": [
                                    "HYDROGEN",
                                    "DEUTERIUM",
                                    "TRITIUM",
                                    "HELIUM",
                                    "LITHIUM",
                                    "BERYLLIUM",
                                    "BORON",
                                    "CARBON",
                                    "NITROGEN",
                                    "OXYGEN",
                                    "FLUORINE",
                                    "NEON",
                                    "SODIUM",
                                    "MAGNESIUM",
                                    "ALUMINUM",
                                    "SILICON",
                                    "PHOSPHORUS",
                                    "SULFUR",
                                    "CHLORINE",
                                    "ARGON",
                                    "POTASSIUM",
                                    "CALCIUM",
                                    "SCANDIUM",
                                    "TITANIUM",
                                    "VANADIUM",
                                    "CHROMIUM",
                                    "MANGANESE",
                                    "IRON",
                                    "COBALT",
                                    "NICKEL",
                                    "COPPER",
                                    "ZINC",
                                    "GALLIUM",
                                    "GERMANIUM",
                                    "ARSENIC",
                                    "SELENIUM",
                                    "BROMINE",
                                    "KRYPTON",
                                    "RUBIDIUM",
                                    "STRONTIUM",
                                    "YTTRIUM",
                                    "ZIRCONIUM",
                                    "NIOBIUM",
                                    "MOLYBDENUM",
                                    "TECHNETIUM",
                                    "RUTHENIUM",
                                    "RHODIUM",
                                    "PALLADIUM",
                                    "SILVER",
                                    "CADMIUM",
                                    "INDIUM",
                                    "TIN",
                                    "ANTIMONY",
                                    "TELLURIUM",
                                    "IODINE",
                                    "XENON",
                                    "CESIUM",
                                    "BARIUM",
                                    "LANTHANUM",
                                    "CERIUM",
                                    "PRASEODYMIUM",
                                    "NEODYMIUM",
                                    "PROMETHIUM",
                                    "SAMARIUM",
                                    "EUROPIUM",
                                    "GADOLINIUM",
                                    "TERBIUM",
                                    "DYSPROSIUM",
                                    "HOLMIUM",
                                    "ERBIUM",
                                    "THULIUM",
                                    "YTTERBIUM",
                                    "LUTETIUM",
                                    "HAFNIUM",
                                    "TANTALUM",
                                    "TUNGSTEN",
                                    "RHENIUM",
                                    "OSMIUM",
                                    "IRIDIUM",
                                    "PLATINUM",
                                    "GOLD",
                                    "MERCURY",
                                    "THALLIUM",
                                    "LEAD",
                                    "BISMUTH",
                                    "POLONIUM",
                                    "ASTATINE",
                                    "RADON",
                                    "FRANCIUM",
                                    "RADIUM",
                                    "ACTINIUM",
                                    "THORIUM",
                                    "PROTACTINIUM",
                                    "URANIUM",
                                    "NEPTUNIUM",
                                    "PLUTONIUM",
                                    "AMERICIUM",
                                    "CURIUM",
                                    "BERKELIUM",
                                    "CALIFORNIUM",
                                    "EINSTEINIUM",
                                    "FERMIUM",
                                    "MENDELEVIUM",
                                    "NOBELIUM",
                                    "LAWRENCIUM",
                                    "RUTHERFORDIUM",
                                    "DUBNIUM",
                                    "SEABORGIUM",
                                    "BOHRIUM",
                                    "HASSIUM",
                                    "MEITNERIUM",
                                    "DARMSTADTIUM",
                                    "ROENTGENIUM",
                                    "COPERNICIUM",
                                    "FLEROVIUM",
                                    "LIVERMORIUM",
                                    "WILDCARD"
                                ],
                                "type": "string"
                            }
                        },
                        "restricted_elements": {
                            "type": "array",
                            "items": {
                                "enum": [
                                    "HYDROGEN",
                                    "DEUTERIUM",
                                    "TRITIUM",
                                    "HELIUM",
                                    "LITHIUM",
                                    "BERYLLIUM",
                                    "BORON",
                                    "CARBON",
                                    "NITROGEN",
                                    "OXYGEN",
                                    "FLUORINE",
                                    "NEON",
                                    "SODIUM",
                                    "MAGNESIUM",
                                    "ALUMINUM",
                                    "SILICON",
                                    "PHOSPHORUS",
                                    "SULFUR",
                                    "CHLORINE",
                                    "ARGON",
                                    "POTASSIUM",
                                    "CALCIUM",
                                    "SCANDIUM",
                                    "TITANIUM",
                                    "VANADIUM",
                                    "CHROMIUM",
                                    "MANGANESE",
                                    "IRON",
                                    "COBALT",
                                    "NICKEL",
                                    "COPPER",
                                    "ZINC",
                                    "GALLIUM",
                                    "GERMANIUM",
                                    "ARSENIC",
                                    "SELENIUM",
                                    "BROMINE",
                                    "KRYPTON",
                                    "RUBIDIUM",
                                    "STRONTIUM",
                                    "YTTRIUM",
                                    "ZIRCONIUM",
                                    "NIOBIUM",
                                    "MOLYBDENUM",
                                    "TECHNETIUM",
                                    "RUTHENIUM",
                                    "RHODIUM",
                                    "PALLADIUM",
                                    "SILVER",
                                    "CADMIUM",
                                    "INDIUM",
                                    "TIN",
                                    "ANTIMONY",
                                    "TELLURIUM",
                                    "IODINE",
                                    "XENON",
                                    "CESIUM",
                                    "BARIUM",
                                    "LANTHANUM",
                                    "CERIUM",
                                    "PRASEODYMIUM",
                                    "NEODYMIUM",
                                    "PROMETHIUM",
                                    "SAMARIUM",
                                    "EUROPIUM",
                                    "GADOLINIUM",
                                    "TERBIUM",
                                    "DYSPROSIUM",
                                    "HOLMIUM",
                                    "ERBIUM",
                                    "THULIUM",
                                    "YTTERBIUM",
                                    "LUTETIUM",
                                    "HAFNIUM",
                                    "TANTALUM",
                                    "TUNGSTEN",
                                    "RHENIUM",
                                    "OSMIUM",
                                    "IRIDIUM",
                                    "PLATINUM",
                                    "GOLD",
                                    "MERCURY",
                                    "THALLIUM",
                                    "LEAD",
                                    "BISMUTH",
                                    "POLONIUM",
                                    "ASTATINE",
                                    "RADON",
                                    "FRANCIUM",
                                    "RADIUM",
                                    "ACTINIUM",
                                    "THORIUM",
                                    "PROTACTINIUM",
                                    "URANIUM",
                                    "NEPTUNIUM",
                                    "PLUTONIUM",
                                    "AMERICIUM",
                                    "CURIUM",
                                    "BERKELIUM",
                                    "CALIFORNIUM",
                                    "EINSTEINIUM",
                                    "FERMIUM",
                                    "MENDELEVIUM",
                                    "NOBELIUM",
                                    "LAWRENCIUM",
                                    "RUTHERFORDIUM",
                                    "DUBNIUM",
                                    "SEABORGIUM",
                                    "BOHRIUM",
                                    "HASSIUM",
                                    "MEITNERIUM",
                                    "DARMSTADTIUM",
                                    "ROENTGENIUM",
                                    "COPERNICIUM",
                                    "FLEROVIUM",
                                    "LIVERMORIUM",
                                    "WILDCARD"
                                ],
                                "type": "string"
                            }
                        }
                    },
                    "additional_properties": False
                },
                "orion_real_range_constraint": {
                    "type": "object",
                    "title": "ScalarRange",
                    "required": [
                        "type",
                        "descriptor_key"
                    ],
                    "properties": {
                        "max": {
                            "type": "number"
                        },
                        "min": {
                            "type": "number"
                        },
                        "type": {
                            "enum": [
                                "ScalarRange"
                            ],
                            "type": "string",
                            "default": "ScalarRange"
                        },
                        "max_inclusive": {
                            "type": "boolean"
                        },
                        "min_inclusive": {
                            "type": "boolean"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_scalar_tune_objective": {
                    "type": "object",
                    "title": "TargetValue",
                    "required": [
                        "type",
                        "descriptor_key",
                        "target",
                        "power"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "TargetValue"
                            ],
                            "type": "string",
                            "default": "TargetValue"
                        },
                        "power": {
                            "type": "number"
                        },
                        "target": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        }
                    },
                    "additional_properties": False
                },
                "orion_class_membership_constraint": {
                    "type": "object",
                    "title": "ClassMembership",
                    "required": [
                        "type",
                        "descriptor_key",
                        "acceptable_classes"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "Categorical"
                            ],
                            "type": "string",
                            "default": "Categorical"
                        },
                        "descriptor_key": {
                            "type": "string"
                        },
                        "acceptable_classes": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        }
                    },
                    "additional_properties": False
                },
                "orion_composition_range_constraint": {
                    "type": "object",
                    "title": "CompositionRange",
                    "required": [
                        "type",
                        "descriptor_key",
                        "element"
                    ],
                    "properties": {
                        "type": {
                            "enum": [
                                "CompositionRange"
                            ],
                            "type": "string",
                            "default": "CompositionRange"
                        },
                        "basis": {
                            "type": "number"
                        },
                        "element": {
                            "enum": [
                                "HYDROGEN",
                                "DEUTERIUM",
                                "TRITIUM",
                                "HELIUM",
                                "LITHIUM",
                                "BERYLLIUM",
                                "BORON",
                                "CARBON",
                                "NITROGEN",
                                "OXYGEN",
                                "FLUORINE",
                                "NEON",
                                "SODIUM",
                                "MAGNESIUM",
                                "ALUMINUM",
                                "SILICON",
                                "PHOSPHORUS",
                                "SULFUR",
                                "CHLORINE",
                                "ARGON",
                                "POTASSIUM",
                                "CALCIUM",
                                "SCANDIUM",
                                "TITANIUM",
                                "VANADIUM",
                                "CHROMIUM",
                                "MANGANESE",
                                "IRON",
                                "COBALT",
                                "NICKEL",
                                "COPPER",
                                "ZINC",
                                "GALLIUM",
                                "GERMANIUM",
                                "ARSENIC",
                                "SELENIUM",
                                "BROMINE",
                                "KRYPTON",
                                "RUBIDIUM",
                                "STRONTIUM",
                                "YTTRIUM",
                                "ZIRCONIUM",
                                "NIOBIUM",
                                "MOLYBDENUM",
                                "TECHNETIUM",
                                "RUTHENIUM",
                                "RHODIUM",
                                "PALLADIUM",
                                "SILVER",
                                "CADMIUM",
                                "INDIUM",
                                "TIN",
                                "ANTIMONY",
                                "TELLURIUM",
                                "IODINE",
                                "XENON",
                                "CESIUM",
                                "BARIUM",
                                "LANTHANUM",
                                "CERIUM",
                                "PRASEODYMIUM",
                                "NEODYMIUM",
                                "PROMETHIUM",
                                "SAMARIUM",
                                "EUROPIUM",
                                "GADOLINIUM",
                                "TERBIUM",
                                "DYSPROSIUM",
                                "HOLMIUM",
                                "ERBIUM",
                                "THULIUM",
                                "YTTERBIUM",
                                "LUTETIUM",
                                "HAFNIUM",
                                "TANTALUM",
                                "TUNGSTEN",
                                "RHENIUM",
                                "OSMIUM",
                                "IRIDIUM",
                                "PLATINUM",
                                "GOLD",
                                "MERCURY",
                                "THALLIUM",
                                "LEAD",
                                "BISMUTH",
                                "POLONIUM",
                                "ASTATINE",
                                "RADON",
                                "FRANCIUM",
                                "RADIUM",
                                "ACTINIUM",
                                "THORIUM",
                                "PROTACTINIUM",
                                "URANIUM",
                                "NEPTUNIUM",
                                "PLUTONIUM",
                                "AMERICIUM",
                                "CURIUM",
                                "BERKELIUM",
                                "CALIFORNIUM",
                                "EINSTEINIUM",
                                "FERMIUM",
                                "MENDELEVIUM",
                                "NOBELIUM",
                                "LAWRENCIUM",
                                "RUTHERFORDIUM",
                                "DUBNIUM",
                                "SEABORGIUM",
                                "BOHRIUM",
                                "HASSIUM",
                                "MEITNERIUM",
                                "DARMSTADTIUM",
                                "ROENTGENIUM",
                                "COPERNICIUM",
                                "FLEROVIUM",
                                "LIVERMORIUM",
                                "WILDCARD"
                            ],
                            "type": "string"
                        },
                        "max_frac": {
                            "type": "number"
                        },
                        "min_frac": {
                            "type": "number"
                        },
                        "descriptor_key": {
                            "type": "string"
                        },
                        "el_is_required": {
                            "type": "boolean"
                        }
                    },
                    "additional_properties": False
                }
            },
            "additional_properties": False
        },
        "tags": []
    },
    {
        "id": "2cf31fb8-5ad8-42ab-87b1-9fcf4da2bfc4",
        "module_type": "OBJECTIVE",
        "display_name": "OrionScalarTuneObjective",
        "schema": {
            "type": "object",
            "title": "TargetValue",
            "schema": "http://json-schema.org/draft-04/schema#",
            "required": [
                "type",
                "descriptor_key",
                "target",
                "power"
            ],
            "properties": {
                "type": {
                    "enum": [
                        "TargetValue"
                    ],
                    "type": "string",
                    "default": "TargetValue"
                },
                "power": {
                    "type": "number"
                },
                "target": {
                    "type": "number"
                },
                "descriptor_key": {
                    "type": "string"
                }
            },
            "additional_properties": False
        },
        "tags": []
    },
    {
        "id": "98e3b305-834f-49cd-8412-a8e7c6320542",
        "module_type": "CONSTRAINT",
        "display_name": "OrionElementalConstraint",
        "schema": {
            "type": "object",
            "title": "Elemental",
            "schema": "http://json-schema.org/draft-04/schema#",
            "required": [
                "type",
                "descriptor_key",
                "required_elements",
                "restricted_elements"
            ],
            "properties": {
                "type": {
                    "enum": [
                        "Elemental"
                    ],
                    "type": "string",
                    "default": "Elemental"
                },
                "descriptor_key": {
                    "type": "string",
                    "description": "Descriptor key"
                },
                "required_elements": {
                    "type": "array",
                    "items": {
                        "enum": [
                            "HYDROGEN",
                            "DEUTERIUM",
                            "TRITIUM",
                            "HELIUM",
                            "LITHIUM",
                            "BERYLLIUM",
                            "BORON",
                            "CARBON",
                            "NITROGEN",
                            "OXYGEN",
                            "FLUORINE",
                            "NEON",
                            "SODIUM",
                            "MAGNESIUM",
                            "ALUMINUM",
                            "SILICON",
                            "PHOSPHORUS",
                            "SULFUR",
                            "CHLORINE",
                            "ARGON",
                            "POTASSIUM",
                            "CALCIUM",
                            "SCANDIUM",
                            "TITANIUM",
                            "VANADIUM",
                            "CHROMIUM",
                            "MANGANESE",
                            "IRON",
                            "COBALT",
                            "NICKEL",
                            "COPPER",
                            "ZINC",
                            "GALLIUM",
                            "GERMANIUM",
                            "ARSENIC",
                            "SELENIUM",
                            "BROMINE",
                            "KRYPTON",
                            "RUBIDIUM",
                            "STRONTIUM",
                            "YTTRIUM",
                            "ZIRCONIUM",
                            "NIOBIUM",
                            "MOLYBDENUM",
                            "TECHNETIUM",
                            "RUTHENIUM",
                            "RHODIUM",
                            "PALLADIUM",
                            "SILVER",
                            "CADMIUM",
                            "INDIUM",
                            "TIN",
                            "ANTIMONY",
                            "TELLURIUM",
                            "IODINE",
                            "XENON",
                            "CESIUM",
                            "BARIUM",
                            "LANTHANUM",
                            "CERIUM",
                            "PRASEODYMIUM",
                            "NEODYMIUM",
                            "PROMETHIUM",
                            "SAMARIUM",
                            "EUROPIUM",
                            "GADOLINIUM",
                            "TERBIUM",
                            "DYSPROSIUM",
                            "HOLMIUM",
                            "ERBIUM",
                            "THULIUM",
                            "YTTERBIUM",
                            "LUTETIUM",
                            "HAFNIUM",
                            "TANTALUM",
                            "TUNGSTEN",
                            "RHENIUM",
                            "OSMIUM",
                            "IRIDIUM",
                            "PLATINUM",
                            "GOLD",
                            "MERCURY",
                            "THALLIUM",
                            "LEAD",
                            "BISMUTH",
                            "POLONIUM",
                            "ASTATINE",
                            "RADON",
                            "FRANCIUM",
                            "RADIUM",
                            "ACTINIUM",
                            "THORIUM",
                            "PROTACTINIUM",
                            "URANIUM",
                            "NEPTUNIUM",
                            "PLUTONIUM",
                            "AMERICIUM",
                            "CURIUM",
                            "BERKELIUM",
                            "CALIFORNIUM",
                            "EINSTEINIUM",
                            "FERMIUM",
                            "MENDELEVIUM",
                            "NOBELIUM",
                            "LAWRENCIUM",
                            "RUTHERFORDIUM",
                            "DUBNIUM",
                            "SEABORGIUM",
                            "BOHRIUM",
                            "HASSIUM",
                            "MEITNERIUM",
                            "DARMSTADTIUM",
                            "ROENTGENIUM",
                            "COPERNICIUM",
                            "FLEROVIUM",
                            "LIVERMORIUM",
                            "WILDCARD"
                        ],
                        "type": "string"
                    }
                },
                "restricted_elements": {
                    "type": "array",
                    "items": {
                        "enum": [
                            "HYDROGEN",
                            "DEUTERIUM",
                            "TRITIUM",
                            "HELIUM",
                            "LITHIUM",
                            "BERYLLIUM",
                            "BORON",
                            "CARBON",
                            "NITROGEN",
                            "OXYGEN",
                            "FLUORINE",
                            "NEON",
                            "SODIUM",
                            "MAGNESIUM",
                            "ALUMINUM",
                            "SILICON",
                            "PHOSPHORUS",
                            "SULFUR",
                            "CHLORINE",
                            "ARGON",
                            "POTASSIUM",
                            "CALCIUM",
                            "SCANDIUM",
                            "TITANIUM",
                            "VANADIUM",
                            "CHROMIUM",
                            "MANGANESE",
                            "IRON",
                            "COBALT",
                            "NICKEL",
                            "COPPER",
                            "ZINC",
                            "GALLIUM",
                            "GERMANIUM",
                            "ARSENIC",
                            "SELENIUM",
                            "BROMINE",
                            "KRYPTON",
                            "RUBIDIUM",
                            "STRONTIUM",
                            "YTTRIUM",
                            "ZIRCONIUM",
                            "NIOBIUM",
                            "MOLYBDENUM",
                            "TECHNETIUM",
                            "RUTHENIUM",
                            "RHODIUM",
                            "PALLADIUM",
                            "SILVER",
                            "CADMIUM",
                            "INDIUM",
                            "TIN",
                            "ANTIMONY",
                            "TELLURIUM",
                            "IODINE",
                            "XENON",
                            "CESIUM",
                            "BARIUM",
                            "LANTHANUM",
                            "CERIUM",
                            "PRASEODYMIUM",
                            "NEODYMIUM",
                            "PROMETHIUM",
                            "SAMARIUM",
                            "EUROPIUM",
                            "GADOLINIUM",
                            "TERBIUM",
                            "DYSPROSIUM",
                            "HOLMIUM",
                            "ERBIUM",
                            "THULIUM",
                            "YTTERBIUM",
                            "LUTETIUM",
                            "HAFNIUM",
                            "TANTALUM",
                            "TUNGSTEN",
                            "RHENIUM",
                            "OSMIUM",
                            "IRIDIUM",
                            "PLATINUM",
                            "GOLD",
                            "MERCURY",
                            "THALLIUM",
                            "LEAD",
                            "BISMUTH",
                            "POLONIUM",
                            "ASTATINE",
                            "RADON",
                            "FRANCIUM",
                            "RADIUM",
                            "ACTINIUM",
                            "THORIUM",
                            "PROTACTINIUM",
                            "URANIUM",
                            "NEPTUNIUM",
                            "PLUTONIUM",
                            "AMERICIUM",
                            "CURIUM",
                            "BERKELIUM",
                            "CALIFORNIUM",
                            "EINSTEINIUM",
                            "FERMIUM",
                            "MENDELEVIUM",
                            "NOBELIUM",
                            "LAWRENCIUM",
                            "RUTHERFORDIUM",
                            "DUBNIUM",
                            "SEABORGIUM",
                            "BOHRIUM",
                            "HASSIUM",
                            "MEITNERIUM",
                            "DARMSTADTIUM",
                            "ROENTGENIUM",
                            "COPERNICIUM",
                            "FLEROVIUM",
                            "LIVERMORIUM",
                            "WILDCARD"
                        ],
                        "type": "string"
                    }
                }
            },
            "additional_properties": False
        },
        "tags": []
    }
]