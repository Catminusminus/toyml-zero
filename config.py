from enum import Enum


class MUTATION_TYPE(Enum):
    ALTER_PARAM_MUTATION_TYPE = 1
    RANDOMIZE_INSTRUCTION_MUTATION_TYPE = 2
    RANDOMIZE_COMPONENT_FUNCTION_MUTATION_TYPE = 3


class OP(Enum):
    NO_OP = 0
    SCALAR_CONST_SET_OP = 1
    VECTOR_INNER_PRODUCT_OP = 2
    SCALAR_DIFF_OP = 3
    SCALAR_PRODUCT_OP = 4
    SCALAR_VECTOR_PRODUCT_OP = 5
    VECTOR_SUM_OP = 6


class ComponentFunction(Enum):
    kSetupComponentFunction = 0
    kPredictCompoentFunction = 1
    kLearnComponentFunction = 2


kLabelsScalarAddress = 0
kPredictionsScalarAddress = 1
kFirstOutScalarAddress = 1
kMaxScalarAddresses = 20

# Vector addresses.
kFeaturesVectorAddress = 0
kFirstOutVectorAddress = 1

# <vector output branch>.
kLabelsVectorAddress = 1
kPredictionsVectorAddress = 2
kMaxVectorAddresses = 20

# Matrix addresses.
kFirstOutMatrixAddress = 0
kMaxMatrixAddresses = 20


config = {
    "mutation_types": [
        MUTATION_TYPE.ALTER_PARAM_MUTATION_TYPE,
        MUTATION_TYPE.RANDOMIZE_INSTRUCTION_MUTATION_TYPE,
        MUTATION_TYPE.RANDOMIZE_COMPONENT_FUNCTION_MUTATION_TYPE,
    ],
    "setup_ops": [
        OP.SCALAR_CONST_SET_OP,
        OP.VECTOR_INNER_PRODUCT_OP,
        OP.SCALAR_DIFF_OP,
        OP.SCALAR_PRODUCT_OP,
        OP.SCALAR_VECTOR_PRODUCT_OP,
        OP.VECTOR_SUM_OP,
    ],
    "predict_ops": [
        OP.SCALAR_CONST_SET_OP,
        OP.VECTOR_INNER_PRODUCT_OP,
        OP.SCALAR_DIFF_OP,
        OP.SCALAR_PRODUCT_OP,
        OP.SCALAR_VECTOR_PRODUCT_OP,
        OP.VECTOR_SUM_OP,
    ],
    "learn_ops": [
        OP.SCALAR_CONST_SET_OP,
        OP.VECTOR_INNER_PRODUCT_OP,
        OP.SCALAR_DIFF_OP,
        OP.SCALAR_PRODUCT_OP,
        OP.SCALAR_VECTOR_PRODUCT_OP,
        OP.VECTOR_SUM_OP,
    ],
    "population_size": 1000,  # 1000
    "selection_size": 10,  # 10
    "learn_size_init": 8,
    "setup_size_init": 10,
    "predict_size_init": 2,
}
