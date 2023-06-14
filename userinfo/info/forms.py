from django import forms
from  info.models import User ,UserDoc

class SignupForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'})
        
    )
    class Meta:
        model = User
        fields = ('full_name','phone_number','address', 'email', 'username','password','password2','is_superuser', 'is_staff')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'full_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control'}),
         }
        

    def clean_password2(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password1

   
class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Username'})
    )
    # email = forms.EmailField(
    #     widget= forms.TextInput()
    # )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'})
    )

    



# user info update
class InfoUpdateForm(forms.ModelForm):
    address=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}),error_messages={'unique': 'phone number already exist'})
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),error_messages={'unique': 'username already exist'})
     
    class Meta:
          model = User
          fields = ('full_name','phone_number','address', 'email', 'username','is_superuser', 'is_staff')
          
          widgets = {
                'full_name':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.TextInput(attrs={'class':'form-control'}),
            }
          



class UserDocsForm(forms.ModelForm):
    # docs_image_url = forms.TextInput(attrs={'id':'bbox_coordinate'})

    # username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    # password2 = forms.CharField(
    #     widget=forms.PasswordInput(attrs={'class':'form-control'})
    # )
    # password = forms.CharField(
    #     widget=forms.PasswordInput(attrs={'class':'form-control'})
        
    # )
    class Meta:
        model = UserDoc
        fields = ['bbox','docs_image_url','doc_type']
        widgets = {
                'bbox':forms.TextInput(attrs={'class':'form-control','id':'bbox_coordinate'}),
                'docs_image_url':forms.FileInput(attrs = {'id':'imageUrlInput'}),
                'doc_type':forms.TextInput(attrs={'class':'form-control'}),
                'user':forms.TextInput(attrs={'class':'form-control'}),
            }
          
        # widgets = {
        #     'username':forms.TextInput(attrs={'class':'form-control'}),
        #     'full_name':forms.TextInput(attrs={'class':'form-control'}),
        #     'email':forms.TextInput(attrs={'class':'form-control'}),
        #     'address':forms.TextInput(attrs={'class':'form-control'}),
        #     'phone_number':forms.TextInput(attrs={'class':'form-control'}),
        #  }