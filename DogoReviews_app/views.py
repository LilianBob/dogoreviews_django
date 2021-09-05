from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Book, Review
from .serializers import BookSerializer

def index (request):
    return HttpResponse ('under construction...')

@csrf_exempt
def bookApi(request, id=0):
    if request.method == 'GET':
        books= Book.objects.all()
        books_serializer= BookSerializer(books, many=True)
        return JsonResponse(books_serializer.data, safe=False)
    elif request.method == 'POST':
        book_data= JSONParser().parse(request)
        book_serializer= BookSerializer(data=book_data)
        if book_serializer.is_valid:
            book_serializer.save()
            return JsonResponse("Book successfully added", safe=False)
        return JsonResponse("Adding failed")
    elif request.method == 'PUT':
        book_data= JSONParser().parse(request)
        book=Book.objects.get(book=book_data['book_id'])
        book_serializer= BookSerializer(book, data=book_data)
        if book_serializer.is_valid:
            book_serializer.save()
            return JsonResponse("Update was successful", safe=False)
        return JsonResponse("Update failed")
    elif request.method == 'Delete':
        book_data= JSONParser().parse(request)
        book=Book.objects.get(id= book_data['book_id'])
        book.delete()
        return JsonResponse("Deleted successfully", safe=False)
