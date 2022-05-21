from django.forms.models import ModelForm
from .models import Student, Presence
from django import forms

class StudentForm(ModelForm):

    class Meta:
        model = Student


        fields = (

            "first_name",
            "last_name",
            "birth_date",
            "email",
            "phone",
            "comments",
            "cursus",
        )
class PresenceParticularForm(ModelForm):

    class Meta:
        model = Presence


        fields = (
            "reason",
            "isMissing",
            "student",
            "date",
            'start_time',
            'stop_time',
        )
class PresenceForm(forms.Form):

    date = forms.DateInput()

    choices = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
    )

