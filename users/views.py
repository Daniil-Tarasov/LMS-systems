from rest_framework.generics import UpdateAPIView, CreateAPIView, ListAPIView, RetrieveAPIView

from users.models import User, Payment
from users.serializers import UserSerializer, PaymentSerializer, UserRegisterSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserRegisterSerializer


class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentCreateAPIVew(CreateAPIView):
    serializer_class = PaymentSerializer


class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentRetrieveAPIView(RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
