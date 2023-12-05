# Generated by Django 4.2.7 on 2023-12-05 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_usermodel_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermodel',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AddField(
            model_name='usermodel',
            name='code',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
