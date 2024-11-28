first=int(input('Введите первое число: '))

second=int(input('Введите второе число: '))

third=int(input('Введите третье число: '))

if first==second and first==third:
    print('3 числа равны')
elif first==second or first==third or second==third:
    print('2 числа равны')
else:
    print('нет равных чисел((')
