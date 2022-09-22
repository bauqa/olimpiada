
from django.db import models

# Create your models here.

class Women(models.Model):
    title = models.CharField(max_length=255,verbose_name="Заголовок")
    content = models.TextField(blank=True,verbose_name="Тескт статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/",verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True,verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True)
    is_published=models.BooleanField(default=True,verbose_name="Публикирован?")
    cat = models.ForeignKey('Category',on_delete=models.PROTECT,null=True,verbose_name="Катеогория")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ['id']

class Category(models.Model):
    name = models.CharField(max_length=127,db_index=True,verbose_name="Название")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['id']
