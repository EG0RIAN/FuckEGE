import csv
from django.http import HttpResponse
from .models import Task, Message
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MessageSerializer


def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="answers.csv"'

    writer = csv.writer(response)
    writer.writerow(['Задание', 'Ответ'])

    for obj in Task.objects.all():
        writer.writerow([obj.task_num, obj.answer])

    return response


def index(request):
    return render(request, 'index.html')


def json_answers(request):
    data = list(Task.objects.values('task_num', 'answer'))
    return JsonResponse(data, safe=False)


@api_view(['POST'])
def post_message(request):
    if request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_BAD_REQUEST)