from django.db import models
from django.core.validators import MaxValueValidator

class Models(models.Model):
    md_name = models.CharField(max_length=100, default="")
    md_info = models.CharField(max_length=250, default="")
    md_image = models.ImageField(upload_to='models/', default="")
    md_file = models.FileField(upload_to='models_files/', default="")
    md_owner_name = models.CharField(max_length=50, default="")
    md_rating = models.FloatField(validators=[MaxValueValidator(5)], default=0)
    md_upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.md_name
