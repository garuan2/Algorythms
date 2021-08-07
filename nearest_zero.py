# passed tests ID: 52304665


def nearest_zero(length, numbers):
    left_array, right_array = [], []
    counter = length - 1
    for item in numbers:
        if item == 0:
            counter = 0
        else:
            counter += 1
        left_array.append(counter)
    counter = length - 1
    for item in reversed(numbers):
        if item == 0:
            counter = 0
        else:
            counter += 1
        right_array.append(counter)
    right_array = right_array[::-1]
    range_to_zero = [
        min(left, right)
        for left, right in zip(left_array, right_array)
                     ]
    return range_to_zero


if __name__ == '__main__':
    a = int(input())
    b = list(int(x) for x in input().split())
    print(' '.join(map(str, nearest_zero(a, b))))
