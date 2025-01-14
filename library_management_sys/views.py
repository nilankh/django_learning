from rest_framework import viewsets
from .models import Book, Member, Loan
from .serializers import BookSerializer, MemberSerializer
from rest_framework import permissions
from rest_framework.permissions import AllowAny

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [AllowAny]