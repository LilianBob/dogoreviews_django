from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Book, Review
from .serializers import BookSerializer, ReviewSerializer

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
        book= Book.objects.get(bookId=book_data['bookId'])
        book_serializer= BookSerializer(book, data=book_data)
        if book_serializer.is_valid:
            book_serializer.save()
            return JsonResponse("Update was successful", safe=False)
        return JsonResponse("Update failed")
    elif request.method == 'Delete':
        book_data= JSONParser().parse(request)
        book= Book.objects.get(bookId=id)
        book.delete()
        return JsonResponse("Deleted successfully", safe=False)

@csrf_exempt
def saveImage(request):
    file= Book(file= request.Files['cover'])
    file.save()
    return JsonResponse("Cover file successfully added!")

@csrf_exempt
def reviewApi(request, id=0):
    if request.method=='GET':
        reviews = Review.objects.all()
        reviews_serializer = ReviewSerializer(reviews, many=True)
        return JsonResponse(reviews_serializer.data, safe=False)

    elif request.method=='POST':
        review_data=JSONParser().parse(request)
        review_serializer = ReviewSerializer(data=review_data)
        if review_serializer.is_valid():
            review_serializer.save()
            return JsonResponse("Review added successfully!!" , safe=False)
        return JsonResponse("Failed to add review.", safe=False)
    
    elif request.method=='PUT':
        review_data = JSONParser().parse(request)
        review=Review.objects.get(review_id=review_data['review_id'])
        review_serializer=ReviewSerializer(review,data=review_data)
        if review_serializer.is_valid():
            review_serializer.save()
            return JsonResponse("Review Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        review=Review.objects.get(review_id=id)
        review.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)