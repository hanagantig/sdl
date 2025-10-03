from django.db import models


class Product(models.Model):
	number = models.IntegerField(null=False, blank=False, verbose_name="Номер работы")
	company = models.CharField(max_length=255, null=False, blank=True, verbose_name="Компания")
	doctor = models.CharField(max_length=255, null=False, blank=False, verbose_name="Доктор")
	patient = models.CharField(max_length=255, null=False, blank=False, verbose_name="Пациент")
	is_paid = models.BooleanField(null=False, blank=True, default=False, verbose_name="Оплачено")
	entered_date = models.DateField(null=False, blank=False, verbose_name="Дата поступления")
	finished_date = models.DateField(null=True, blank=True, verbose_name="Дата сдачи")
	created_date = models.DateField(auto_now_add=True, verbose_name="Дата создания")
	updated_date = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

	def __str__(self):
		return "Изделие N{0}".format(self.number)

	class Meta:
		verbose_name = u'Изделие'
		verbose_name_plural = u'Изделия'


class ProductItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="items", verbose_name="Изделие")
	title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Наименование")
	price = models.IntegerField(null=False, blank=False, verbose_name="Цена")
	is_paid = models.BooleanField(null=False, blank=True, default=False, verbose_name="Оплачено")

	class Meta:
		verbose_name = u'Вид работы'
		verbose_name_plural = u'Виды работ'