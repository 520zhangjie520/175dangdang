# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BookClass(models.Model):
    id = models.IntegerField(primary_key=True)
    boo = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    class_name = models.CharField(max_length=255, blank=True, null=True)
    book_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_class'


class TAddress(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    mobilephone = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_address'


class TBook(models.Model):
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=255, blank=True, null=True)
    writer = models.CharField(max_length=255, blank=True, null=True)
    pic = models.CharField(max_length=255, blank=True, null=True)
    real_price = models.FloatField(blank=True, null=True)
    dangdang_price = models.FloatField(blank=True, null=True)
    publishing = models.CharField(max_length=255, blank=True, null=True)
    publishing_time = models.CharField(max_length=255, blank=True, null=True)
    word_num = models.CharField(max_length=255, blank=True, null=True)
    page_num = models.CharField(max_length=255, blank=True, null=True)
    size = models.CharField(max_length=255, blank=True, null=True)
    paper = models.CharField(max_length=255, blank=True, null=True)
    paking = models.CharField(max_length=255, blank=True, null=True)
    version_num = models.CharField(max_length=255, blank=True, null=True)
    print_num = models.CharField(max_length=255, blank=True, null=True)
    print_time = models.CharField(max_length=255, blank=True, null=True)
    isbn = models.CharField(db_column='ISBN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    manager_rec = models.TextField(blank=True, null=True)
    content_val = models.TextField(blank=True, null=True)
    writer_val = models.TextField(blank=True, null=True)
    catalog = models.TextField(blank=True, null=True)
    media_com = models.TextField(blank=True, null=True)
    digest_pic = models.TextField(blank=True, null=True)
    stock_num = models.CharField(max_length=255, blank=True, null=True)
    ground_time = models.CharField(max_length=255, blank=True, null=True)
    customer_rat = models.CharField(max_length=255, blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True)
    sales_vol = models.CharField(max_length=255, blank=True, null=True)
    class_id = models.IntegerField(blank=True, null=True)
    discuss_num = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_book'


class TOrder(models.Model):
    id = models.IntegerField(primary_key=True)
    order_num = models.IntegerField(blank=True, null=True)
    order_time = models.CharField(max_length=255, blank=True, null=True)
    order_price = models.CharField(max_length=255, blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_order'


class TOrderItem(models.Model):
    id = models.IntegerField(primary_key=True)
    book_id = models.IntegerField(blank=True, null=True)
    book_num = models.IntegerField(blank=True, null=True)
    order_sum = models.IntegerField(blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_order_item'


class TShop(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    book_id = models.IntegerField()
    number = models.IntegerField(
        blank=True, null=True)
    save_price = models.CharField(max_length=255, blank=True, null=True)
    all_price = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_shop'
        unique_together = (('id', 'user_id', 'book_id'),)


class TUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=255, blank=True, null=True)
    flag = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user'
