import numpy as np
import argparse


def binary_insert_sort(input_list):
    input_range = len(input_list)
    for sorted_index in range(input_range-1):
        insert = input_list[sorted_index+1]

        # binary search
        left = 0
        right = sorted_index
        while left < right:
            mid = int((left + right) / 2)
            if input_list[mid]< insert:
                left = mid + 1
            else:
                right = mid

        insert_index = left
        while insert_index <= sorted_index:
            if input_list[insert_index] > insert:
                break
            insert_index += 1

        for i in range(insert_index, sorted_index+2):
            stack = input_list[i]
            input_list[i] = insert
            insert = stack


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int, default=8)
    args = parser.parse_args()

    total_number = args.n

    bubble = np.random.randint(10, total_number*10, total_number)

    print('Before:{0}'.format(bubble))

    binary_insert_sort(bubble)

    print('After: {0}'.format(bubble))


if __name__ == '__main__':
    main()