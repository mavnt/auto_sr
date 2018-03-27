# auto_sr

## `__str__` and `__repr__` automatically generated using annotations

You have:

```python
class Person0(object):
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

p0 = Person0("John", "Smith", 55)
print(p0, [p0])
```

```
<__main__.Person0 object at 0x06E0CF10> [<__main__.Person0 object at 0x06E0CF10>]
```

-----

With auto_sr you have:

```python
@auto_sr()
class Person1(object):
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
p1 = Person1("John", "Smith", 55)
print(p1, [p1])
```

```
{'name': 'John', 'surname': 'Smith', 'age': 55} [{'name': 'John', 'surname': 'Smith', 'age': 55}]
```

or

```python
@auto_sr(["surname"])
class Person2(object):
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
p2 = Person2("John", "Smith", 55)
print(p2, [p2])
```

```
{'surname': 'Smith'} [{'surname': 'Smith'}]
```

or (with inheritance)

```python
class Student0(Person2):
    def __init__(self, *args):
        super(Student0, self).__init__(*args)


@auto_sr(["id"])
class Student1(Person2):
    def __init__(self, id, *args):
        super(Student1, self).__init__(*args)
        self.id = id
# surname only, inherited from Person2
s0 = Student0("John", "Smith", 55)
print(s0, [s0])

# id (Student1)
s1 = Student1(7575, "John", "Smith", 55)
print(s1, [s1])
```

```
{'surname': 'Smith'} [{'surname': 'Smith'}]
{'id': 7575} [{'id': 7575}]
```

