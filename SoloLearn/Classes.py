class Human:
    def __init__(self, sex):
        self.__sex = sex

    @property  # work as a getter - read-only
    def gender(self):
        return self.__sex

    @gender.setter
    def gender(self, value):
        if value == "male":
            print("a man")
        self.__sex = value


if __name__ == '__main__':
    h = Human("female")
    print(h.gender)
    h.gender = "male"  # set the value
