from django.forms import ModelForm
from .models import Service

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = [
            'seo',
            'content_marketing',
            'web_dev',
            'ux_design'
        ]
