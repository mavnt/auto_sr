# coding=utf-8
from .auto_sr import auto_sr


class Person0(object):
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


@auto_sr()
class Person1(object):
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


@auto_sr(["surname"])
class Person2(object):
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class Student0(Person2):
    def __init__(self, *args):
        super(Student0, self).__init__(*args)


@auto_sr(["id"], repr_=False)
class Student1(Person2):
    def __init__(self, id, *args):
        super(Student1, self).__init__(*args)
        self.id = id


def demo() -> None:
    # standard
    p0 = Person0("John", "Smith", 55)
    print(p0, [p0])

    # all
    p1 = Person1("John", "Smith", 55)
    print(p1, [p1])

    # surname only
    p2 = Person2("John", "Smith", 55)
    print(p2, [p2])

    # surname only, inherited from Person2
    s0 = Student0("John", "Smith", 55)
    print(s0, [s0])

    # id (Student1)
    s1 = Student1(7575, "John", "Smith", 55)
    print(s1, [s1])


if __name__ == "__main__":
    demo()
