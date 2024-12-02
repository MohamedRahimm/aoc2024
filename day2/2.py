# reports = row
# levels = col

with open("input.txt", "r") as file:
    content = file.read().splitlines()


# part 1
def is_valid(arr):
    is_sorted = arr == sorted(arr) or arr == sorted(arr, reverse=True)
    for i in range(len(arr)-1):
        if not 1 <= abs(arr[i]-arr[i+1]) <= 3:
            return 0
    return int(is_sorted)


reports = [list(map(int, line.split())) for line in content]
p1 = sum([is_valid(i) for i in reports])
print(p1)


# part 2
p2 = 0
for report in reports:
    for j in range(len(report)):
        if (is_valid(report[:j]+report[j+1:])):
            p2 += 1
            break
print(p2)
