my_dict={'sveta':2000,'katya':1989,'masha':1988}
print(my_dict)
print(my_dict.get('masha'))
print(my_dict.get('ksusha','Такого человечка нет'))
my_dict.update({'lenka':2006,
                 'inga':2001})
print(my_dict)
my_dict.pop('masha')
print(my_dict)

