from django.forms import ModelForm
from main.models import user_apps
        
class user_apps_f(ModelForm):
    class Meta:
        model = user_apps
        fields =['programing_language','app_name','description','code']