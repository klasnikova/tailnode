from django import forms
from .models import Index_Section, Service_Excellence, Projects, SocialMedia, Settings

class IndexSectionFormA(forms.ModelForm):
    class Meta:
        model = Index_Section
        fields = ['section_a_text_1', 'section_a_text_2']

class IndexSectionFormB(forms.ModelForm):
    class Meta:
        model = Index_Section
        fields = ['section_b_text_1', 'section_b_text_2']

class IndexSectionFormC(forms.ModelForm):
    class Meta:
        model = Index_Section
        fields = ['section_c_text_1', 'section_c_text_2']

class IndexSectionFormD(forms.ModelForm):
    class Meta:
        model = Index_Section
        fields = ['section_d_text_1', 'section_d_text_2']

class ServiceExcellenceForm(forms.ModelForm):
    class Meta:
        model = Service_Excellence
        fields = ['service_excellence_name', 'service_excellence_description']
        widgets = {
            'service_excellence_name': forms.TextInput(attrs={'class': 'form-input'}),
            'service_excellence_description': forms.Textarea(attrs={'class': 'form-textarea'}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['project_name', 'project_description', 'project_icon_url', 'project_exploler_url', 'project_date', 'project_status', 'exploler_button', 'visibility']
        widgets = {
            'project_date': forms.DateInput(attrs={'type': 'date', 'class': 'block w-full rounded p-2 outline-none bg-gray-100 dark:text-white dark:bg-slate-900 text-base border-b-gray-600 placeholder-gray-500 text-gray-900'}),
            'project_status': forms.CheckboxInput(attrs={'class': 'peer sr-only'}),
            'exploler_button': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
            'visibility': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }

class SocialMediaForm(forms.ModelForm):
    class Meta:
        model = SocialMedia
        fields = ['social_url', 'social_visibility']
        widgets = {
            'social_url': forms.TextInput(attrs={'class': 'form-input'}),
            'social_visibility': forms.CheckboxInput(attrs={'class': 'form-checkbox'})
        }

class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ['text_content_select', 'text_input_edit_blinking', 'socialmedia_navbar', 'contact_us_url']
        widgets = {
            'text_content_select': forms.CheckboxInput(attrs={'class': 'peer sr-only'}),
            'text_input_edit_blinking': forms.Select(attrs={'class': 'form-select'}),
            'socialmedia_navbar': forms.Select(attrs={'class': 'form-select'}),
            'contact_us_url': forms.TextInput(attrs={'class': 'form-input'}),
        }

class ChangeCredentialPasswordForm(forms.Form):
    new_password = forms.CharField(label='Password Baru', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Konfirmasi Password Baru', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if new_password != confirm_password:
            raise forms.ValidationError('New password and confirm password does not match')

        return cleaned_data


