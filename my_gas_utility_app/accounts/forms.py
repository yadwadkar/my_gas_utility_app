from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Customer

class CustomerRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    address = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username', 'email', 'address', 'phone_number', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True  # Set the user as a customer
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            customer = Customer.objects.create(
                user=user,
                address=self.cleaned_data['address'],
                phone_number=self.cleaned_data['phone_number']
            )
        return user
