
n=int(input())
dir_list = list(input().split())

index_i = index_j = 1

for i in dir_list:
    if i == 'L' and index_j>1 : index_j-=1
    elif i == 'R' and index_j<n : index_j+=1
    elif i == 'U' and index_i>1 : index_i-=1
    elif i == 'D' and index_i<n : index_i+=1

print(index_i, index_j)
