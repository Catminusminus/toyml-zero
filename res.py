from algorithm import Algorithm
import config
import random
import pandas as pd
from sklearn.model_selection import train_test_split

# Regularized evolutionary search


class Chromosome:
    def __init__(self):
        self.algorithm = Algorithm()
        self.algorithm.randomize()

    def mutate(self):
        strategy = random.choice(list(range(3)))
        if strategy == 0:
            self.algorithm.mutateSetup()
            return
        if strategy == 1:
            self.algorithm.mutatePredict()
            return
        self.algorithm.mutateLearn()

    def evaluate(self, train_data, test_data):
        return self.algorithm.evaluate(train_data, test_data)


class Population:
    def __init__(
        self, P=config.config["population_size"], T=config.config["selection_size"]
    ):
        self.choromosomes = [Chromosome() for i in range(P)]
        self.T = T

    def mutate(self):
        self.choromosomes[-1].mutate()

    def copy(self, new):
        self.choromosomes.append(new)

    def remove(self, index):
        self.choromosomes.pop(index)

    def select(self, train_data, test_data):
        selected = random.sample(self.choromosomes, self.T)
        scores = [chromosome.evaluate(train_data, test_data) for hromosome in selected]

        print(f"best score: {np.max(scores)}")

        selected_index = np.argmax(scores)

        self.copy(selected(selected_index))
        self.remove(0)

    def generation(self, max_iteration, data):
        train_data, test_data = data
        for iteration in range(max_iteration):
            print(f"iteration: {iteration}")
            self.select(train_data, test_data)
            self.mutate()


class Data:
    def __init__(self, df):
        self.features = df.drop("label", axis=1)
        self.label = df["label"]


if __name__ == "__main__":
    population = Population()
    df = pd.read_csv("mnist_test.csv")
    train_df, test_df = train_test_split(df)
    train_data, test_data = Data(train_df), Data(test_df)

    population.generation(1000, (train_data, test_data))
