
# 입력
n = int(input())
array=[]
for i in range(n):
    array.append(int(input()))

# 출력
def print_result(arr):
    for i in range(n):
        print(arr[i], end=' ')
    print('')

# 정렬 라이브러리
sort_by_library = sorted(array, reverse=True)
print("정렬 라이브러리 : ", end='')
print_result(sort_by_library)


# 선택 정렬
selection_sort = array.copy()
for i in range(n):
    max_index = i
    for j in range(i+1, n):
        if selection_sort[max_index] < selection_sort[j]:
            max_index = j
    selection_sort[max_index], selection_sort[i] \
        = selection_sort[i], selection_sort[max_index]
print("선택 정렬 : ", end='')
print_result(selection_sort)


# 삽입 정렬
insertion_sort = array.copy()
for i in range(1,n):
    for j in range(i, 0, -1):
        if insertion_sort[j-1] < insertion_sort[j]:
            insertion_sort[j-1], insertion_sort[j] \
                = insertion_sort[j],insertion_sort[j-1]
print("삽입 정렬 : ",end='')
print_result(insertion_sort)

# 퀵 정렬
def quick(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    left_side = [x for x in tail if x>=pivot]
    right_side = [x for x in tail if x<pivot]

    return quick(left_side) + [pivot] + quick(right_side)

quick_sort = array.copy()
quick_sort = quick(quick_sort)
print("퀵 정렬 : ", end='')
print_result(quick_sort)

# 계수 정렬
count_sort = array.copy()
count = [0] * (max(count_sort)+1)
for i in count_sort:
    count[i]+=1
print("계수 정렬 : ", end='')
for i in range(len(count)-1,0,-1):
    if count[i]:
        for j in range(count[i]):
            print(i, end=' ')