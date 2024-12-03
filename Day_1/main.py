


def get_difference():
    left_side = []
    right_side = []
    total_difference = []
    with open("./input.txt", 'r') as file:

        for line in file:
            split_line = line.strip().split('  ');
            print(split_line)
            left_side.append(int(split_line[0]))
            right_side.append(int(split_line[1]))
    

    left_side.sort()
    right_side.sort()
    for i in range(len(left_side)):
        total_difference.append(abs(left_side[i] - right_side[i]))

    print(f'Answr is: {sum(total_difference)}')
        

get_difference()
