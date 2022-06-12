from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import uuid
# Create your models here.


TYPES = (
    ('Customer Complaints','Customer Complaints'),
    ('Section Initiated Complaints', 'Section Initiated Complaints'),
)

STATUS = (
    ('Pending','Pending'),
    ('Completed', 'Completed'),
)


CATEGORY_CHOICES = (
    ('HT','HT'),
    ('LT', 'LT'),
)

TRANS_CHOICES = (
    ('Transformer 1','Transformer 1'),
    ('Transformer 2','Transformer 2'),
    ('Transformer 3','Transformer 3'),
    ('Transformer 4','Transformer 4'),
    ('Transformer 5','Transformer 5'),
    ('Transformer 6','Transformer 6'),
    ('Transformer 7','Transformer 7'),
)
CATEGORY_NATURE = (
    ('Touching','Touching'),
    ('Creepings', 'Creepings'),
    ('Low Hanging Conductor','Low Hanging Conductor'),
    ('Damaged Insulator', 'Damaged Insulator'),
    ('Slanted Pole','Slanted Pole'),
    ('Damaged Pole', 'Damaged Pole'),
    ('Damaged Line AB Switch','Damaged Line AB Switch'),
    ('Clearance Issue', 'Clearance Issue'),
    ('Broken Stay','Broken Stay'),
    ('Damaged Strut', 'Damaged Strut'),
)

CATEGORY_NATURE_TRANS = (
    ('Damaged Transformer AB', 'Damaged Transformer AB'),
    ('Damaged LAs', 'Damaged LAs'),
    ('Damaged DO Set', 'Damaged DO Set'),
    ('Damaged HT drops', 'Damaged HT drops'),
    ('HT Bush Damaged', 'HT Bush Damaged'),
    ('LT Bush Damaged', 'LT Bush Damaged'),
    ('Oil Leakage', 'Oil Leakage'),
    ('Burned LT cables', 'Burned LT cables'),
    ('Damaged Fuse units', 'Damaged Fuse units'),
    ('Yard cleaning Required', 'Yard cleaning Required'),
    ('Earthing required', 'Earthing required'),
    ('Load unbalance', 'Load unbalance'),
    ('Body painting', 'Body painting'),
    ('Low Oil Level', 'Low Oil Level'),
    ('Damaged Breather', 'Damaged Breather'),
)
class Complaint(models.Model):
    complaint_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    complaint_type = models.CharField(max_length=30, null=True, choices=TYPES, default='Customer Complaints')
    complaint_category = models.CharField(max_length=20, null=True, choices=CATEGORY_CHOICES, default='HT')
    complaint_nature = models.CharField(max_length=40, null=True, choices=CATEGORY_NATURE, default='Touching')
    email = models.EmailField(max_length=254, null=True)
    phone = PhoneNumberField(unique = False, null = False, blank = False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=30, null=True, choices=STATUS, default='Pending')
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.complaint_type) + ": "+ self.complaint_category + " | "+ self.complaint_nature + " | "+ self.email

class Complaint_Transformer(models.Model):
    complaint_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    complaint_trans = models.CharField(max_length=20, null=True, choices=TRANS_CHOICES, default='Transformer 1')	
    complaint_nature = models.CharField(max_length=40, null=True, choices=CATEGORY_NATURE_TRANS, default='Damaged Transformer AB')
    email = models.EmailField(max_length=254, null=True)
    phone = PhoneNumberField(unique = False, null = False, blank = False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=30, null=True, choices=STATUS, default='Pending')
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	
    def __str__(self):
        return str("Transformer Maintenance") + ": "+ self.complaint_trans + " | "+ self.complaint_nature + " | "+ self.email
