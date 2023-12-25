class Car:

    ENGINE_CAPAcCITY1_5 = 1.5
    ENGINE_CAPAcCITY1_6 = 1.6
    ENGINE_CAPAcCITY2 = 2

    price = 1000000

    def __init__(self, name_car, color_car):
        self.name_car = name_car
        self.color_car = color_car

    def __str__(self):
        return f'Автомобиль {self.name_car} цвета {self.color_car}'

    def __eq__(self, __o):
        return super().__eq__(__o)

    def horse_powers(self, volume):
        if volume <= Car.ENGINE_CAPAcCITY1_5:
            return f'Количество лошадиных сил автомобиля {self.name_car} 80 '
        elif Car.ENGINE_CAPAcCITY2 > volume >= Car.ENGINE_CAPAcCITY1_6:
            return f'Количество лошадиных сил автомобиля {self.name_car} 100'
        elif volume >= Car.ENGINE_CAPAcCITY2:
            return f'Количество лошадиных сил автомобиля {self.name_car} 110'
        else:
            return f'Объём двигателя введён не верно'

    def price_car(self, volume):
        if volume <= Car.ENGINE_CAPAcCITY1_5:
            res1 = Car.price = 500000
            return f'Стоимость автомобиля {self.name_car} {res1}'
        elif Car.ENGINE_CAPAcCITY2 > volume >= Car.ENGINE_CAPAcCITY1_6:
            res2 = Car.price = 700000
            return f'Стоимость автомобиля {self.name_car} {res2}'
        elif volume >= Car.ENGINE_CAPAcCITY2:
            res3 = Car.price = 900000
            return f'Стоимость автомобиля {self.name_car} {res3}'
