from django.db import models
from django.utils.translation import gettext_lazy as _


class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'))
    category = models.ForeignKey('api.Category', on_delete=models.CASCADE, verbose_name=_('Category'))
    tags = models.ManyToManyField('api.Tag', verbose_name=_('Tags'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Price'))
    stock = models.PositiveIntegerField(verbose_name=_('Stock'))

    class Meta:
        verbose_name = _('Item')
        verbose_name_plural = _('Items')

    def __str__(self):
        return self.name
