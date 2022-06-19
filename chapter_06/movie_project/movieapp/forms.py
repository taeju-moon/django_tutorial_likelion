from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label="Search for Movies", max_length=100)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)

        self.fields["search"].widget.attrs = {
            'class':'form-control',
            'placeholder':'enter the title',
            'rows':20,
        }