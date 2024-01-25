from django import forms

from django import forms
from .models import Branch,District,applicationform



class LocationForm(forms.Form):

    district = forms.ModelChoiceField(queryset=District.objects.all(),
        widget=forms.Select(attrs={
            "hx-get": "load_cities/", "hx-target": "#id_branch","class":"form-control"}))
    branch = forms.ModelChoiceField(queryset=Branch.objects.none(),
                                    widget=forms.Select(attrs={"class":"form-control"}))



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if "district" in self.data:
            district_id = int(self.data.get("district"))
            self.fields["branch"].queryset = Branch.objects.filter(district_id=district_id)
