# Generated by Django 2.2.4 on 2019-08-29 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20190626_1313'),
        ('insitu_stationary', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MetObsStation',
        ),
        migrations.CreateModel(
            name='InsituStationary',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('catalog.dataset',),
        ),
    ]
