# Generated by Django 4.0.5 on 2022-07-02 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0002_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyrole',
            name='require_CV',
            field=models.BooleanField(),
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]