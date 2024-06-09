immutable_var = 1, 4, True, [1,2,3]
print(immutable_var)
# immutable_var[0] = 5 кортеж относится к неизменяемым типам данных, такую операцию выполнить нельзя
immutable_var[3][0] = 5
print(immutable_var) #элементы кортежа могут быть изменяемыми, то есть список внутри изменить можно
mutable_list = [1,9,9,3,'Анастасия']
mutable_list[3] = 4
mutable_list[4] = 'Anastasiia'
print(mutable_list)