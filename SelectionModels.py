def elite_selection_model(generation, best_threshold=0.1):
    """
    :param best_threshold:
    :param generation:
    :return:
    """
    number_of_selected = int(len(generation) * best_threshold)
    sorted_by_assess = sorted(generation, key=lambda x: x.fitness)
    return sorted_by_assess[:number_of_selected]


def cup_selction_model(generation, best_threshold=0.1):
    """
    :param best_threshold:
    :param generation:
    :return:
    """
    number_of_selected = int(len(generation) * best_threshold)
    return generation


def roulette_selection_model(generation, best_threshold=0.1):
    """
    :param best_threshold:
    :param generation:
    :return:
    """
    number_of_selected = int(len(generation) * best_threshold)
    return generation