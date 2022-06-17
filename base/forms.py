from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    # Specify the data about the data of the form
    class Meta:
        # The model on which to create the form
        model = Room
        