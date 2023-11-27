# Generated by Django 4.2.6 on 2023-11-25 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academix_Portal', '0016_alter_assignment_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='attachment',
            field=models.FileField(upload_to='attachments'),
        ),
        migrations.AlterField(
            model_name='material',
            name='material_file',
            field=models.FileField(upload_to='materials'),
        ),
    ]