#!/usr/bin/env python
from random import choice, random

ALPHABET = 'abcdefghijklmnopqrstuvwxyz '
m_dict = {}

#def module_dict(seq):
#    module_string = seq.lower().split()
#    for item in module_string:
#        m_dict[item] = module_string.count(item)
#    print(m_dict)

#max_score = sum(m_dict.values())

#module_dict = {
#'nothing ':0,
#'in ':0,
#'biology ':0,
#'makes ':0,
#'sense ':0,
#'except ':0,
#'in ':0,
#'the ':0,
#'light ':0,
#'of ':0,
#'evolution':0
#}

def initialize(parent, num):
    """Returns num random sequences the length of parent."""
    return [[choice(ALPHABET) for i in range(len(parent))] for seq in range(num)]

def score(seq, target):
    """Returns number of differences between seq and target."""
    sum_score = 0
    for n in range(0,len(m_dict)):
        for i in range(0,len(seq)):
            if seq[i:len(list(m_dict)[n])+i-1] in list(m_dict):
                if list(m_dict.values())[n] > 1:
                    module_duplicate = seq.count(seq[i:len(list(m_dict)[n])])
                    if module_duplicate >= list(m_dict.values())[n]:
                        sum_score = sum_score + list(m_dict.values())[n]
                elif list(m_dict.values())[n] == 1:
                    sum_score = sum_score + list(m_dict.values())[n]
    return sum_score

def select(population, scores):
    """Returns best sequence and score from population."""
    scored = zip(scores, population)
    return sorted(scored, reverse=True)[0]

def breed(parent, num, mutation_rate):
    """Returns num copies of parent with mutation_rate changes per letter."""
    result = []
    length = len(parent)
    for seq in range(num):
        curr = parent[:]
        for pos in range(length):
            if random() <= mutation_rate: curr[pos] = choice(ALPHABET)
        result.append(curr)
    return result

def evolve(target, num=100, mutation_rate=0.01, generation=0):
    """Evolves random sequences towards seed, using ALPHABET."""
    module_string = target.lower().split()
    for item in module_string:
        m_dict[item] = module_string.count(item)
    print(list(m_dict))
    max_score = sum(m_dict.values())
    print("max score", max_score)
    population = initialize(target, num)
    while True:
        scores = [score(seq, target) for seq in population]
        best_score, best_seq = select(population, scores)
        print(generation, '\t', best_score, '\t', ''.join(best_seq))
        if best_score == max_score: break
        population = breed(best_seq, num, mutation_rate)
        generation += 1

evolve('nothing in biology makes sense except in the light of evolution')