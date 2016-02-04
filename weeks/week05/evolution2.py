#!/usr/bin/env python
from random import choice, random, randint

ALPHABET = 'abcdefghijklmnopqrstuvwxyz '
m_dict = {}

def initialize(parent, num):
    """Returns num random sequences the length of parent."""
    return [[choice(ALPHABET) for i in range(len(parent))] for seq in range(num)]

def score(seq, target):
    """Returns number of differences between seq and target."""
    #return sum(map(int, [a != b for a, b in zip(seq, target)]))
    score_sum=0
    for n in range(0,len(m_dict)):
        i = len(list(m_dict)[n])
        x = list(m_dict.values())[n]
        substring = ''.join(seq[x:x+i])
        #for x in range(0, len(seq)-i):#, len(list(m_dict)[n])):
        #    substring = ''.join(seq[x:x+i])
        #    seq = ''.join(seq)
        #    if seq[x:x+i] != list(m_dict)[n]:
        #        score_sum=score_sum+1
        if substring != list(m_dict)[n]:
            score_sum=score_sum+1
        #    else:
                #print(substring)
                #print(seq.count(substring))
                #if seq.count(substring) > list(m_dict.values())[n]:
                #    score_sum=score_sum+1
                #else:
                #    score_sum=score_sum
    return score_sum

def select(population, scores):
    """Returns best sequence and score from population."""
    scored = zip(scores, population)
    lowest_score = sorted(scores, reverse=False)[0]
    number_of_same_best_scores = scores.count(lowest_score)
    rand_index = randint(0,number_of_same_best_scores-1)
    #print(number_of_same_best_scores)
    return sorted(scored, reverse=False)[rand_index]

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

def evolve(target, num=1000, mutation_rate=0.75, generation=0):
    """Evolves random sequences towards seed, using ALPHABET."""
    population = initialize(target, num)
    #target = target.replace(" ", ", ")
    #module_string = target.lower().split(',')
    module_string = target.lower().split()
    for item in module_string:
        m_dict[item] = target.find(item)
    print(m_dict)
    while 1:
        scores = [score(seq, target) for seq in population]
        best_score, best_seq = select(population, scores)
        print(generation, '\t', best_score, '\t', ''.join(best_seq))
        if best_seq == target: break
        population = breed(best_seq, num, mutation_rate)
        generation += 1

evolve('nothing in biology makes sense except in the light of evolution')