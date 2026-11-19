from django.db import models
MAX_LENGTH = 255
class Vid(models.Model):
    Vid_animals = models.CharField(max_length=20)
    def __str__(self):
        return self.Vid_animals
    class Meta:
        verbose_name = 'Вид животного'
        verbose_name_plural = 'Виды животных'

class Tip(models.Model):
    Tip_animals = models.CharField(max_length=20)
    def __str__(self):
        return self.Tip_animals
    class Meta:
        verbose_name = 'Тип животного'
        verbose_name_plural = 'Типы животных'


class Klimzona(models.Model):
    Klimzoni = models.CharField(max_length=20)
    def __str__(self):
        return self.Klimzoni

    class Meta:
        verbose_name = 'Климатическая зона'
        verbose_name_plural = 'Климатические зоны'


class Animals(models.Model):
    Data_registr_v_zoo = models.DateField()
    Data_rozden = models.DateField(null=True, blank=True)
    Klichka = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='animals/', null=True, blank=True)
    ID_Vid = models.ForeignKey(Vid, on_delete=models.PROTECT)
    ID_Tip = models.ForeignKey(Tip, on_delete=models.PROTECT)
    ID_Klimzona = models.ForeignKey(Klimzona, on_delete=models.PROTECT)

    def __str__(self):
        return self.Klichka or f'Животное №{self.pk}'

    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'


class Dolznost(models.Model):
    Naimenovanye = models.CharField(max_length=20)
    Obyazannosti = models.CharField(max_length=150)

    def __str__(self):
        return self.Naimenovanye

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Pol(models.Model):
    Pol = models.CharField(max_length=20)

    def __str__(self):
        return self.Pol

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'


class CategSotr(models.Model):
    naim_categor = models.CharField(max_length=20)

    def __str__(self):
        return self.naim_categor

    class Meta:
        verbose_name = 'Категория сотрудника'
        verbose_name_plural = 'Категории сотрудников'


class Sotr(models.Model):
    FIO = models.CharField(max_length=30)
    Data_rozden = models.DateField(null=True, blank=True)
    zp = models.PositiveIntegerField(null=True, blank=True)
    Data_priema = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='employees/', null=True, blank=True)
    ID_Pol = models.ForeignKey(Pol, on_delete=models.PROTECT)
    ID_Dolznost = models.ForeignKey(Dolznost, on_delete=models.PROTECT)
    ID_categor = models.ForeignKey(CategSotr, on_delete=models.PROTECT)

    def __str__(self):
        return self.FIO

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
