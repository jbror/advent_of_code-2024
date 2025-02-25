def is_increasing(lst):
  for i in range(1, len(lst)):
    if lst[i] < lst[i-1]:
      return False
  return True

def is_decreasing(lst):
  for i in range(1, len(lst)):
    if lst[i] > lst[i-1]:
      return False
  return True

def is_safe(levels):
    if not (is_increasing(levels) or is_decreasing(levels)):
        return False

    for i in range(1, len(levels)):
        diff = abs(levels[i] - levels[i - 1])
        if diff == 0 or diff > 3:
            return False

    return True

def is_safe_with_dampener(levels):
    if is_safe(levels):
        return True

    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i+1:]
        if is_safe(new_levels):
            return True

    return False

report_list = []
report_list_copy = []
with open('input_day02.txt', 'r') as file:
    for line in file:
        numbers = line.split()
        for n in numbers:
            int_n = int(n)
            report_list_copy.append(int_n)
        report_list.append(report_list_copy)
        report_list_copy = []

data_input = report_list


fooSafe = is_safe_with_dampener(data_input)

print(fooSafe)
safe_score = 0

for report in data_input:
    if is_safe_with_dampener(report):
        safe_score+=1

print(safe_score)
