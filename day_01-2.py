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
similarity_score = 0 # output goes here

print(left_list_sorted)


print(similarity_score)





#from p1 stuff
"""
for i in range (length_lists):
    diff_list += abs(right_list_sorted[i] - left_list_sorted[i])
"""
