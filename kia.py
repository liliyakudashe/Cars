from car import Car


class Kia(Car):

    price = 1500000

    def horse_powers(self, volume):
        if volume <= Kia.ENGINE_CAPAcCITY1_5:
            return f'Количество лошадиных сил автомобиля {self.name_car} 100 '
        elif Kia.ENGINE_CAPAcCITY2 > volume >= Kia.ENGINE_CAPAcCITY1_6:
            return f'Количество лошадиных сил автомобиля {self.name_car} 110'
        elif volume >= Kia.ENGINE_CAPAcCITY2:
            return f'Количество лошадиных сил автомобиля {self.name_car} 120'
        else:
            return f'Объём двигателя введён не верно'

    def price_car(self, volume):
        if volume <= Kia.ENGINE_CAPAcCITY1_5:
            res1 = Kia.price = 2000000
            return f'Стоимость автомобиля {self.name_car} {res1}'
        elif Kia.ENGINE_CAPAcCITY2 > volume >= Kia.ENGINE_CAPAcCITY1_6:
            res2 = Kia.price = 2500000
            return f'Стоимость автомобиля {self.name_car} {res2}'
        elif volume >= Kia.ENGINE_CAPAcCITY2:
            res3 = Kia.price = 3000000
            return f'Стоимость автомобиля {self.name_car} {res3}'
