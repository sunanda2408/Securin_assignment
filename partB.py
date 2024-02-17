def generate_combinations_die_A(list, length):
    if length == 0:
        return [[]]
    combinations = []
    for element in list:
        sub_combinations = generate_combinations_die_A(list, length - 1)
        for sub_comb in sub_combinations:
            combinations.append([element] + sub_comb)
    return combinations

def generate_combinations_die_B(list, length, start):
    if length == 0:
        return [[]]
    combinations = []
    for i in range(start, len(list)):
        sub_combinations = generate_combinations_die_B(list, length - 1, i + 1)
        for sub_comb in sub_combinations:
            combinations.append([list[i]] + sub_comb)
    return combinations

def calculate_probability_sum(arr1, arr2):
    psum = [0.0] * 12
    for i in arr1:
        for j in arr2:
            k = i + j
            psum[k - 1] += 1
    for i in range(len(psum)):
        if psum[i] != 0:
            psum[i] /= 36
    return psum
def find_transformed_dice(die_A, die_B):
    list1 = [1, 2, 3, 4]
    length = 6
    combos1 = generate_combinations_die_A(list1, length)

    list2 = [1, 2, 3, 4, 5, 6, 7, 8]
    start = 0
    combos2 = generate_combinations_die_B(list2, length, start)

    psum = [0.0, 1.0 / 36, 2.0 / 36, 3.0 / 36, 4.0 / 36, 5.0 / 36, 6.0 / 36, 5.0 / 36, 4.0 / 36, 3.0 / 36, 2.0 / 36, 1.0 / 36]

    for i in combos1:
        for j in combos2:
            if calculate_probability_sum(i, j) == psum:
                print("New Die A:", i)
                print("New Die B:", j)
                return

if __name__ == "__main__":
    die_A = [1, 2, 3, 4, 5, 6]
    die_B = [1, 2, 3, 4, 5, 6]
    find_transformed_dice(die_A, die_B)
