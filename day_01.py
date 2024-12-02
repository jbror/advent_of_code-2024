left_list = []
right_list = []
with open('input_day01.txt', 'r') as file:
    for line in file:
        numbers = line.split()
        left_num = int(numbers[0])
        right_num = int(numbers[1])
        left_list.append(left_num)
        right_list.append(right_num)

left_list_sorted = sorted(left_list)
right_list_sorted = sorted(right_list)

length_lists = len(left_list)
diff_list = 0 # keep track of the diff

for i in range (length_lists):
    diff_list += abs(right_list_sorted[i] - left_list_sorted[i])

print(diff_list)
