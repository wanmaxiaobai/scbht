from itertools import combinations

# def stringconcate(lst):
#     all_combinations = []
#     for r in range(1, len(lst) + 1):
#         combinations_r = combinations(lst, r)
#         for comb in combinations_r:
#             all_combinations.append(" anD ".join(map(str, comb)))
#     return all_combinations
#
# from itertools import combinations, chain

# def stringconcate(lst, n):
#     all_combinations = []
#     for r in range(1, min(len(lst) + 1, n + 1) if n is not None else len(lst) + 1):
#         combinations_r = combinations(lst, r)
#         for comb in combinations_r:
#             all_combinations.append(" and ".join(map(str, comb)))
#     return all_combinations


def stringconcate(lst, m, n):
    all_combinations = []
    for r in range(m, min(len(lst) + 1, n + 1) if n is not None else len(lst) + 1):
        combinations_r = combinations(lst, r)
        for comb in combinations_r:
            all_combinations.append(" and ".join(map(str, comb)))
    return all_combinations

