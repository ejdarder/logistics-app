import datetime

from django.db import models
from django.conf import settings
from django.utils import timezone

class Part (models.Model):
	part_description = models.CharField(max_length=50)
	part_number = models.CharField(max_length=10)
	part_supplier=models.CharField(max_length=20)
	add_date=models.DateTimeField('date added')
	part_stock=models.IntegerField(default=0)
	#part_id=models.IntegerField(primary_key=True)

	def __str__(self):
		return self.part_number

	def add_part(self):
		self.add_date=timezone.now()
		self.save()

# Field classes
# https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.ForeignKey

# class PO (models.Model):
# 	po_number = models.CharField(max_length=5)
# 	pn_ordered=models.ForeignKey(Part, on_delete=models.CASCADE)
# 	po_qty =models.IntegerField(default=1)
	
# 	def __str__(self):
# 		return self.po_number