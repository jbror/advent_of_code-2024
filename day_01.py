left_list = [88276,66898,58877,69396,53434,69841]
right_list = [66757,13714,87487,12997,62485,67231]


left_list_sorted = sorted(left_list)
right_list_sorted = sorted(right_list)

length_lists = len(left_list)
diff_list = 0 # här håller jag koll på "avståndet" för varje nummer

for i in range (length_lists):
    print(right_list_sorted[i] - left_list_sorted[i])
    diff_list += abs(right_list_sorted[i] - left_list_sorted[i])
    print(diff_list)

print(left_list_sorted)
print(right_list_sorted)


#test from input
#left_list = [3,4,2,1,3,3]
#right_list = [4,3,5,3,9,3]

"""
88276   66757
66898   13714
58877   87487
69396   12997
53434   62485
69841   67231
51135   99904
75350   18379
"""
