# Generated by Django 3.2.10 on 2021-12-20 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyPriceLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='NULL', max_length=100)),
                ('result', models.CharField(default='NULL', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='dailyprice',
            name='commodity',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='dailyprice',
            name='arrival',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='dailyprice',
            name='avg_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dailyprice',
            name='max_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dailyprice',
            name='measure',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='dailyprice',
            name='min_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dailyprice',
            name='name',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='selectedprice',
            name='arrival',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='selectedprice',
            name='avg_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='selectedprice',
            name='date',
            field=models.DateField(default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='selectedprice',
            name='max_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='selectedprice',
            name='measure',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='selectedprice',
            name='min_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='selectedprice',
            name='name',
            field=models.CharField(default='NULL', max_length=100),
        ),
    ]
