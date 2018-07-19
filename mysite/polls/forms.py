from django import forms

class QuesForm(forms.Form):
    question = forms.CharField(widget=forms.Textarea)
    Choice_1=forms.CharField(max_length=100)
    Choice_2=forms.CharField(max_length=100)
    Choice_3=forms.CharField(max_length=100)

class EditQues(forms.Form):
    question_edit=forms.CharField(widget=forms.Textarea, label='Question')
    
