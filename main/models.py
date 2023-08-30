from django.db import models


# Create your models here.
class Product(models.Model):
    name_prod = models.CharField(max_length=100, verbose_name='Наименование')
    description_prod = models.CharField(max_length=100, verbose_name='Описание')
    img_prod = models.ImageField(upload_to='preview', verbose_name='Превью', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория', null=True, blank=True)
    price_prod = models.IntegerField(verbose_name='Цена', null=True, blank=True, help_text='Введите цену продукта в рублях')
    data_create_prod = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    data_change_prod = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.name_prod} {self.price_prod} {self.description_prod}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    name_category = models.CharField(max_length=100, verbose_name='Наименование категории')
    category_description = models.CharField(max_length=100, verbose_name='Описание категории')

    def __str__(self):
        return f'{self.name_category} {self.category_description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    version_number = models.CharField(max_length=10, verbose_name='Номер версии')
    version_name = models.CharField(max_length=100, verbose_name='Название версии')
    is_current = models.BooleanField(default=False, verbose_name='Активность')

    # def save(self, *args, **kwargs):
    #     if self.is_current:
    #         # При установке этой версии как активной,
    #         # устанавливаем все остальные версии для этого продукта как неактивные
    #         Version.objects.filter(product=self.product).exclude(pk=self.pk).update(is_current=False)
    #     super(Version, self).save(*args, **kwargs)
    def __str__(self):
        return f'{self.product}, {self.version_name}, {self.version_number}'

    class Meta:
        verbose_name = "версия"
        verbose_name_plural = "версии"