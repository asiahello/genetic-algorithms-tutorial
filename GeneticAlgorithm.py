from abc import abstractmethod, ABC
from random import choice, random


class Element(ABC):

    @abstractmethod
    def __init__(self):
        self.fitness = self.evaluate_function()

    def mutation(self):
        self._perform_mutation()
        self.fitness = self.evaluate_function()

    @abstractmethod
    def _perform_mutation(self):
        """ implements how Element mutates """
        pass

    @abstractmethod
    def crossover(self, element2: 'Element') -> 'Element':
        """ implements how Element crossovers"""
        pass

    @abstractmethod
    def evaluate_function(self):
        """ evaluation of the Element """
        pass


class GeneticAlgorithm:

    def __init__(self, first_population_generator: callable, selection_model: callable, stop_condition: callable,
                 mutation_probability: float = 0.1):
        """
        :param first_population_generator: method to generate the first population
        :param selection_model: method to choose best elements from population
        :param stop_condition:
        :param mutation_probability:
        """
        self.generate_first_population = first_population_generator
        self.select_best_elements = selection_model
        self.stop_condition = stop_condition
        self.mutation_probability = mutation_probability

    def run(self):
        population = self.generate_first_population()
        population.sort(key=lambda x: x.fitness)
        population_length = len(population)

        i = 0
        while True:
            selected = self.select_best_elements(population)
            new_population = selected.copy()

            while len(new_population) != population_length:
                parent_1 = choice(population)
                parent_2 = choice(population)
                child = parent_1.crossover(parent_2)
                child.mutation() if random() <= self.mutation_probability else None
                new_population.append(child)

            population = new_population
            the_best_match = min(population, key=lambda x: x.fitness)
            print("Generation: {} S: {} fitness: {}".format(i, the_best_match, the_best_match.fitness))

            if self.stop_condition(the_best_match, the_best_match.fitness, i):
                break
            else:
                i += 1
