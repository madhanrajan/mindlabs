# Generated by Django 2.0.13 on 2019-09-29 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0016_auto_20190327_0757'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='file',
            field=models.FileField(default=1, upload_to='files/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]