# Generated by Django 4.2.6 on 2023-11-29 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academix_Portal', '0022_alter_material_material_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='material_file',
            field=models.FileField(upload_to='materials'),
        ),
    ]
