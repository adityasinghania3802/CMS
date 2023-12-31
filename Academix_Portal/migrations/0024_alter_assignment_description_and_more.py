# Generated by Django 4.2.6 on 2023-12-03 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academix_Portal', '0023_alter_material_material_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='description',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='faculty_profile',
            name='middle_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student_profile',
            name='middle_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
