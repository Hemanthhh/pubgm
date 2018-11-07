from django import forms
from tournament.models import Data

class Enroll(forms.ModelForm):
    name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder' : 'Name',
            }
        )
    )
    whatsapp = forms.IntegerField(
        widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'minlength': 10,
                'maxlength': 10,
                'required': True,
                'type': 'number',
                'placeholder':'Whatsapp Number',
                'id':'whatsapp',
            }
        )
    )
    paytm = forms.IntegerField(
        widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'minlength': 10,
                'maxlength': 10,
                'required': True,
                'type': 'number',
                'placeholder':'Paytm Number',
                'id':'paytm',
            }
        )
    )
    pubg_uid = forms.IntegerField(
        widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'required': True,
                'placeholder':'PUBG Gamer ID',
            }
        )
    )
    pubg_uname = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'required': True,
                'placeholder':'PUBG Ingame Name',
            }
        )
    )

    class Meta:
        model = Data
        fields = ('name','whatsapp','paytm','pubg_uid','pubg_uname')