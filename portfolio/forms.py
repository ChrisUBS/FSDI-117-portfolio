from django import forms
from .models import project

# class ProjectForm(forms.Form):
#     name = forms.CharField(
#         max_length=256,
#         widget=forms.TextInput(attrs={"placeholder": "Project Name"})
#     )
#     description = forms.CharField(
#         widget=forms.Textarea(attrs={"placeholder": "Project Description"})
#     )
#     year = forms.IntegerField(
#         widget=forms.NumberInput(attrs={"placeholder": "Year"})
#     )
#     skills = forms.ModelMultipleChoiceField(
#         queryset=skill.objects.all(),
#         widget=forms.CheckboxSelectMultiple()
#     )
#     img = forms.ImageField()
#     web_link = forms.URLField(
#         widget=forms.URLInput(attrs={"placeholder": "Project Website Link"})
#     )

class ProjectForm(forms.ModelForm):
    class Meta:
        model = project
        fields = ["name", "description", "year", "skills", "img", "web_link"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Project Name"}),
            "description": forms.Textarea(attrs={"placeholder": "Description"}),
            "year": forms.NumberInput(attrs={"placeholder": "Year"}),
            "img": forms.ClearableFileInput(attrs={"placeholder": "Select and Image"}),
            "web_link": forms.URLInput(attrs={"placeholder": "Project Website Link"}),
            # "skills": forms.CheckboxSelectMultiple(attrs={"class": "skills-checkbox-grid"}),
            "skills": forms.SelectMultiple(attrs={
                    "size": "8", 
                    "style": "width: 100%;"
                }),
        }