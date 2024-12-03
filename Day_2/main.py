


def get_difference():
    left_side = []
    right_side = []
    diff_dict = {}
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
        if left_side[i] in right_side:
            diff_dict[left_side[i]] = []
            diff_dict[left_side[i]].append(right_side.count(left_side[i]))

    for num in diff_dict:
        total_difference.append(num * diff_dict[num][0])

    print(f'Answr is: {sum(total_difference)}')
        

get_difference()
