# Generated by Django 3.2.3 on 2022-01-10 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='uid',
        ),
        migrations.AddField(
            model_name='user',
            name='adr',
            field=models.CharField(default=189185, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, default=218, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]