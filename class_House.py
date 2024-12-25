class House: #Создание класса дом
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_floor):
        self.name = name
        self.number_floor = number_floor

    def __len__(self): #Специальный метод определения длины дома - это количество этажей
        return self.number_floor

    def end_floor_rp(self, number):  # Метод для определения окончания слова "этаж" родительный падеж
        if number % 10 > 4 or number in range(10, 21) or number % 10 == 0:
            return 'этажей'
        elif number % 10 in range(2, 5):
            return 'этажа'
        else:
            return 'этаж'

    def end_floor_rp(self, number):  # Метод для определения окончания слова "этаж" 
        if number % 10 > 4 or number in range(10, 21) or number % 10 == 0:
            return 'этажей'
        elif number % 10 in range(2, 5):
            return 'этажа'
        else:
            return 'этаж'

    def met_world_operations(self, other, operations): #Метод результата сравнения
        operations_dict = {'=':' равно ','!=':' не равно ', '<':' меньше ', '<=':' меньше или равно ', '>':' больше ', '>=':' больше или равно ',}
        if isinstance(other, House):
            return f'{self.number_floor} {self.end_floor_rp(self.number_floor)} {self.name}'+operations_dict[operations]+f'{other.number_floor} {self.end_floor_rp(other.number_floor)} {other.name}.'
        elif isinstance(other, int):
            return f'{self.number_floor} {self.end_floor_rp(self.number_floor)} {self.name}' + operations_dict[operations] + f'{other} {self.end_floor_rp(other)}.'

    def __eq__(self, other):
        if isinstance(other, House):
            if self.number_floor == other.number_floor:
                return self.met_world_operations(other,operations='=')
            else:
                return self.met_world_operations(other,operations='!=')
        elif isinstance(other, int):
            if self.number_floor == other:
                return self.met_world_operations(other, operations='=')
            else:
                return self.met_world_operations(other, operations='!=')

    def __lt__(self, other):
        if isinstance(other, House):
            if self.number_floor < other.number_floor:
                return self.met_world_operations(other, operations='<')
            else:
                return False
        elif isinstance(other, int):
            if self.number_floor < other:
                return self.met_world_operations(other, operations='<')
            else:
                return False

    def __le__(self, other):
        if isinstance(other, House):
            if self.number_floor <= other.number_floor:
                return self.met_world_operations(other, operations='<=')
            else:
                return False
        elif isinstance(other, int):
            if self.number_floor <= other:
                return self.met_world_operations(other, operations='<=')
            else:
                return False

    def __gt__(self, other):
        if isinstance(other, House):
            if self.number_floor > other.number_floor:
                return self.met_world_operations(other, operations='>')
            else:
                return False
        elif isinstance(other, int):
            if self.number_floor <= other:
                return self.met_world_operations(other, operations='>')
            else:
                return False

    def __ge__(self, other):
        if isinstance(other, House):
            if self.number_floor >= other.number_floor:
                return self.met_world_operations(other, operations='>=')
            else:
                return False
        elif isinstance(other, int):
            if self.number_floor <= other:
                return self.met_world_operations(other, operations='>=')
            else:
                return False

    def __ne__(self, other):
        if isinstance(other, House):
            if self.number_floor != other.number_floor:
                return self.met_world_operations(other, operations='!=')
            else:
                return False
        elif isinstance(other, int):
            if self.number_floor != other:
                return self.met_world_operations(other, operations='!=')
            else:
                return False

    def __add__(self, value):
        #if isinstance(value, int):
         self.number_floor += value
         return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __sub__(self, value):
        if isinstance(value, int):
            self.number_floor -= value
            return self

    def __rsub__(self, value):
        if isinstance(value, int):
            self.number_floor = value - self.number_floor
            return self

    def __isub__(self, value):
        return self.__sub__(value)

    def __mul__(self, value):
        if isinstance(value, int):
            self.number_floor *= value
            return self

    def __rmul__(self, value):
        return self.__mul__(value)

    def __imul__(self, value):
        return self.__mul__(value)

    def __truediv__(self, value):
        if isinstance(value, int):
            self.number_floor = self.number_floor / value
            self.number_floor = int(self.number_floor)
            return self

    def __itruediv__(self, value):
        return self.__truediv__(value)

    def __rtruediv__(self, value):
        if isinstance(value, int):
            self.number_floor = value / self.number_floor
            self.number_floor = int(self.number_floor)
            return self

    def __str__(self): #Специальный метод str - возвращает сведения о доме
        return f'Название: {self.name}, в здании: {self.number_floor} {self.end_floor_rp(self.number_floor)}'

    def __del__(self):

        print(f'{self.name} снесён, но он останется в истории')

    def go_to (self, new_floor): # Метод выводит каждый этаж до которого нужно приехать включительно, если этаж <1 или больше, чем в доме, выводит строку об отсутствии этажа
        if new_floor <= self.number_floor and new_floor > 0:
            for i in range(1, new_floor+1):
                print (str(i)+' этаж')
        else:
            print(f'{new_floor} - такого этажа не существует в "{self.name}", в нем {self.number_floor} {self.end_floor_rp(self.number_floor)}')
