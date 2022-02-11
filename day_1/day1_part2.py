def count_increases_triples(input_file):
    """
    Counts the number of times the sequence of numbers increase in a given file
    :param input_file: text file containing a sequence of numbers separated by newlines
    :return: number of times the sequence increases
    """
    with open(input_file) as infile:
        raw_lines = infile.readlines()
        number_list = []
        for item in raw_lines:
            number_list.append(int(item[:-1]))
        increase_count = 0
        triple_list = []
        for number in range(len(number_list) - 2):
            triple_list.append(number_list[number]+number_list[number+1]+number_list[number+2])

        for number in range(len(triple_list) - 1):
            if triple_list[number + 1] > triple_list[number]:
                increase_count += 1
    return increase_count

if __name__ == "__main__":
    print(count_increases_triples("../day_2/input"))