from django.db import models
from django.utils.translation import ugettext_lazy as _
from jsonfield import JSONField


class Article(models.Model):
    """Article Model"""

    title = models.CharField(verbose_name=_('Title'), max_length=90, db_index=True)
    pic = models.CharField(verbose_name=_('Pic'), max_length=90, db_index=True)
    content = models.TextField(verbose_name=_('Content'), blank=True)
    is_swiper = models.BooleanField(verbose_name=_('Is Swiper'), default=False)
    create_date = models.DateTimeField(verbose_name=_('Create Date'), auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['create_date']


class Category(models.Model):
    """Category Model"""

    title = models.CharField(verbose_name=_('Title'), max_length=90, db_index=True)
    type = models.CharField(verbose_name=_('Type'), max_length=11, db_index=True)
    pic = models.CharField(verbose_name=_('Pic'), max_length=90, db_index=True)
    desc = models.TextField(verbose_name=_('Desc'), blank=True)
    create_date = models.DateTimeField(verbose_name=_('Create Date'), auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['create_date']


class Question(models.Model):
    """Question Model"""

    title = models.CharField(verbose_name=_('Title'), max_length=90, db_index=True)
    type = models.CharField(verbose_name=_('Type'), max_length=11, db_index=True)
    answer = models.JSONField(verbose_name=_('Answer'), max_length=720, db_index=True)
    create_date = models.DateTimeField(verbose_name=_('Create Date'), auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['create_date']


class Feedback(models.Model):
    """Feedback Model"""

    title = models.CharField(verbose_name=_('Title'), max_length=90, db_index=True)
    content = models.TextField(verbose_name=_('Content'), blank=True)
    create_date = models.DateTimeField(verbose_name=_('Create Date'), auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['create_date']


class FileModel(models.Model):
    """FileModel Model"""
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='static/media/upload')


class Record(models.Model):
    """Record Model"""
    title = models.CharField(verbose_name=_('Title'), max_length=90, db_index=True)
    content = models.TextField(verbose_name=_('Content'), blank=True)
    openid = models.CharField(verbose_name=_('Open Id'), max_length=32, blank=True, db_index=True)
    create_date = models.DateTimeField(verbose_name=_('Create Date'), auto_now_add=True)
    psy_type = models.ForeignKey(to='Category', db_constraint=False, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['create_date']
