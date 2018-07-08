from django import forms

from .models import ContractDB


class NewContract(forms.ModelForm):
	class Meta:
		model = ContractDB
		fields = ['ngo', 'project', 'milestone' , 'donor', 'amount',]
