print('Введите числа через пробел')
numbers = list(map(int, input().split()))
averg=sum(numbers)/ len(numbers)
print('Среднее арифметическое:', averg)