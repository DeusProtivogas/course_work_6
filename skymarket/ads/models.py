from django.conf import settings
from django.db import models


class Ad(models.Model):

    title = models.CharField(max_length=200, verbose_name="Название товара", default="")
    price = models.PositiveIntegerField(verbose_name="Цена товара", default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="ads",
                               verbose_name="Автор объявления", default="")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания объявления", null=False)
    description = models.CharField(blank=True, null=True, max_length=1000, verbose_name="Описание товара", default="")
    image = models.ImageField(upload_to="images/", verbose_name="фото", null=True, blank=True,)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ("-created_at",)


class Comment(models.Model):
    text = models.CharField(max_length=1000,verbose_name="Комментарий",)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Время создания комментария",)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                               related_name="comments", verbose_name="Автор комментария", default="")
    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Объявление",
        default=""
    )

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ("-created_at",)