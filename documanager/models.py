import os
from documanager.settings import MEDIA_ROOT, MEDIA_FOLDER
from documanager.utils.system_storage import upload_path_handler, upload_path_handler2
from django.core.files.storage import FileSystemStorage
from django.core.validators import MaxLengthValidator
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe

class User(models.Model):
    name = models.CharField(max_length=120)
    password = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Document(models.Model):
    name_s = models.CharField(max_length=120)
    file_path_s = models.CharField(max_length=500)
    file_name_s = models.CharField(max_length=250)
    file_type_s = models.CharField(max_length=50)
    url_s = models.CharField(max_length=500)
    created_at_dt = models.DateTimeField(default=timezone.now, editable=False)
    modified_at_dt = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    file_uploaded_b = models.FileField(
        upload_to=upload_path_handler,
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        """ On save, update timestamp """
        if self.id:
            self.modified_at_dt = timezone.now()
     
        return super(Document, self).save(*args, **kwargs)

    def __str__(self):
        return self.name_s

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['url_s'], name='unique_url'),
            models.UniqueConstraint(fields=['file_uploaded_b'], name='unique_document')
        ]

class Revision(models.Model):
    title_s = models.CharField(max_length=120)
    comment_s = models.TextField(max_length=1000, blank=True, validators=[MaxLengthValidator(1000)])
    number_i = models.IntegerField(default=1)
    file_name_s = models.CharField(max_length=250, default="")
    file_type_s = models.CharField(max_length=50, default="")
    local_full_path_s = models.CharField(max_length=500, default="")
    created_at_dt = models.DateTimeField(default=timezone.now, editable=False)
    modified_at_dt = models.DateTimeField(null=True, blank=True)
    document = models.ForeignKey(to=Document, on_delete=models.CASCADE)
    file_uploaded_b = models.FileField(
        upload_to=upload_path_handler2,
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        """ On save, update timestamp """
        if self.id:
            self.modified_at_dt = timezone.now()

        try:
            latest_revision = Revision.objects.filter(document_id=self.document.id).last()
            self.number_i = latest_revision.number_i + 1
        except Exception as e:
             self.number_i = 1

        doc = Document.objects.filter(id=self.document.id).first()
        user = doc.user
        
        self.local_full_path_s = f"/home/documanager/files/{user.id}/{self.document.id}/{self.number_i}_{doc.file_name_s}"
 
        return super(Revision, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title_s}_v{self.number_i}"