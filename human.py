class Human:

# конструктор класса и его свойства - трафарет
    def __init__(self, name, years, sex, height, weight):
        self.name = name
        self.years = years
        self.sex = sex
        self.height = height
        self.weight = weight

    def walk(self):
        print(f'{self.name} walk!')

    def run(self):
        if self.years > 3:
            return print(f"{self.name} run!")
        else:
            return print(f"{self.name} can't run!")

    # staticmethod это метод принадлежит классу, но мы не используем его методы и свойства
    @staticmethod
    def speak(word):
        print(word)

    # вызов метда без создания обьекта класса (человека)
    @classmethod
    def birth(cls, name, years, sex, height, weight):
        return cls(name, years, sex, height, weight)

    # magic method - обьект
    def __repr__(self):
        return (f'Human(name={self.name}, years={self.years}, sex={self.sex}, '
                f'height={self.height}, weight={self.weight})')

# создаем человека при помощи classmethod
alex = Human.birth(name="Vlad", years=2, sex='male', height=178, weight=88)



# создаем человека
peter = Human(name="Peter", years=33, sex='male', height=188, weight=100)
peter.walk()
olga = Human(name="Olga", years=25, sex='female', height=166, weight=50)
olga.walk()
print(peter.speak("Human"))

alex.run()
peter.run()

class Auto:

    def __init__(self, mark, body_type, speed):
        self.mark = mark
        self.body_type = body_type
        self.speed = speed

    def drive(self):
        print(f"{self.mark} drive!")

toyota = Auto(mark="Toyota", body_type="sedan", speed=100)
toyota.drive()
honda = Auto(mark="Honda", body_type="crossover", speed=80)
honda.drive()


