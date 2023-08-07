from django.core.management import BaseCommand

from main.models import Category


class Command(BaseCommand):
    help = 'команда, которая умеет заполнять данные в базу данных, при этом предварительно зачищать ее от старых данных'

    def handle(self, *args, **options):
        """фнкция очистки таблицы категории-Category БД и заполнение новыми данными"""
        Category.objects.all().delete()  # очистка таблицы Category

        # Добавить новые данные в базу данных
        new_items = [
            {'name_category': 'Соки', 'category_description': 'Соки вкусные, разные заразные'},
            {'name_category': 'Хлебобулочные изделия', 'category_description': 'Хлеб, булки, пироженки, батон'},
            # Добавьте здесь остальные данные, которые добавляем, здесь можно реалисовать распаковку из файла
        ]

        cat_list = []
        for item_data in new_items:
            cat_list.append(Category(**item_data))

        Category.objects.bulk_create(cat_list)  # заполняем таблицу


