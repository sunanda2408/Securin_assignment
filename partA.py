def main():
    # Define Die A and Die B
    die_a = [1, 2, 3, 4, 5, 6]
    die_b = [1, 2, 3, 4, 5, 6]

    total_combinations = len(die_a) * len(die_b)
    print("Total combinations:", total_combinations)

    combinations = []
    sum_count = [0] * 11  # Initialize the sum_count list for sums from 2 to 12

    # calculate sum count
    for i in range(len(die_a)):
        row = []
        for j in range(len(die_b)):
            combination = (die_a[i], die_b[j])
            row.append(combination)
            _sum = die_a[i] + die_b[j]
            sum_count[_sum - 2] += 1  # Adjust the index to start from 0
        combinations.append(row)

    # Display the 6x6 matrix of combinations
    print("\nMatrix of combinations:")
    for row in combinations:
        for combination in row:
            print("({}, {}) ".format(combination[0], combination[1]), end="")
        print()

    # Display probabilities for each sum
    print("\nProbability of each sum:")
    for i in range(2, 13):
        probability = sum_count[i - 2] / total_combinations  # Adjust the index to start from 0
        print("P(Sum = {}) = {}/36 = {:.2f}".format(i, sum_count[i - 2], probability))


if __name__ == "__main__":
    main()
