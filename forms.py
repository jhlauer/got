from django.forms import ModelForm
from APPNAME.models import Model_1

# Create the form class.
class TypeForm(ModelForm):
    class Meta:
        model = Model_1
        fields = '__all__'