with open("input.txt", "r") as file:
    content = file.read().strip()

# didn't want to use regex


def is_valid(arr):
    total = 0
    toggle = True
    for i in range(len(arr)):
        num1 = ""
        num2 = ""
        # p2 logic
        if (arr[i:i+4] == "do()"):
            toggle = True
        if (arr[i:i+7] == "don't()"):
            toggle = False
        # added toggle == True for p2
        if (arr[i:i+4] == "mul(" and toggle == True):
            j = i+4
            comma = False
            while (j < len(arr)):
                if (num1 != "" and num2 != "" and arr[j] == ")"):
                    total += int(num1)*int(num2)
                    break
                elif (arr[j] == "," and num1 != ""):
                    comma = True
                    j += 1
                try:
                    int(arr[j])
                except:
                    break
                if (comma == False):
                    num1 += arr[j]
                else:
                    num2 += arr[j]
                j += 1
    return total


print(is_valid(content))
