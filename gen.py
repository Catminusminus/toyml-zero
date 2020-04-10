import random


def gen_setup_ops(config_):
    return random.choice(config_["setup_ops"])


def gen_predict_ops(config_):
    return random.choice(config_["predict_ops"])


def gen_learn_ops(config_):
    return random.choice(config_["learn_ops"])


def ScalarInAddress():
    return random.choice(range(0, kMaxScalarAddresses))


def VectorInAddress():
    return random.choice(range(0, kMaxVectorAddresses))


def MatrixInAddress():
    return random.choice(range(0, kMaxMatrixAddresses))


def ScalarOutAddress():
    return random.choice(range(kFirstOutScalarAddress, kMaxScalarAddresses))


def VectorOutAddress():
    return random.choice(range(kFirstOutVectorAddress, kMaxVectorAddresses))


def MatrixOutAddress():
    return random.choice(range(kFirstOutMatrixAddress, kMaxMatrixAddresses))


def UniformActivation(low, high):
    return random.uniform(low, high)
