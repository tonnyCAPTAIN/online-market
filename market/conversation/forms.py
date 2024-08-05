from django import forms

from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ['content',]
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border',
                # 'placeholder': 'Enter message here ...',
                # 'style': 'border: 1px solid #ccc; min-height: 100px; background-color: #fff;',
            })
        }


