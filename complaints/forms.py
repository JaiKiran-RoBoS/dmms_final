from django.forms import ModelForm
from .models import Complaint, Complaint_Transformer


class ComplaintForm(ModelForm):
	class Meta:
		model = Complaint
		fields = ['complaint_type','complaint_category','complaint_nature','email','phone']

class ComplaintUpdateForm(ModelForm):
	class Meta:
		model = Complaint
		fields = '__all__'
		readonly_fields = ['complaint_id']

class ComplaintTransForm(ModelForm):
	class Meta:
		model = Complaint_Transformer
		fields = ['complaint_trans','complaint_nature','email','phone']


class ComplaintTransUpdateForm(ModelForm):
	class Meta:
		model = Complaint_Transformer
		fields = '__all__'
		readonly_fields = ['complaint_id']
