from django.db import models
from django.utils.translation import ugettext_lazy as _


class Article(models.Model):
    """Article Model"""

    title = models.CharField(verbose_name=_('Title'), max_length=90, db_index=True)
    pic = models.CharField(verbose_name=_('Pic'), max_length=90, db_index=True)
    content = models.TextField(verbose_name=_('content'), blank=True)
    is_swiper = models.BooleanField(verbose_name=_('Is Swiper'), default=False)
    create_date = models.DateTimeField(verbose_name=_('Create Date'), auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_date']
