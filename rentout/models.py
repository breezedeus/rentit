from django.contrib.auth.models import User
from django.db import models


# # Create your models here.
# class Item(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=5000, default='Nothing is written.')
#     owner = models.ForeignKey(User)
#     price = models.FloatField(null=True)
#
#     def __str__(self):
#         return self.name + '_' + str(self._get_pk_val())


class Outorder(models.Model):
    item_name = models.CharField('Item name', max_length=100)
    creator = models.ForeignKey(User)
    price = models.FloatField()
    address = models.CharField('Address to get the object', max_length=100, null=True)
    description = models.CharField(max_length=5000, default='The creator is so lazy.')
    borrower_id = models.PositiveIntegerField(default=0)
    start_date = models.DateTimeField('date the item may rent out')
    end_date = models.DateTimeField('date the item may be sent back')
    pub_date = models.DateTimeField('date published')
    #ext = models.CharField(max_length=1000, null=True)

    def available(self):
        return self.borrower_id == 0
    available.boolean = 'True'
    available.short_description = 'Still available?'

    def __str__(self):
        return '_'.join((self.item_name, str(self.id)))


class Wish(models.Model):
    outorder = models.ForeignKey(Outorder)
    creator = models.ForeignKey(User)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=5000, default='I want to rent it.')
    start_date = models.DateTimeField('date the user may want to rent out')
    end_date = models.DateTimeField('date the user may want to sent the item back')
    rating = models.PositiveSmallIntegerField(default=3)
    pub_date = models.DateTimeField('date published')
