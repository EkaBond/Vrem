class Figure:
    sides_count = 0
    __sides = [] #(список сторон(целые числа)),
    __color = [] #(список цветов в формате RGB)
    filled = False    # bool по условию, пусть пока будет False - не закрашен

    def __init__(self, color, *sides):
        self.__color = color
        self.__sides = sides

    def get_color(self):   #возвращает список цветов
        return self.__color

    def __is_valid_color(self, r: int, g: int, b: int):  #или лучше прописать внутри ф-ии что они целые r=int(r) или int(self.r)
        if 0 < self.r < 255 and 0 < self.g <255 and 0 < self.b < 255:
            return True
        else:
            return False

    def  set_color(self, r, g, b):
        if self.__is_valid_color(r,g,b) == True:
            self.__color = [self.r, self.g, self.b]

    def  __is_valid_sides(self, *args):
        #тут нужен списк [] внести в него все стороны из аргс? a=list(args) или прописать через фор наполнив список (append)
        for side in self.__sides:
            if side > 0 and type(side) == int and #тут сравнить длинну списка с аргс == len(self.__sides)
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
    def (self, *new_sides):
        if self.__is_valid_sides(*new_sides) == True:
            self.__sides = list(new_sides)

#*******************************************************************************************

class Circle(Figure):
    sides_count = 1
    __radius = # длинну поделить на 2*пи
# для круга одна сторона, __sides[5] одна сторона длинной 5, как в площади? через get_sides по индексу вытащить сторону?
class Traingle(Figure):
    sides_count = 3

    def get_square(self):
        p = sum(a+b+c)/2 #a b c это стороны. где их взять? из атрибута __sides[] по индексу? нет. не даст черзе ф-ю get _sides
        s = (p*(p-a)*(p-b)(p-c))**0.5                    # она возвращает список
        return s

class Cube(Traingle):
    sides_count = 12

    def __init__(self, color, a):  #a примет на себя одно значение при создании куба(по условию передаем одну сторону)
        sides = [a] * self.sides_count  # размножит себя 12 раз и запишет в переменную sides
        super.__init__(color, *sides)   # метод родительского класса определяет значение __sides

    def get_volume(self):
        v = стона **3    #где взять эту сторону? сторона одна, __sides =[1]  тогда обратиться по индексу self.__sides[0] по инлексу?
        return v        # но я не внутри класса родителя у меня нет доступа но я могу получить доступ через метод родителя
                        # сторону возвращает get_sides значит взять ее по инлексу что ли? self.get_sides() []