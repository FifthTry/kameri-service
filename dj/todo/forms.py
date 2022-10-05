from django import forms


class AddTodoForm(forms.Form):
    title = forms.CharField(label='title', max_length=100, required=True)
    status = forms.CharField(label='status', max_length=100, required=True)
    description = forms.CharField(label='description', required=True)
