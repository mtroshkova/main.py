immutable_var=(['food','music'],13,['lady'])
print ("Вот такой 'Кортеж':", immutable_var)
print(type(immutable_var))
immutable_var[1] = 2 #не поддерживает обращение по элементам?
print('вот такой кортеж не поддерживает обращение по элементам')
mutable_list = ['не очень', 'просто', 'мне','дается','обучение',2, 7]
mutable_list[0] = 'ОЧЕНЬ'
mutable_list[-1]='!'
mutable_list[-2]='!'
print (mutable_list)
