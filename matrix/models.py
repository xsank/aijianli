#encoding:utf-8
from django.db import models

# Create your models here.


class Admin(models.Model):
    name = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=20, verbose_name='密码')
    ip = models.GenericIPAddressField(verbose_name='登陆IP')
    time = models.DateField(verbose_name='登陆时间')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = '管理员'


class IDMap(models.Model):
    openid = models.CharField(max_length=40, verbose_name='OpenID')
    name = models.CharField(max_length=20, verbose_name='用户名')

    def __unicode__(self):
        return self.openid or self.name

    class Meta:
        verbose_name_plural = 'ID映射表'


class Style(models.Model):
    info = models.CharField(max_length=20, verbose_name='样式信息')
    css_addr = models.CharField(max_length=100, verbose_name='样式地址')

    def __unicode__(self):
        return self.info

    class Meta:
        verbose_name_plural = '风格'


class Resume(models.Model):
    ENGLISH = 'en'
    CHINESE = 'zh'
    LANGUAGE = (
        ('en', u'English'),
        ('zh', u'中文')
    )
    title = models.CharField(max_length=20, verbose_name='简历名称')
    language = models.CharField(max_length=10, choices=LANGUAGE, default=CHINESE)
    content = models.TextField(verbose_name='简历内容')
    style = models.ForeignKey(Style, verbose_name='简历样式')
    is_open = models.BooleanField(default=True, verbose_name='是否开放')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = '简历'


class User(models.Model):
    account = models.ForeignKey(IDMap, verbose_name='用户标识')
    password = models.CharField(max_length=20, verbose_name='密码')
    resume = models.ForeignKey(Resume, verbose_name='简历')
    time = models.DateField(verbose_name='登陆时间')

    def __unicode__(self):
        return self.account

    class Meta:
        verbose_name_plural = '用户'
