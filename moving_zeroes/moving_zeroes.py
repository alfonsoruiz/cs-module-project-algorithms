'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):

    for i, val in enumerate(arr):
        if val != 0:
            arr.insert(0, arr.pop(i))

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 0, 3, 2, 1]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
