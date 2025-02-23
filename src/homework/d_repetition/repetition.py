def get_factorial(num):
    "Returns the factorial of a given number using a for loop."
    result = 1 
    for i in range(1, num + 1):
        result *= i
    return result

def sum_odd_numbers(num):
    "Returns the sum of odd numbers up to the given number using a while loop."
    total = 0 
    i = 1
    while i <= num:
        total += i 
        i += 2
    return total 

#Test cases 
if __name__ == "__main__":
    #Testing get_factorial function
    assert get_factorial(5) == 120, "Error in get_factorial function"
    assert get_factorial(0) == 1, "Error in get_factorial function"
    assert get_factorial(1) == 1, "Error in get_factorial function"

    #Testing sum_odd_numbers function
    assert sum_odd_numbers(10) == 25, "Error in sum_odd_numbers function"
    assert sum_odd_numbers(1) == 1, "Error in sum_odd_numbers function"
    assert sum_odd_numbers(0) == 0, "Error in sum_odd_numbers function"

    print("All test passed!") 