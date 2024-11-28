my_dict={'sveta':2000,'katya':1989,'masha':1988}
print(my_dict)
print(my_dict.get('masha'))
print(my_dict.get('ksusha','Такого человечка нет'))
my_dict.update({'lenka':2006,
                 'inga':2001})
print(my_dict)
my_dict.pop('masha')
print(my_dict)

my_set={13,2,'perm',14,2,'svet'}
print(my_set)
my_set.add(86)
my_set.add(6)
print(my_set)
my_set.discard(13)
print(my_set)
