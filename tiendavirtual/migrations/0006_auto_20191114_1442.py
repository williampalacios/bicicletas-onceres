# Generated by Django 2.2.7 on 2019-11-14 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendavirtual', '0005_auto_20191114_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='imagentest',
            field=models.FileField(blank=True, null=True, upload_to='img_prod'),
        ),
    ]
