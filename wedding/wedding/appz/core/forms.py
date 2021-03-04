from django import forms
from newbook.models import Destination
class Destform(forms.ModelForm):
    class Meta():
        model = Destination
        fields = "__all__"
            