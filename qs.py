#!/bin/python
def partition(ar):
    left, pivot, right = [], [], []
    pivot.append(ar[0])
    
    for i in range(1, len(ar)):
        if ar[i] >= pivot[0]:
            right.append(ar[i])
        else:
            left.append(ar[i])
    return left, pivot, right

def quick_sort(ar):
    print ar
    left, pivot, right = partition(ar)
    if len(left) > 1:
        left = quick_sort(left)
    if len(right) > 1:
        right = quick_sort(right)
    return left + pivot + right

m = input()
ar = [int(i) for i in raw_input().strip().split()]
qr = quick_sort(ar)
print qr
