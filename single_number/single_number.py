'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    for i in arr:
        matches = 0
        for j in arr:
            if i == j:
                matches += 1
        print(f"{i} matched {matches} times")
        if matches == 1:
            return i
            


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")