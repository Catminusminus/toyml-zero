import random
import config


def gen_setup_ops(config_):
    return random.choice(config_["setup_ops"])


def gen_predict_ops(config_):
    return random.choice(config_["predict_ops"])


def gen_learn_ops(config_):
    return random.choice(config_["learn_ops"])


def ScalarInAddress():
    return random.choice(range(0, config.kMaxScalarAddresses))


def VectorInAddress():
    return random.choice(range(0, config.kMaxVectorAddresses))


def MatrixInAddress():
    return random.choice(range(0, config.kMaxMatrixAddresses))


def ScalarOutAddress():
    return random.choice(range(config.kFirstOutScalarAddress, config.kMaxScalarAddresses))


def VectorOutAddress():
    return random.choice(range(config.kFirstOutVectorAddress, config.kMaxVectorAddresses))


def MatrixOutAddress():
    return random.choice(range(config.kFirstOutMatrixAddress, config.kMaxMatrixAddresses))


def UniformActivation(low, high):
    return random.uniform(low, high)
