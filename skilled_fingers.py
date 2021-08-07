# passed tests ID:52308927

import collections


def skilled_fingers(fingers, matrix):
    k = 2 * fingers
    input_data = list(map(int, matrix.replace(' ', '').replace('.', '')))
    counted_data = collections.Counter(input_data)
    result = 0
    for value in counted_data.values():
        if value <= k:
            result += 1
    return result


if __name__ == '__main__':
    keys = int(input())
    data = []
    for i in range(4):
        data.append(input())
    data = ''.join(data)
    print(skilled_fingers(keys, data))
