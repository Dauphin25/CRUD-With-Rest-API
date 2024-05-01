from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'))
    parent_category = models.ForeignKey('self',
                                        on_delete=models.CASCADE,
                                        null=True,
                                        blank=True,
                                        verbose_name=_('Parent Category'),
                                        related_name=_('subcategories'))

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name
