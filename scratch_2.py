class listers(list):
    def __init__(self):
        super().__init__()
        self.__values = []


    @property
    def updates(self):
        print(self.__values,890)
        return self.__values

    @updates.setter
    def updates(self,values):
        print(values)
        self.__values.__iadd__(values)
        super().__iadd__(self.__values)






y = listers()
print(y)
y.updates = (90,45,[34])
y.updates = (89,)
print(y)