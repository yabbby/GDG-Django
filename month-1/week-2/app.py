#Function to sum number in a list
def sum_numbers(numbers):
    return sum(numbers)
#print even number between 1 and 20 using a loop
for number in range(1, 21):
    if number % 2 == 0:
        print(number)
#program to find the largest number in a list
def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest
