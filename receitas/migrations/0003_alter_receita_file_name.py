# Generated by Django 4.0.3 on 2022-04-03 16:21

from django.db import migrations, models
import receitas.models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0002_receita_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='file_name',
            field=models.ImageField(null=True, upload_to=receitas.models.upload_image_receita),
        ),
    ]
