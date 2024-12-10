import math


class Figure:
    sides_count = 0
    __sides = [] #(список сторон(целые числа)),
#    __color = [] #(список цветов в формате RGB)
    filled = False    # bool по условию, пусть пока будет False - не закрашен

    def __init__(self, color :tuple[int,int,int], *sides, filled):
        self.__color = color
        self.__sides = sides
        self.filled = False

    def get_color(self):   #возвращает список цветов
        return self.__color
    @staticmethod
    def __is_valid_color(self, r, g, b):
        if 0 < self.r < 255 and 0 < self.g <255 and 0 < self.b < 255:
            return True
        else:
            return False

    def  set_color(self, r, g, b):
        if self.__is_valid_color(r,g,b):
            self.__color = [self.r, self.g, self.b]

    @staticmethod
    def  __is_valid_sides(self, *args):
        #тут нужен списк [] внести в него все стороны из аргс? a=list(args) или прописать через фор наполнив список (append)
        for side in args:
            if side > 0 and type(side) == int and sides_count == len(args): #тут сравнить длинну списка с аргс == len(self.__sides)
                return True
            else:
                return False
    def get_sides(self):
        return self.__sides

#периметр это сумма всех сторон. есть функция sum для списков. вернет сумму всех сторон в нашем списке
    def __len__(self):
        return sum(self.__sides)
# я могу вызвать функцию внутри другой фонкции и передать в нее аргкменты первоц функции. внутренняя функция
# проделает прописанную в ней операцию,но уже с аргументами внешней функции __is_valid_sides дает True
# если кол-ва сторон совпадают, тогда если тру, то  ф-я set_sides поменят список на другие стороны
    def set_sides(self, *new_sides):
        if len(new_sides) == len(self.__sides):
            new_list = []
            for side in new_sides:
                if self.__is_valid_sides(side):
                    new_list.append(side)
            self.__sides = new_list
#*******************************************************************************************

class Circle(Figure):
    sides_count = 1

    def __init__(self, color: tuple[int, int, int], l, filled = False):
        super().__init__(color, l, filled = filled)
        self.__radius = l/(2*math.pi)

    def  get_square(self):
        return self.__radius ** 2 * math.pi

#    __radius = # длинну поделить на 2*пи
# для круга одна сторона, __sides[5] одна сторона длинной 5, как в площади? через get_sides по индексу вытащить сторону?
class Traingle(Figure):
    sides_count = 3

    def __init__(self, color: tuple[int, int, int], *sides, filled = False):
        super().__init__(color, *sides, filled = filled)


    def get_square(self):
        p = len(self) / 2
        #        p = sum(a+b+c)/2 #a b c это стороны. где их взять? из атрибута __sides[] по индексу? нет. не даст черзе ф-ю get _sides
        s = (p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])) ** 0.5  # она возвращает список
        return s

class Cube(Traingle):
    sides_count = 12

    def __init__(self, color:tuple[int, int, int], a):  #a примет на себя одно значение при создании куба(по условию передаем одну сторону)
        sides = [a] * self.sides_count  # размножит себя 12 раз и запишет в переменную sides
        super().__init__(color, *sides)   # метод родительского класса определяет значение __sides

    # def get_volume(self):
    #     v = a**3  #где взять эту сторону? сторона одна, __sides =[1]  тогда обратиться по индексу self.__sides[0] по инлексу?
    #     return v        # но я не внутри класса родителя у меня нет доступа но я могу получить доступ через метод родителя
    #                   # сторону возвращает get_sides значит взять ее по инлексу что ли? self.get_sides() []

circlel = Circle((200,200,100),10)
cubel = Cube((222,35,130),6)

#circlel.set_color(55, 66, 77) #выдает ошибку но не пойму почему аргумент b не видит везде есть
print(circlel.get_color())

#cubel.set_color(300,70,15)
print(cubel.get_color())

cubel.set_sides(5,3,12,4,5)
print(cubel.get_sides())
circlel.set_sides(15)
print(circlel.get_sides())

print(len(circlel))
print(cubel.get.volume())
