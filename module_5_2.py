def end_floor(number): # Функция для определения окончания слова "этаж"
    if number % 10 > 4  or number in range(10, 21) or number % 10 == 0:
        return 'этажей'
    elif number % 10 in range(2, 5):
        return 'этажа'
    else:
        return 'этаж'


class House: #Создание класса дом
    def __init__(self, name, number_floor):
        self.name = name
        self.number_floor = number_floor

    def __len__(self): #Магический метод определения длины дома - это количество этажей
        return self.number_floor

    def __str__(self): #Магический метод str - возвращает сведения о доме
        return f'Название: {self.name}, в здании: {self.number_floor} {end_floor(self.number_floor)}'


    def go_to (self, new_floor): # Метод выводит каждый этаж до которого нужно приехать включительно, если этаж <1 или больше, чем в доме, выводит строку об отсутствии этажа
        if new_floor <= self.number_floor and new_floor > 0:
            for i in range(1, new_floor+1):
                print (str(i)+' этаж')
        else:
            print(f'{new_floor} - такого этажа не существует в "{self.name}", в нем {self.number_floor} {end_floor(self.number_floor)}')

#Основная программа
h1 = House('ЖК Эльбрус', 11)
h2 = House('ЖК Акация', 22)
# __str__
print(h1)
print(h2)
# __len__
print(len(h1))
print(len(h2))