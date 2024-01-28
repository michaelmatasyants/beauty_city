# Generated by Django 5.0.1 on 2024-01-26 10:57

import django.core.validators
import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Имя')),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(db_index=True, max_length=128, region=None, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Имя')),
                ('photo', models.ImageField(upload_to='', verbose_name='Портрет')),
            ],
            options={
                'verbose_name': 'Мастер',
                'verbose_name_plural': 'Мастера',
            },
        ),
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('address', models.CharField(max_length=250, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Все салоны красоты',
                'verbose_name_plural': 'Все салоны красоты',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Paid', 'Оплачен'), ('Unpaid', 'Не оплачен')], db_index=True, default='Unpaid', max_length=10, verbose_name='Статус оплаты')),
                ('promocode', models.CharField(blank=True, max_length=250, null=True, verbose_name='Промокод через choice')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='salons.client')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='SalonServiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salons', to='salons.master')),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salons', to='salons.salon')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salons', to='salons.service')),
            ],
            options={
                'verbose_name': 'Услуга салона красоты',
                'verbose_name_plural': 'Услуги салона красоты',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='salons.order')),
                ('salon_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='salons.salonserviceitem')),
            ],
            options={
                'verbose_name': 'Позиция в заказе',
                'verbose_name_plural': 'Позиции в заказе',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(db_index=True, verbose_name='Дата и время')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='salons.client', verbose_name='Клиент')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shedules', to='salons.master', verbose_name='Мастер')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписание',
                'unique_together': {('master', 'date_time')},
            },
        ),
    ]