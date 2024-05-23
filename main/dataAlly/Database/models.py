from django.core.validators import MaxValueValidator
from django.db import models

class Database(models.Model):
    db_name = models.CharField(max_length=100, default="")
    db_type = models.CharField(max_length=100, default="")
    db_info = models.CharField(max_length=250, default="")
    db_image = models.ImageField(upload_to='datasets/', default="")
    db_file = models.FileField(upload_to='datasets_files/', default="")
    db_owner_name = models.CharField(max_length=50, default="")
    db_rating = models.FloatField(validators=[MaxValueValidator(5)], default=0)
    db_upload_date = models.DateTimeField(auto_now_add=True)
    db_price = models.IntegerField(default=0)

    def __str__(self):
        return self.db_name