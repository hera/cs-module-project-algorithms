'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    num_zeroes = 0
    result = []

    for i in arr:
        if i != 0:
            result.append(i)
        else:
            num_zeroes += 1
    
    for j in range(num_zeroes):
        result.append(0)
    
    return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")