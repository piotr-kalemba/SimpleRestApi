from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer


class HomeView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request):
        book = Book()
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookView(APIView):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        serializer = BookSerializer(book, context={'request': request})
        return Response(serializer.data)

    def delete(self, request, id):
        book = Book.objects.get(id=id)
        book.delete()
        return Response(status=status.HTTP_204_NON_CONTENT)

    def put(self, request, id):
        book = Book.objects.get(id=id)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

