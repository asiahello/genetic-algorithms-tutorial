from GeneticAlgorithm import GeneticAlgorithm, Element
from SelectionModels import elite_selection_model

from random import randint, choice

TARGET = 'Kocham Monike'


class Text(Element):

    POSSIBILITIES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890,.-;:_!"#%&/()=?@${[]}'''

    def __init__(self, text):
        self.text = text
        super().__init__()

    def _perform_mutation(self):
        """
        :return: mute text by replacing one letter with random one
        """
        random_index = randint(0, len(self.text)-1)
        text_as_list = list(self.text)
        text_as_list[random_index] = choice(self.POSSIBILITIES)
        self.text = "".join(text_as_list)

    def crossover(self, second_parent: 'Text') -> 'Text':
        """
        :param second_parent:
        :return:
        """
        crossing_point = randint(0, len(self.text)-1)
        new_text = self.text[:crossing_point] + second_parent.text[crossing_point:]
        return Text(new_text)

    def evaluate_function(self):
        """
        :return: number of different letters in a text in comparision to target
        """
        diff = 0
        for letter_1, letter_2 in zip(self.text, TARGET):
            if letter_1 != letter_2:
                diff += 1
        return diff

    def __repr__(self):
        return self.text


def stop_condition(string, current_fitness, i):
    """
    :param string:
    :param current_fitness:
    :param i:
    :return: True if there is no difference between string, otherwise false
    """
    return current_fitness == 0


def first_population_generator():
    """
    :return: 100 objects of Text with random strings with fixed length
    """
    return [Text("".join(choice(Text.POSSIBILITIES) for _ in range(len(TARGET)))) for _ in range(100)]


genetic_algorithm = GeneticAlgorithm(first_population_generator, elite_selection_model, stop_condition)
genetic_algorithm.run()
