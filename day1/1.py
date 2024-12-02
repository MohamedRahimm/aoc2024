# part 1
with open('input.txt', 'r') as file:
    content = file.read().split("\n")

clean_str = [i.split(" ") for i in content]
left_list = sorted([clean_str[i][0] for i in range(len(clean_str))])
right_list = sorted([clean_str[i][-1] for i in range(len(clean_str))])
total = 0
for i in range(len(right_list)):
    total += abs(int(left_list[i]) - int(right_list[i]))
print(total)

# part 2
num_map = {num: 0 for num in left_list}
for num in right_list:
    if num in num_map:
        num_map[num] += 1
out = sum(int(key)*val for key, val in num_map.items())
print(out)
