def get_list_of_lines(filename):
    line_list = []
    with open(filename) as infile:
        raw_lines = infile.readlines()
    for item in raw_lines:
        line_list.append((item[:-1]))
    return line_list


def get_location_from_course_part1(command_list):
    depth = 0
    h_position = 0
    for command in command_list:
        direction = command.split(" ")[0]
        distance = int(command.split(" ")[1])
        print(direction,distance)
        if direction == "forward":
            h_position += distance
        elif direction == "down":
            depth += distance
        elif direction == "up":
            depth -= distance
    return depth, h_position


def get_location_from_course_part2(command_list):
    depth = 0
    h_position = 0
    aim = 0
    for command in command_list:
        direction = command.split(" ")[0]
        distance = int(command.split(" ")[1])
        if direction == "forward":
            h_position += distance
            depth += distance*aim
        elif direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance
    return depth, h_position


if __name__ == "__main__":
    command_list = get_list_of_lines("input")
    depth1, h_position1 = get_location_from_course_part1(command_list)
    print(depth1*h_position1)
    depth2, h_position2 = get_location_from_course_part2(command_list)
    print(depth2*h_position2)
