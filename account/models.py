from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=10)
    birth_date = models.DateTimeField()
    photo = models.URLField()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("User")


class Group(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField(User, related_name='groups')

    class Meta:
        verbose_name = _("Group")
        verbose_name_plural = _("Group")


class UserMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(_("message"), max_length=100)
    file = models.FileField(_('file'), upload_to='media/')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("UserMessage")
        verbose_name_plural = _("UserMessage")


