from django.db import models
from django.utils.timezone import now

# Create your models here.
class tln(models.Model):

    id = models.AutoField(primary_key=True)
    input_text = models.TextField()
    output_text = models.TextField()
    input_language = models.CharField()
    output_language = models.CharField()
    timestamp = models.DateTimeField(default=now)

    class Meta:
        db_table = 'translation'  # Set the table name here