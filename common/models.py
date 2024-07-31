from django.core.exceptions import ValidationError
from django.db import models
from django.http.request import MediaType
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from .validators import file_validator
# Create your models here.


class Media(models.Model):

    class MediaType(models.TextChoices):
        IMAGE = 'image', _('image'),
        VIDEO = 'video', _('video'),
        FILE = 'file', _('file'),
        AUDIO = 'audio', _('audio'),
        MUSIC = 'music', _('music')

    type = models.CharField(_('type'), max_length=50, choices=MediaType.choices)
    file = models.FileField(_('file'), upload_to='media/', validators=[FileExtensionValidator(
        allowed_extensions=['png', 'jpg', 'jpeg', 'gif', 'mp4', 'mp3']
    )])

    def clean(self):
        if self.type not in self.MediaType.IMAGE.value:
            raise ValidationError(_(" Invalid file type"))
        elif self.type == self.MediaType.IMAGE:
            if self.file.name.split('.')[-1] not in ['jpg', 'jpeg', 'png']:
                raise ValidationError(_('Invalid image file'))

    class Meta:
        verbose_name = _('Media')
        verbose_name_plural = _('Media')
