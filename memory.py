import config


class Memory:
    vector = [None for i in range(config.kMaxVectorAddresses)]
    scalar = [None for i in range(config.kMaxScalarAddresses)]

    @classmethod
    def oneIfPredictIsAccurateElseZero(cls):
        return cls.scalar[config.kPredictionsScalarAddress]
