# Generated by Django 4.1.4 on 2023-02-07 18:50

import application.managers
from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(db_index=True, max_length=250, unique=True)),
                ('role', models.CharField(choices=[('MANAGEMENT', 'Management'), ('SALES', 'Sales'), ('SUPPORT', 'Support')], max_length=20)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', application.managers.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.EmailField(db_index=True, max_length=100, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=250)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('sales_contact', models.ForeignKey(limit_choices_to={'role': 'SALES'}, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('is_signed', models.BooleanField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('payment_due', models.DateTimeField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='client_contract', to='application.client')),
                ('sales_contact', models.ForeignKey(limit_choices_to={'role': 'SALES'}, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('event_status', models.CharField(choices=[('CREATED', 'Created'), ('FINISHED', 'Finished')], max_length=20)),
                ('attendees', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('event_date', models.DateTimeField()),
                ('notes', models.CharField(max_length=300)),
                ('client', models.ForeignKey(limit_choices_to={'client_contract__is_signed': True}, on_delete=django.db.models.deletion.PROTECT, related_name='client_event', to='application.client')),
                ('contract', models.ForeignKey(limit_choices_to={'is_signed': True}, on_delete=django.db.models.deletion.PROTECT, to='application.contract')),
                ('support_contact', models.ForeignKey(limit_choices_to={'role': 'SUPPORT'}, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
