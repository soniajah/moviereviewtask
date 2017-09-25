from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Movies, Review
import logging
import json

# Create your views here.
def index(request):
    return HttpResponse("Wellcome to the Movie Reviews")

def getmovies(request):
    data = []
    q = Movies.objects.all()
    for i in q:
        data.append({'ID': i.id, 'Title': i.Title, 'Description': i.Description})
    return HttpResponse(json.dumps(data), content_type='application/json')

def getmoviereviews(request, question_id):
    data = []
    q = Review.objects.filter(MovieID=question_id)
    for i in range(0,len(q)):
        data.append({"ReviewTitle": q[i].ReviewTitle,
                         'ReviewContent': q[i].ReviewContent, 'Username': q[i].Username})
    return HttpResponse(json.dumps(data), content_type='application/json')

def addreview(request, question_id):
    q1 = request.GET.get('username', '')
    q2 = request.GET.get('reviewTitle', '')
    q3 = request.GET.get('reviewContent', '')
    movieId = Movies.objects.get(id = question_id)
    q = Review(MovieID= movieId, Username= q1, ReviewTitle= q2,ReviewContent = q3)
    q.save()
    return HttpResponse("ok")