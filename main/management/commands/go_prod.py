from django.core.management import BaseCommand

from main.models import Product


class Command(BaseCommand):
    help = 'команда, которая умеет заполнять данные в базу данных, при этом предварительно зачищать ее от старых данных'

    def handle(self, *args, **options):
        """фнкция очистки таблицы категории-Product БД и заполнение новыми данными"""
        Product.objects.all().delete()  # очистка таблицы Category

        # Добавить новые данные в базу данных
        new_items = [
            {'name_prod': 'Соки', 'description_prod': 'Соки вкусные', 'img_prod': '', 'category_prod': 'фрукты',
             'price_prod': '100'},
            {'name_prod': 'Яблоки', 'description_prod': 'Сладкие яблоки', 'img_prod': '', 'category_prod': 'фрукты',
             'price_prod': '50'},
            {'name_prod': 'Бананы', 'description_prod': 'Спелые бананы', 'img_prod': '', 'category_prod': 'фрукты',
             'price_prod': '80'},
            {'name_prod': 'Морковь', 'description_prod': 'Свежая морковь', 'img_prod': '', 'category_prod': 'овощи',
             'price_prod': '30'},
            {'name_prod': 'Помидоры', 'description_prod': 'Сочные помидоры', 'img_prod': '', 'category_prod': 'овощи',
             'price_prod': '40'},
            {'name_prod': 'Огурцы', 'description_prod': 'Сладкие огурцы', 'img_prod': '', 'category_prod': 'овощи',
             'price_prod': '35'},
            {'name_prod': 'Хлеб белый', 'description_prod': 'Ароматный хлеб', 'img_prod': '', 'category_prod': 'хлеб',
             'price_prod': '25'},
            {'name_prod': 'Хлеб ржаной', 'description_prod': 'Питательный хлеб', 'img_prod': '',
             'category_prod': 'хлеб', 'price_prod': '30'},
            {'name_prod': 'Хлеб тостовый', 'description_prod': 'Полезный хлеб', 'img_prod': '',
             'category_prod': 'хлеб', 'price_prod': '35'},
            {'name_prod': 'Персики', 'description_prod': 'Сочные персики', 'img_prod': '', 'category_prod': 'фрукты',
             'price_prod': '70'}
        ]

        prod_list = []
        for item_data in new_items:
            prod_list.append(Product(**item_data))

        Product.objects.bulk_create(prod_list)  # заполняем БД