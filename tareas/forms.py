from django import forms
from django.forms import ModelForm

from .models import *


class FormTarea(forms.ModelForm):

    class Meta:
        model = Tarea
        fields = '__all__'

class FormTarea1(forms.ModelForm):

    class Meta:
        model = Tarea1
        fields = '__all__'

class FormTarea_mayo(forms.ModelForm):

    class Meta:
        model = Tarea_mayo
        fields = '__all__'

class FormTarea_marzo(forms.ModelForm):

    class Meta:
        model = Tarea_marzo
        fields = '__all__'        


class FormTarea_abril(forms.ModelForm):

    class Meta:
        model = Tarea_abril
        fields = '__all__'                

class FormTarea_junio(forms.ModelForm):

    class Meta:
        model = Tarea_junio
        fields = '__all__'                        

class FormTarea_julio(forms.ModelForm):

    class Meta:
        model = Tarea_julio
        fields = '__all__'                                

class FormTarea_agosto(forms.ModelForm):

    class Meta:
        model = Tarea_agosto
        fields = '__all__'                                        

class FormTarea_septiembre(forms.ModelForm):

    class Meta:
        model = Tarea_septiembre
        fields = '__all__'                                        

class FormTarea_octubre(forms.ModelForm):

    class Meta:
        model = Tarea_octubre
        fields = '__all__'                                        

class FormTarea_noviembre(forms.ModelForm):

    class Meta:
        model = Tarea_noviembre
        fields = '__all__'                                        

class FormTarea_diciembre(forms.ModelForm):

    class Meta:
        model = Tarea_diciembre
        fields = '__all__'                                        