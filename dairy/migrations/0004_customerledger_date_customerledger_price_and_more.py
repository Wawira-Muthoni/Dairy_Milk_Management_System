# Generated by Django 4.1 on 2022-08-10 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dairy', '0003_customerledger'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerledger',
            name='date',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='customerledger',
            name='price',
            field=models.FloatField(db_index=True, default=0.0, max_length=1000),
        ),
        migrations.AddField(
            model_name='customerledger',
            name='quantity',
            field=models.FloatField(db_index=True, default=0.0, max_length=100),
        ),
        migrations.AddField(
            model_name='customerledger',
            name='related_customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dairy.customerledger'),
        ),
        migrations.AddField(
            model_name='customerledger',
            name='total',
            field=models.FloatField(db_index=True, default=0.0, max_length=10000),
        ),
    ]