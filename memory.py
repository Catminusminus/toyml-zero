import config


class Memory:
    vector = [0 for i in range(config.kMaxVectorAddresses)]
    scalar = [0 for i in range(config.kMaxScalarAddresses)]

    @classmethod
    def oneIfPredictIsAccurateElseZero(cls):
        return cls.scalar[config.kPredictionsScalarAddress]

    @classmethod
    def wipe(cls):
        cls.vector = [0 for i in range(config.kMaxVectorAddresses)]
        cls.scalar = [0 for i in range(config.kMaxScalarAddresses)]
