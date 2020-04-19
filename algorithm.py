from instruction import NO_OP, Instruction
from config import MUTATION_TYPE
import config
import gen
from enum_switch import Switch
import random
from memory import Memory


class ComponentFunction:
    def __init__(self, config_item, gen_ops):
        self.instructions = [NO_OP for i in range(config.config[config_item])]
        self.gen_ops = gen_ops

    def randomize(self):
        for instruction in self.instructions:
            instruction.setOpAndRandomizeParams(self.gen_ops(config.config))

    def randomizeOne(self):
        index = random.choice(range(len(self.instructions)))
        self.instructions[index].setOpAndRandomizeParams(self.gen_ops(config.config))

    def alterParam(self):
        index = random.choice(range(len(self.instructions)))
        self.instructions[index].alterParam()

    def execute(self):
        for instruction in self.instructions:
            instruction.execute()


class Algorithm:
    def __init__(self):
        self.setup_ = ComponentFunction("setup_size_init", gen.gen_setup_ops)
        self.predict_ = ComponentFunction("predict_size_init", gen.gen_predict_ops)
        self.learn_ = ComponentFunction("learn_size_init", gen.gen_learn_ops)

    def randomize(self):
        self.setup_.randomize()
        self.predict_.randomize()
        self.learn_.randomize()

    def mutate(self, component):
        class RandomDict(Switch):
            def ALTER_PARAM_MUTATION_TYPE(this):
                component.alterParam()

            def RANDOMIZE_INSTRUCTION_MUTATION_TYPE(this):
                component.randomizeOne()

            def RANDOMIZE_COMPONENT_FUNCTION_MUTATION_TYPE(this):
                component.randomize()

        randomize_dict = RandomDict(MUTATION_TYPE)
        mutation_type = random.choice(list(MUTATION_TYPE))
        randomize_dict(mutation_type)

    def mutateSetup(self):
        self.mutate(self.setup_)

    def mutatePredict(self):
        self.mutate(self.predict_)

    def mutateLearn(self):
        self.mutate(self.learn_)

    def train(self, train_data):
        Y, X = train_data["label"].values, train_data.drop("label", axis=1).values
        Memory.wipe()
        for x, y in zip(X, Y):
            Memory.vector[config.kFeaturesVectorAddress] = x
            Memory.scalar[config.kLabelsScalarAddress] = y
            self.setup_.execute()
            self.predict_.execute()
            self.learn_.execute()

    def test(self, test_data):
        count = 0
        Y, X = test_data["label"].values, test_data.drop("label", axis=1).values
        Memory.wipe()
        for x, y in zip(X, Y):
            Memory.vector[config.kFeaturesVectorAddress] = x
            Memory.scalar[config.kLabelsScalarAddress] = y
            self.setup_.execute()
            self.predict_.execute()
            count += Memory.oneIfPredictIsAccurateElseZero()
        return count / len(test_data)

    def evaluate(self, train_data, test_data):
        self.train(train_data)
        return self.test(test_data)
