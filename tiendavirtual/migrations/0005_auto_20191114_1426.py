# Generated by Django 2.2.7 on 2019-11-14 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendavirtual', '0004_remove_productos_externalurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='imagentest',
            field=models.ImageField(blank=True, null=True, upload_to='img_prod'),
        ),
    ]