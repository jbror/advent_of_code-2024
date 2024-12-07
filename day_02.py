data_input = [
[7,6,4,2,1],
[1,2,7,8,9],
[9,7,6,2,1],
[1,3,2,4,5],
[8,6,4,4,1],
[1,3,6,7,9]
]

report_list2 = []
report_list = []
with open('input_test_day02.txt', 'r') as file:
    for line in file:
        numbers = line.split()
        for n in numbers:
            int_n = int(n)
            report_list2.append(int_n)
            print(report_list2)
        report_list.append(report_list2)
        report_list2 = []

            #print(int_n)
            #print(type(int_n))
        #print(numbers)
        #level_num = int(numbers)
        #report_list.append(level_num)
        #print(report_list)

print(report_list)
data_input = report_list

for l in data_input:
    my_list = l
    is_increasing = True
    is_decreasing = True

    for i in range(1, len(my_list)):
        #print(is_increasing, is_decreasing)
        if my_list[i] == my_list[i-1]:
            is_decreasing = False
            is_increasing = False
            break
        elif my_list[i] > my_list[i-1]:
            is_decreasing = False
        elif my_list[i] < my_list[i-1]:
            is_increasing = False

        if not is_increasing and not is_decreasing:
            break

    # this checks if the code increases or decrease by maximum of 3
        if abs(my_list[i] - my_list[i-1]) > 3:
            is_decreasing = False
            is_increasing = False
            is_safe = False # not needed but i'm keeping this to make it clear!
            break


    if is_increasing or is_decreasing:
        print("very safe")
    else:
        print("Not safe, next Chernobyl INC!")
