import config
from enum_switch import Switch
import random
from memory import Memory
import numpy as np
import gen


class Instruction:
    def __init__(self):
        self.op_ = None
        self.in1_ = None  # First input address.
        self.in2_ = None  # Second input address.
        self.out_ = None  # Output address.

        self.activation_data_ = None
        self.float_data_0_ = None
        self.float_data_1_ = None
        self.float_data_2_ = None

    def evalutate(self):
        raise NotImplemetError("TODO")

    def fillWithNoOp(self):
        self.op_ = config.OP.NO_OP
        self.in1_ = 0
        self.in2_ = 0
        self.out_ = 0
        self.activation_data_ = 0.0
        self.float_data_0_ = 0.0
        self.float_data_1_ = 0.0
        self.float_data_2_ = 0.0

    def randomizeOut(self):
        class RandomDict(Switch):
            def NO_OP(this):
                print("Invalid OP")
                raise

            def SCALAR_CONST_SET_OP(this):
                self.out_ = gen.ScalarOutAddress()

            def VECTOR_INNER_PRODUCT_OP(this):
                self.out_ = gen.ScalarOutAddress()

            def SCALAR_DIFF_OP(this):
                self.out_ = gen.ScalarOutAddress()

            def SCALAR_PRODUCT_OP(this):
                self.out_ = gen.ScalarOutAddress()

            def SCALAR_VECTOR_PRODUCT_OP(this):
                self.out_ = gen.VectorOutAddress()

            def VECTOR_SUM_OP(this):
                self.out_ = gen.VectorOutAddress()

        random_dict = RandomDict(config.OP)
        random_dict(self.op_)

    def randomizeData(self):
        class RandomDict(Switch):
            def NO_OP(this):
                print("Invalid OP")
                raise

            def SCALAR_CONST_SET_OP(this):
                self.activation_data_ = gen.UniformActivation(-1.0, 1.0)

            def VECTOR_INNER_PRODUCT_OP(this):
                print("Invalid OP")
                raise

            def SCALAR_DIFF_OP(this):
                print("Invalid OP")
                raise

            def SCALAR_PRODUCT_OP(this):
                print("Invalid OP")
                raise

            def SCALAR_VECTOR_PRODUCT_OP(this):
                print("Invalid OP")
                raise

            def VECTOR_SUM_OP(this):
                print("Invalid OP")
                raise

        random_dict = RandomDict(config.OP)
        random_dict(self.op_)

    def randomizeIn1(self):
        class RandomDict(Switch):
            def NO_OP(this):
                print("Invalid OP")
                raise

            def SCALAR_CONST_SET_OP(this):
                print("Invalid OP")
                raise

            def VECTOR_INNER_PRODUCT_OP(this):
                self.in1_ = gen.VectorInAddress()

            def SCALAR_DIFF_OP(this):
                self.in1_ = gen.ScalarInAddress()

            def SCALAR_PRODUCT_OP(this):
                self.in1_ = gen.ScalarInAddress()

            def SCALAR_VECTOR_PRODUCT_OP(this):
                self.in1_ = gen.ScalarInAddress()

            def VECTOR_SUM_OP(this):
                self.in1_ = gen.VectorInAddress()

        random_dict = RandomDict(config.OP)
        random_dict(self.op_)

    def randomizeIn2(self):
        class RandomDict(Switch):
            def NO_OP(this):
                print("Invalid OP")
                raise

            def SCALAR_CONST_SET_OP(this):
                print("Invalid OP")
                raise

            def VECTOR_INNER_PRODUCT_OP(this):
                self.in2_ = gen.VectorInAddress()

            def SCALAR_DIFF_OP(this):
                self.in2_ = gen.ScalarInAddress()

            def SCALAR_PRODUCT_OP(this):
                self.in2_ = gen.ScalarInAddress()

            def SCALAR_VECTOR_PRODUCT_OP(this):
                self.in2_ = gen.VectorInAddress()

            def VECTOR_SUM_OP(this):
                self.in2_ = gen.VectorInAddress()

        random_dict = RandomDict(config.OP)
        random_dict(self.op_)

    def setOpAndRandomizeParams(self, op):
        self.fillWithNoOp()
        self.op_ = op

        class RandomDict(Switch):
            def NO_OP(this):
                pass

            def SCALAR_CONST_SET_OP(this):
                self.randomizeOut()
                self.randomizeData()

            def VECTOR_INNER_PRODUCT_OP(this):
                self.randomizeIn1()
                self.randomizeIn2()
                self.randomizeOut()

            def SCALAR_DIFF_OP(this):
                self.randomizeIn1()
                self.randomizeIn2()
                self.randomizeOut()

            def SCALAR_PRODUCT_OP(this):
                self.randomizeIn1()
                self.randomizeIn2()
                self.randomizeOut()

            def SCALAR_VECTOR_PRODUCT_OP(this):
                self.randomizeIn1()
                self.randomizeIn2()
                self.randomizeOut()

            def VECTOR_SUM_OP(this):
                self.randomizeIn1()
                self.randomizeIn2()
                self.randomizeOut()

        random_dict = RandomDict(config.OP)
        random_dict(op)

    def alterParam(self):
        class RandomDict(Switch):
            def NO_OP(this):
                return

            def SCALAR_CONST_SET_OP(this):
                choice = random.choice(range(0, 2))
                if choice == 0:
                    self.randomizeData()
                    return
                self.randomizeOut()

            def VECTOR_INNER_PRODUCT_OP(this):
                choice = random.choice(range(0, 3))
                if choice == 0:
                    self.randomizeIn1()
                    return
                if choice == 1:
                    self.randomizeIn2()
                    return
                self.randomizeOut()

            def SCALAR_DIFF_OP(this):
                choice = random.choice(range(0, 3))
                if choice == 0:
                    self.randomizeIn1()
                    return
                if choice == 1:
                    self.randomizeIn2()
                    return
                self.randomizeOut()

            def SCALAR_PRODUCT_OP(this):
                choice = random.choice(range(0, 3))
                if choice == 0:
                    self.randomizeIn1()
                    return
                if choice == 1:
                    self.randomizeIn2()
                    return
                self.randomizeOut()

            def SCALAR_VECTOR_PRODUCT_OP(this):
                choice = random.choice(range(0, 3))
                if choice == 0:
                    self.randomizeIn1()
                    return
                if choice == 1:
                    self.randomizeIn2()
                    return
                self.randomizeOut()

            def VECTOR_SUM_OP(this):
                choice = random.choice(range(0, 3))
                if choice == 0:
                    self.randomizeIn1()
                    return
                if choice == 1:
                    self.randomizeIn2()
                    return
                self.randomizeOut()

        random_dict = RandomDict(config.OP)
        random_dict(self.op_)

    def execute(self):
        class RandomDict(Switch):
            def NO_OP(this):
                pass

            def SCALAR_CONST_SET_OP(this):
                Memory.scalar[self.out_] = self.activation_data_

            def VECTOR_INNER_PRODUCT_OP(this):
                Memory.vector[self.out_] = np.dot(
                    Memory.vector[self.in1_], Memory.vector[self.in2_]
                )

            def SCALAR_DIFF_OP(this):
                Memory.scalar[self.out_] = (
                    Memory.scalar[self.in1_] - Memory.scalar[self.in2_]
                )

            def SCALAR_PRODUCT_OP(this):
                Memory.scalar[self.out_] = (
                    Memory.scalar[self.in1_] * Memory.scalar[self.in2_]
                )

            def SCALAR_VECTOR_PRODUCT_OP(this):
                Memory.vector[self.out_] = (
                    Memory.vector[self.in2_] * Memory.scalar[self.in1_]
                )

            def VECTOR_SUM_OP(this):
                Memory.vector[self.out_] = (
                    Memory.vector[self.in1_] + Memory.vector[self.in2_]
                )

        random_dict = RandomDict(config.OP)
        random_dict(self.op_)

    def toString(self):
        class RandomDict(Switch):
            def NO_OP(this):
                return "NO_OP"

            def SCALAR_CONST_SET_OP(this):
                return f"s{self.out_} = {self.activation_data_}"

            def VECTOR_INNER_PRODUCT_OP(this):
                return f"v{self.out_} = v{self.in1_} * v{self.in2_}"

            def SCALAR_DIFF_OP(this):
                return f"s{self.out_} = s{self.in1_} - s{self.in2_}"

            def SCALAR_PRODUCT_OP(this):
                return f"s{self.out_} = s{self.in1_} * s{self.in2_}"

            def SCALAR_VECTOR_PRODUCT_OP(this):
                return f"v{self.out_} = v{self.in2_} * s{self.in1_}"

            def VECTOR_SUM_OP(this):
                return f"v{self.out_} = v{self.in1_} + v{self.in2_}"

        random_dict = RandomDict(config.OP)
        return random_dict(self.op_)


NO_OP = Instruction()
