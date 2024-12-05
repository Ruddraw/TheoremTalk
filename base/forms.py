#base/forms.py

from django import forms
from .models import Reply

class ReplyForm(forms.ModelForm):
  class Meta:
    model = Reply
    fields = ['text']
    widgets = {
      'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your reply...'}),
    }
