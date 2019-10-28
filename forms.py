from django.forms import ModelForm
from got.models import House, Culture, Title

# Create the form class.
class HouseForm(ModelForm):
    class Meta:
        model = House
        fields = '__all__'

class CultureForm(ModelForm):
    class Meta:
        model = Culture
        fields = '__all__'

class TitleForm(ModelForm):
    class Meta:
        model = Title
        fields = '__all__'