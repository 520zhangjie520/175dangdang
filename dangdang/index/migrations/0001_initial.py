# Generated by Django 2.0 on 2019-10-20 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookClass',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(blank=True, max_length=255, null=True)),
                ('book_num', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'book_class',
            },
        ),
        migrations.CreateModel(
            name='TAddress',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=255, null=True)),
                ('telephone', models.CharField(blank=True, max_length=255, null=True)),
                ('mobilephone', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 't_address',
            },
        ),
        migrations.CreateModel(
            name='TBook',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(blank=True, max_length=255, null=True)),
                ('writer', models.CharField(blank=True, max_length=255, null=True)),
                ('pic', models.CharField(blank=True, max_length=255, null=True)),
                ('real_price', models.FloatField(blank=True, null=True)),
                ('dangdang_price', models.FloatField(blank=True, null=True)),
                ('publishing', models.CharField(blank=True, max_length=255, null=True)),
                ('publishing_time', models.CharField(blank=True, max_length=255, null=True)),
                ('word_num', models.CharField(blank=True, max_length=255, null=True)),
                ('page_num', models.CharField(blank=True, max_length=255, null=True)),
                ('size', models.CharField(blank=True, max_length=255, null=True)),
                ('paper', models.CharField(blank=True, max_length=255, null=True)),
                ('paking', models.CharField(blank=True, max_length=255, null=True)),
                ('version_num', models.CharField(blank=True, max_length=255, null=True)),
                ('print_num', models.CharField(blank=True, max_length=255, null=True)),
                ('print_time', models.CharField(blank=True, max_length=255, null=True)),
                ('isbn', models.CharField(blank=True, db_column='ISBN', max_length=255, null=True)),
                ('manager_rec', models.TextField(blank=True, null=True)),
                ('content_val', models.TextField(blank=True, null=True)),
                ('writer_val', models.TextField(blank=True, null=True)),
                ('catalog', models.TextField(blank=True, null=True)),
                ('media_com', models.TextField(blank=True, null=True)),
                ('digest_pic', models.TextField(blank=True, null=True)),
                ('stock_num', models.CharField(blank=True, max_length=255, null=True)),
                ('ground_time', models.CharField(blank=True, max_length=255, null=True)),
                ('customer_rat', models.CharField(blank=True, max_length=255, null=True)),
                ('flag', models.IntegerField(blank=True, null=True)),
                ('sales_vol', models.CharField(blank=True, max_length=255, null=True)),
                ('class_id', models.IntegerField(blank=True, null=True)),
                ('discuss_num', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 't_book',
            },
        ),
        migrations.CreateModel(
            name='TOrder',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('order_num', models.IntegerField(blank=True, null=True)),
                ('order_time', models.CharField(blank=True, max_length=255, null=True)),
                ('order_price', models.CharField(blank=True, max_length=255, null=True)),
                ('address_id', models.IntegerField(blank=True, null=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('flag', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 't_order',
            },
        ),
        migrations.CreateModel(
            name='TOrderItem',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_id', models.IntegerField(blank=True, null=True)),
                ('book_num', models.IntegerField(blank=True, null=True)),
                ('order_sum', models.IntegerField(blank=True, null=True)),
                ('order_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 't_order_item',
            },
        ),
        migrations.CreateModel(
            name='TShop',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('book_id', models.IntegerField()),
                ('number', models.IntegerField(blank=True, null=True)),
                ('save_price', models.CharField(blank=True, max_length=255, null=True)),
                ('all_price', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 't_shop',
            },
        ),
        migrations.CreateModel(
            name='TUser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('flag', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 't_user',
            },
        ),
    ]
