from class_House import House

def print_history():
    print('Дома записанные в историю: ' + ', '.join(House.houses_history))
s1 = House('ЖК Эльбрус', 10)
print_history()
s2 = House('ЖК Акация', 20)
print_history()
s3 = House('ЖК Матрёшки', 20)
print(s2==s3)
print(s1<s2)
House.go_to(s1,3)
print(s1==s3)
print(s3>s1)
print_history()

# Удаление объектов
del s2
del s3
print_history()