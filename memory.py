import config
import numpy as np


class Memory:
    vector = [0 for i in range(config.kMaxVectorAddresses)]
    scalar = [0 for i in range(config.kMaxScalarAddresses)]

    @classmethod
    def oneIfPredictIsAccurateElseZero(cls):
        return (
            1
            if np.abs(
                cls.scalar[config.kLabelsScalarAddress]
                - cls.scalar[config.kPredictionsScalarAddress]
            )
            < 0.5
            else 0
        )

    @classmethod
    def wipe(cls):
        cls.vector = [0 for i in range(config.kMaxVectorAddresses)]
        cls.scalar = [0 for i in range(config.kMaxScalarAddresses)]
