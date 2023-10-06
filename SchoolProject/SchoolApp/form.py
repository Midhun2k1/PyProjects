from django import forms
from .models import Department, Course, Material, FormSubmission


class FormSubmissionForm(forms.ModelForm):
    class Meta:
        model = FormSubmission
        fields = '__all__'

    department = forms.ModelChoiceField(queryset=Department.objects.all())
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    materials_provided = forms.ModelMultipleChoiceField(queryset=Material.objects.all(), widget=forms.CheckboxSelectMultiple)
