# Generated by Django 4.2 on 2023-07-06 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0002_rename_fees_studentmodel_fees_paid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='stream',
            field=models.CharField(max_length=10),
        ),
    ]
