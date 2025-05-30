# Generated by Django 5.2 on 2025-04-28 17:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ShoeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=12)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('offerprice', models.IntegerField()),
                ('color', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='product/')),
                ('image1', models.ImageField(default='', upload_to='product/')),
                ('image2', models.ImageField(default='', upload_to='product/')),
                ('image3', models.ImageField(default='', upload_to='product/')),
                ('image4', models.ImageField(default='', upload_to='product/')),
                ('image5', models.ImageField(default='', upload_to='product/')),
                ('description', models.TextField()),
                ('priority', models.IntegerField(default=0)),
                ('gender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eapp.gender')),
                ('shoe_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eapp.shoecategory')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('amount', models.FloatField(verbose_name='Amount')),
                ('status', models.CharField(default='Pending', max_length=254, verbose_name='Payment Status')),
                ('provider_order_id', models.CharField(max_length=40, null=True, verbose_name='Order ID')),
                ('payment_id', models.CharField(max_length=36, null=True, verbose_name='Payment ID')),
                ('signature_id', models.CharField(max_length=128, null=True, verbose_name='Signature ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eapp.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('Stock', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sizes', to='eapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('totalprice', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eapp.product')),
                ('product_size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eapp.productsize')),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eapp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'product')},
            },
        ),
    ]
