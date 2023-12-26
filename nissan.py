from car import Car
from vehicle import Vehicle


class Nissan(Car, Vehicle):

    vehicle_type = "sedan"
    price = 2000000

    def __str__(self):
        return f'Автомобиль {self.vehicle_type} {self.name_car} цвета {self.color_car}'

    def horse_powers(self, volume):
        if volume <= Nissan.ENGINE_CAPAcCITY1_5:
            return f'Количество лошадиных сил автомобиля {self.name_car} 120 '
        elif Nissan.ENGINE_CAPAcCITY2 > volume >= Nissan.ENGINE_CAPAcCITY1_6:
            return f'Количество лошадиных сил автомобиля {self.name_car} 130'
        elif volume >= Nissan.ENGINE_CAPAcCITY2:
            return f'Количество лошадиных сил автомобиля {self.name_car} 180'
        else:
            return f'Объём двигателя введён не верно'

    def price_car(self, volume):
        if volume <= Nissan.ENGINE_CAPAcCITY1_5:
            res1 = Nissan.price = 3000000
            return f'Стоимость автомобиля {self.name_car} {res1}'
        elif Nissan.ENGINE_CAPAcCITY2 > volume >= Nissan.ENGINE_CAPAcCITY1_6:
            res2 = Nissan.price = 3500000
            return f'Стоимость автомобиля {self.name_car} {res2}'
        elif volume >= Nissan.ENGINE_CAPAcCITY2:
            res3 = Nissan.price = 4000000
            return f'Стоимость автомобиля {self.name_car} {res3}'
