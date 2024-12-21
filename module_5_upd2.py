from module_5_2 import House

def __len__(floor):
    floor = floor.number_floor
    return floor*3

House.__len__ = __len__ #Изменение метода класса House на функцию

h1 = House('ЖК Эльбрус', 15)
h2 = House('ЖК Акация', 27)
h3 = House('Орловский парк', 101)
# __str__
print(h1)
print(h2)
print(h3)
# __len__
text_len = 'Высота в метрах: '
print(text_len+str(len(h1)))
print(text_len+str(len(h2)))
print(text_len+str(len(h3)))