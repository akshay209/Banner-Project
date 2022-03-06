from django import forms
from .models import Banner

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['position','start_date','end_date','end_time','banner_type','image']
        widgets = {
            'position' : forms.NumberInput(attrs={'class':'form-control','id':'position'}),
            'start_date' : forms.DateInput(attrs={'class':'form-control','id':'start_date'}),
            'end_date' : forms.DateInput(attrs={'class':'form-control','id':'end_date'}),
            'end_time' : forms.TimeInput(attrs={'class':'form-control','id':'end_time'}),
            'banner_type' : forms.TextInput(attrs={'class':'form-control','id':'type'}),


        }
    