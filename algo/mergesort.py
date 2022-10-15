"""Mergesort prototype implementation in Python 3.7+.

Time complexity: O(n*logn).

Split an array on half, until the size of 1.
Merge two sorted sub-arrays through element-by-element comparison.
e.g. [1, 5], [3, 4]:
1 < 3 -> [1], 5 > 3 -> [1, 3], 5 > 4 -> [1, 3, 4], append remaining 5 -> [1, 3, 4, 5].
"""
from typing import Sequence


def mergesort(array: Sequence) -> Sequence:
    """Sorts array through mergesort algorithm."""
    if len(array) <= 1:
        return array

    halfsize = len(array) // 2
    left_part = array[halfsize:]
    right_part = array[:halfsize]

    left_sorted = mergesort(left_part)
    right_sorted = mergesort(right_part)

    return _merge(left_sorted, right_sorted)


def _merge(left_part: Sequence, right_part: Sequence) -> Sequence:
    merged = []
    while len(left_part) > 0 and len(right_part) > 0:
        # Merge two sorted sub-arrays through element-by-element comparison.
        if left_part[0] <= right_part[0]:
            merged.append(left_part.pop(0))
        else:
            merged.append(right_part.pop(0))

    # Add to the end of the sorted array remaining elements, if any.
    merged.extend(left_part)
    merged.extend(right_part)
    return merged


if __name__ == '__main__':
    import time
    PI = ('3.141592653589793238462643383279502884197169399375105820974944592307816406286'
          '208998628034825342117067982148086513282306647093844609550582231725359408128481'
          '117450284102701938521105559644622948954930381964428810975665933446128475648233'
          '786783165271201909145648566923460348610454326648213393607260249141273724587006'
          '606315588174881520920962829254091715364367892590360011330530548820466521384146'
          '951941511609433057270365759591953092186117381932611793105118548074462379962749')
    array_sample = [float(digit) for digit in PI.replace('.', '')]

    # Sort.
    timer_start = time.perf_counter()
    array_sorted = mergesort(array_sample)
    time_elapsed = time.perf_counter() - timer_start
    assert array_sorted == sorted(array_sample)
    print(f'Sorted array: {array_sorted}')
    print(f'Array of size {len(array_sample)} sorted in {time_elapsed:.6f}s.')

    # Sort using built-in function.
    timer_start = time.perf_counter()
    sorted(array_sample)
    time_elapsed = time.perf_counter() - timer_start
    print(f'Array of size {len(array_sample)} sorted using built-in sort in {time_elapsed:.6f}s.')

