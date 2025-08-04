class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"{self.name}")
        print(f"{self.age}")


class Employee(Person):
    def __init__(self,name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        super().display_details()
        print(f"{self.salary}")


if __name__ == "__main__":
    personne = Person("Marie Dubois", 30)
    personne.display_details()

    employe = Employee("Pierre Martin", 28, 45000)
    employe.display_details()