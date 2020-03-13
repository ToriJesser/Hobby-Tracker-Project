from django.forms import ModelForm
from .models import LegoSet

#Create the form class.
class LegoSetForm(ModelForm):
    class Meta:
        model = LegoSet
        fields = '__all__'


