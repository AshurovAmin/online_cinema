class Student:
    def __init__(self, name):
        self.__name = name
    #
    # def get_name(self):
    #     return self.__name
    #
    # def set_name(self, new_name):
    #     self.__name = new_name
    #
    # def delete_name(self):
    #     raise Exception('Нельзя удалять name')
    #
    # name = property(get_name, set_name, delete_name)
#

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    @name.deleter
    def name(self):
        raise Exception('Нельзя удалять name')

s = Student("Amin")
print(s.name)
s.name = "Amin"
print(s.name)



# print(s.get_name())
# s.set_name('Amin')
# print(s.get_name())