from django.db import models

# Create your models here.
class Data(models.Model):
    name1=models.CharField(max_length=128)
    memrry=models.CharField(max_length=128)
    xueli=models.CharField(max_length=128)
    g_xingzhi=models.CharField(max_length=128)
    exprence=models.TextField()
    age=models.CharField(max_length=128)
    jiguan=models.CharField(max_length=128)
    expect_city=models.CharField(max_length=128)
    expect_salary=models.CharField(max_length=128)
    expect_zhiwei=models.CharField(max_length=128)
    expect_hangye=models.CharField(max_length=128)
    g_status=models.CharField(max_length=128)
    now_position=models.CharField(max_length=128)
    birth=models.CharField(max_length=128)
    email=models.CharField(max_length=128)
    phone=models.CharField(max_length=128)

    class Meta:
        db_table='exsl'