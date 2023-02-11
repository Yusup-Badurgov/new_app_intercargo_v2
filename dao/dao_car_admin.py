# CRUD
from flask import request

from dao.dao_car import Car


class AdminCar(Car):

    def save_changes(self, old_str, new_str):
        with open('database_car', 'r', encoding='utf-8') as file:
            data_car = file.read()

        new_data_str = data_car.replace(old_str, new_str)

        with open('database_car', 'w', encoding='utf-8') as file:
            file.write(new_data_str)

    def changes_price(self):
        choice_country = super().get_request_country_city()[0]
        choice_city = super().get_request_country_city()[1]
        changed_price = request.form['changed_price']

        cities = super().get_cities()

        data_dict = super().create_dict(choice_country)

        old_str_data = f'{choice_country} ' \
                       f'{data_dict[choice_country][cities[0]]}' \
                       f' {data_dict[choice_country][cities[1]]}' \

        old_price = data_dict[choice_country][choice_city]

        data_dict[choice_country][choice_city] = str(changed_price)

        new_str_data = f'{choice_country} ' \
                       f'{data_dict[choice_country][cities[0]]}' \
                       f' {data_dict[choice_country][cities[1]]}' \


        self.save_changes(old_str_data, new_str_data)

        return f'Данные по направлению "{choice_country} - {choice_city} / {choice_city} - {choice_country} " - успешно изменены\n' \
               f'Было {old_price}€\n' \
               f'Стало {changed_price}€'
