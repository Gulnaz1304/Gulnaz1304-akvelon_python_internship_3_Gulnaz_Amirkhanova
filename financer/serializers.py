from rest_framework import serializers
from .models import User
from .models import Transaction


class Summ:
    """let us to to view sum of income/outcome """
    def __init__(self, date, sum):
        self.date = date
        self.sum = sum


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['user', 'amount', 'date']


class SumSerializer(serializers.Serializer):
    date = serializers.DateField()
    sum = serializers.IntegerField()





