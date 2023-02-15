from operator import index


numbers = [5, 3, 0, 12, 22, 10, 55]             # create a list

def sum_recursion(numbers, index):             # this defines what your recursion is going to do
    if index == 0:
        return numbers[index]

    if index < len(numbers):
        return numbers[index] + sum_recursion(numbers, index - 1)
    else:
        print("Number of index was not found")

index = int(input("Enter index number: "))        # ask the user to enter an index

print(f"The sum is {sum_recursion(numbers, index)}")          # print the results