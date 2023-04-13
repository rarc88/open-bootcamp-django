from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100,
                           help_text='Max 100 characters')
    url = forms.URLField(label='WebSite', required=False, initial='http://')
    comment = forms.CharField(label='Comment')


class ContactForm (forms.Form):
    textWidget = forms.TextInput(attrs={'class': 'form-control mt-4'})
    taxtAreaWidget = forms.Textarea(attrs={'class': 'form-control mt-4'})

    name = forms.CharField(label='Name', max_length=50,
                           widget=textWidget)
    email = forms.EmailField(label='Email', max_length=50,
                             widget=textWidget)
    message = forms.CharField(label='Message',
                              widget=taxtAreaWidget)

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if name.upper() != 'OPEN':
            raise forms.ValidationError(
                'the name cannot be different from Open')

        return name
