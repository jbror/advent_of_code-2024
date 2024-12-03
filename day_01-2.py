left_list = []
right_list = []
with open('input_day01.txt', 'r') as file:
    for line in file:
        numbers = line.split()
        left_num = int(numbers[0])
        right_num = int(numbers[1])
        left_list.append(left_num)
        right_list.append(right_num)

count = 0
similarity_score = 0
for i in left_list:
    count = right_list.count(i)
    similarity_score += count * i
    print(similarity_score)
