# Generated by Django 4.0.3 on 2022-04-05 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_cumtomer_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('price', models.FloatField(null=True)),
                ('category', models.CharField(choices=[('Indoor', 'Indoor'), ('Out door', 'Out door')], max_length=50, null=True)),
                ('description', models.CharField(max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
