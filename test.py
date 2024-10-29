def mssl(lst):
    if len(lst) == 0:
        return 0
    Max = max(lst[0], 0)
    curr = Max
    for num in lst[1:]:
        curr = num + curr * (curr >= 0)
        Max = max(Max, curr)
    return Max

def sublist(lst1, lst2):
    endOfLst = len(lst1) == 1
    target = 0
    for el in lst2:
        if el == lst1[target]:
            if endOfLst:
                return True
            else:
                target += 1
                endOfLst = target == (len(lst1) -1)
    return False

# Python program to Count Inversions in an array using merge sort

# This function merges two sorted subarrays arr[l..m] and arr[m+1..r] 
# and also counts inversions in the whole subarray arr[l..r]
def countAndMerge(arr, startLeft, endLeft, endRight):
  
    # Counts in two subarrays
    leftSize = endLeft - startLeft + 1
    rightSize = endRight - endLeft

    # Set up two lists for left and right halves
    leftHalf = arr[startLeft:endLeft + 1]
    rightHalf = arr[endLeft + 1:endRight + 1]

    # Initialize inversion count (or result)
    # and merge two halves
    inversionCount = 0
    leftIndex = 0
    rightIndex = 0
    #We use that variable to modify the array on the spot
    index = startLeft
    while leftIndex < leftSize and rightIndex < rightSize:

        # No increment in inversion count
        # if left[] has a smaller or equal element
        if leftHalf[leftIndex] <= rightHalf[rightIndex]:
            arr[index] = leftHalf[leftIndex]
            leftIndex += 1
        else:
            #if the right element is smaller, then that means its concurrent left element was misplaced and so were all elements to its right 
            arr[index] = rightHalf[rightIndex]
            rightIndex += 1
            inversionCount += (leftSize - leftIndex)
        index += 1

    # Merge remaining elements
    while leftIndex < leftSize:
        arr[index] = leftHalf[leftIndex]
        leftIndex += 1
        index += 1
    while rightIndex < rightSize:
        arr[index] = rightHalf[rightIndex]
        rightIndex += 1
        index += 1

    return inversionCount

# Function to count inversions in the array
def countInversions(arr, left, right):
    totalInversions = 0
    if left < right:
        mid = (right + left) // 2

        # Recursively count inversions in the left and right halves
        totalInversions += countInversions(arr, left, mid)
        totalInversions += countInversions(arr, mid + 1, right)

        # Count inversions where greater element is in the left half
        # and smaller in the right half
        totalInversions += countAndMerge(arr, left, mid, right)
    return totalInversions

def inversionCount(arr):
    if type(arr) == str:
        arr = list(arr)
    return countInversions(arr, 0, len(arr) - 1)
def mystery(n, div = 0):
    if n <= 1:
        return div
    else:
        return mystery(n // 2, div + 1)

def twosumforthreesum(lst, target):
    target_map = {}
    for i, val in enumerate(lst):
        if val in target_map:
            return [target_map[val], i]
        else:
            target_map[target - val] = i
    return []
def twosum(lst, target):
    target_map = {}
    result = []
    for i, val in enumerate(lst):
        if val in target_map:
            result.append([target_map[val], i])
        else:
            target_map[target - val] = i
    return result

def threesum(lst, target):
    for i in lst:
        if twosumforthreesum(lst, target - i):
            return True
    return False

def lastfirst(nameshamble):
    first_names = []
    last_names = []
    for i in range(len(nameshamble)):
        name = nameshamble[i].split(',')
        first_names.append(name[1].strip())
        last_names.append(name[0].strip())
    return [first_names, last_names]

def pair(lst1, lst2, target):
    wanted_map = {}
    i = 0
    resul = []
    while i < len(lst1) :
        wanted_map[target - lst1[i]] = lst1[i]
        i += 1
    for j in range(len(lst2)):
        if lst2[j] in wanted_map:
            resul.append([wanted_map[lst2[j]], lst2[j]])
    return resul

def intersect(lst1, lst2):
    target_map = {}
    for i in lst1:
        target_map[i] = True
    result = []
    for i in lst2:
        if i in target_map:
            result.append(i)
    return result

def in_both(lst1, lst2):
    target_map = {}
    for i in lst1:
        target_map[i] = True
    result = []
    for i in lst2:
        if i in target_map:
            return True
    return False

def four_letter(lst):
    return [x for x in lst if len(x) == 4]

def doubles(lst):
    if len(lst) < 2:
        return []
    return [lst[i] for i in range(len(lst))[1:] if lst[i] == 2*(lst[i-1])]

def indexes(word, char):
    return [i for i in range(len(word)) if word[i] == char]

str1 = 'ABBFHDL'
str2 = 'DCBA'

print(mssl([4,-2,-8,5, -2, 7, 7, 2, -6, 5]))
print(mssl([3,4,5]))
print(mssl([-2, -3, -5]))
print("MAXIMUM SUM SUB STRING\n\n")
print(sublist([15, 1, 100], [20, 15, 30, 50, 1, 100]))
print(sublist([15, 50, 20], [20, 15, 30, 50, 1, 100]))
print("SUB LIST\n\n")
print(inversionCount(str1))
print(inversionCount(str2))
print("INVERSIONS\n\n")
print(mystery(4))
print(mystery(11))
print(mystery(25))
print("MYSTERY\n\n")
print(threesum([5, 4, 10, 20, 15, 19], 39))
print(threesum([5, 4, 10, 20, 15, 19], 10))
print("THREESUM\n\n")
print(lastfirst(['Gerber, Len', 'Fox, Kate', 'Dunn, Bob']))
print("LASTFIRST\n\n")
print(twosum([7,8,5,3,4,6], 11))
print("TWOSUM\n\n")
print(pair([2,3,4], [5,7,9,12], 9))
print("PAIR\n\n")
print(intersect([3, 5, 1, 7, 9], [4, 2, 6, 3, 9]))
print("INTERSECT\n\n")
print(in_both([3,2, 5, 4, 7], [9, 0, 1, 3]))
print("INBOTH\n\n")
print(four_letter(['dog', 'letter', 'stop', 'door', 'bus', 'dust']))
print("FOUR_LETTER\n\n")
print(doubles([3, 0, 1, 2, 3, 6, 2, 4, 5, 6, 5]))
print("DOUBLES\n\n")
print(indexes('mississipi', 's'))
print(indexes('mississipi', 'i'))
print(indexes('mississipi', 'a'))
print("INDEXES")