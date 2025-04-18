from rest_framework.serializers import ModelSerializer

from users.models import User, Payment


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("email",)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('phone_number', 'city', 'avatar')


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
