from rest_framework import viewsets
from .models import Book, Member, Loan
from .serializers import BookSerializer, MemberSerializer, LoanSerializer
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [AllowAny]


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [AllowAny]

    @action(detail=True, methods=['patch'])
    def mark_as_returned(self, request, pk=None):
        loan = self.get_object()
        print('line 29', loan)
        return
        loan.returned = True
        loan.return_date = request.data.get("return_date")
        loan.save()
        return Response({"status": "Loan marked as returned."})
