from car import Car
from kia import Kia
from nissan import Nissan

nissan_qashqai = Nissan("Nissan Qashqai", "Синий")
nissan_qashqai_horse = nissan_qashqai.horse_powers(Nissan.ENGINE_CAPAcCITY2)
nissan_qashqai_price = nissan_qashqai.price_car(Nissan.ENGINE_CAPAcCITY2)

print(nissan_qashqai)
print(nissan_qashqai_horse)
print(nissan_qashqai_price)

kia_quoris = Kia("Kia Quoris", "Красный")
kia_quoris_horse = kia_quoris.horse_powers(Kia.ENGINE_CAPAcCITY1_6)
kia_quoris_price = kia_quoris.price_car(Kia.ENGINE_CAPAcCITY1_6)

print("*" * 30)
print(kia_quoris)
print(kia_quoris_horse)
print(kia_quoris_price)

car_vaz = Car("ВАЗ-2106", "Белая")
car_vaz_horse = car_vaz.horse_powers(Car.ENGINE_CAPAcCITY1_5)
car_vaz_price = car_vaz.price_car(Car.ENGINE_CAPAcCITY1_5)

print("*" * 30)
print(car_vaz)
print(car_vaz_horse)
print(car_vaz_price)
