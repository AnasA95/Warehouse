# Generated by Django 2.0.5 on 2018-06-03 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whss', '0004_auto_20180529_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='a', max_length=300),
            preserve_default=False,
        ),
    ]