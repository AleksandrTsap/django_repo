from django.contrib.auth import get_user_model

from authapp.forms import ShopUserChangeForm


class AdminShopUpdateUser(ShopUserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email', 'first_name',
                  'last_name', 'age', 'avatar',
                  'is_staff', 'is_active', 'is_superuser')
