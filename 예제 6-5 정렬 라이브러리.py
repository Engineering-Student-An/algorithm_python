array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# sorted() 함수
result = sorted(array)
print(result)

# sort() 내장함수
print(array)
array.sort()
print(array)

array = [('바나나', 2), ('사과', 5), ('당근', 3)]

# key 매개변수 활용

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)

array = [('바나나', 2), ('사과', 5), ('당근', 3)]

# key 매개변수 활용 (람다식)

result = sorted(array, key=lambda x: x[1])
print(result)
