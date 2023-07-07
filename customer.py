class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if self.is_child():
            return 1000

        if self.is_adult():
            return 1500

        if self.is_senior():
            return 1200

    def is_child(self):
        return 0 <= self.age < 20

    def is_adult(self):
        return 20 <= self.age < 65

    def is_senior(self):
        return 65 <= self.age

    def info_csv(self):
        return f"{self.full_name()},{self.age},{self.entry_fee()}"


if __name__ == "__main__":
    ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
    print(ken.age)
    print(ken.entry_fee())

    tom = Customer(first_name="Tom", family_name="Ford", age=57)
    print(tom.age)
    print(tom.entry_fee())

    ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
    print(ieyasu.age)
    print(ieyasu.entry_fee())
