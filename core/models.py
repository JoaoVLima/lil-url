from django.db import models

# Create your models here.


class DataLog(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # date_edited = models.DateTimeField(auto_now=True, null=True, blank=True)
    # date_deleted = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class Shortener(DataLog):
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)
    enabled = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.short_url} -> {self.long_url}'


class Access(models.Model):
    date_accessed = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dispositivo = models.CharField(max_length=100, blank=True)
    ip = models.CharField(max_length=100, blank=True)
    localizacao = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.ip}'


class Shortener_Access(models.Model):
    fk_id_shortener = models.ForeignKey(Shortener, on_delete=models.CASCADE)
    fk_id_access = models.ForeignKey(Access, on_delete=models.CASCADE)

