from django import forms
from .models import Animals, Vid, Tip, Sotr, Dolznost
class AnimalsForm(forms.ModelForm):
    class Meta:
        model = Animals
        fields = ['Data_registr_v_zoo', 'Data_rozden', 'Klichka', 'photo',
                  'ID_Vid', 'ID_Tip', 'ID_Klimzona']
        widgets = {
            'Data_registr_v_zoo': forms.DateInput(attrs={'type': 'date'}),
            'Data_rozden': forms.DateInput(attrs={'type': 'date'}),
        }
class VidForm(forms.ModelForm):
    class Meta:
        model = Vid
        fields = ['Vid_animals']
class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ['Tip_animals']
class SotrForm(forms.ModelForm):
    class Meta:
        model = Sotr
        fields = ['FIO', 'Data_rozden', 'zp', 'Data_priema', 'photo',
                  'ID_Pol', 'ID_Dolznost', 'ID_categor']
        widgets = {
            'Data_rozden': forms.DateInput(attrs={'type': 'date'}),
            'Data_priema': forms.DateInput(attrs={'type': 'date'}),
        }
class DolznostForm(forms.ModelForm):
    class Meta:
        model = Dolznost
        fields = ['Naimenovanye', 'Obyazannosti']