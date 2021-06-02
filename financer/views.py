from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Transaction
from .serializers import UserSerializer, TransactionSerializer, SumSerializer, Summ
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=["POST"], detail=False)
    def all_transactions(self, request):
        """method to get all transactions that particular User ever done"""
        user_id = request.data["user"]
        user = User.objects.get(id=user_id)
        user_transactions = user.transactions.all()
        serializer = TransactionSerializer(user_transactions, many=True)

        return Response(serializer.data)

    @action(methods=["POST"], detail=False)
    def transactions_sum_of_date(self, request):
        """ method let us know if we are in plus or minus at particular day"""
        user = User.objects.get(id=request.data["user"])
        user_transactions = user.transactions.all()
        user_transaction_by_date = user_transactions.filter(date=request.data["date"])
        spended = user_transaction_by_date.aggregate(Sum('amount'))
        result = Summ(request.data["date"], spended.get('amount__sum'))
        serializer = SumSerializer(result)
        return Response(serializer.data)

    @action(methods=["POST"], detail=False)
    def filter_users_by_transaction_date(self, request):
        """show users that has transactions at particular day"""
        users = User.objects.filter(transactions__date=request.data["date"])
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    @action(methods=["POST"], detail=False)
    def filter_users_by_transaction_type(self, request):
        """shows us users that have in or out transactions depending on input"""
        type = request.data["type"] # type of transaction "in"- with +, out- with-
        if type == "in":
            users = User.objects.filter(transactions__amount__gt=0)
        else:
            users = User.objects.filter(transactions__amount__lt=0)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @action(methods=["POST"], detail=False)
    def filter_transactions_by_date(self, request):
        """returns all transactions that was made in particular day"""
        transactions = Transaction.objects.all().filter(date=request.data["date"])
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    @action(methods=["POST"], detail=False)
    def filter_transactions_by_type(self, request):
        """return only income or outcome transactions"""
        transactions = Transaction.objects.all()
        type = request.data["type"]
        if type == "in" :
            transactions = transactions.filter(amount__gt=0)
        else:
            transactions = transactions.filter(amount__lt=0)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    @action(methods=["GET"], detail=False)
    def order_transactions_by_date(self, request):
        """orders transactions by date"""
        transactions = Transaction.objects.all()
        ordered_transactions = transactions.order_by("date")
        serializer = TransactionSerializer(ordered_transactions, many=True)
        return Response(serializer.data)

    @action(methods=["GET"], detail=False)
    def order_transactions_by_amount(self, request):
        """orders transactions by amount"""
        transactions = Transaction.objects.all()
        transactions.filter(id)
        ordered_transactions = transactions.order_by("amount")
        serializer = TransactionSerializer(ordered_transactions, many=True)
        return Response(serializer.data)
