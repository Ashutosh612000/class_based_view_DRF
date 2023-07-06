from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Course
from django.http import Http404
from api.serializer import CourseSerializer


# Create your views here.

class CourseListView(APIView):

    def get(self,request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses,many=True)
        json = serializer.data
        return Response(json)

    def post(self,request):
        courseSerializer = CourseSerializer(data= request.data)
        if courseSerializer.is_valid():
            courseSerializer.save()
            return Response(courseSerializer.data, status=status.HTTP_201_CREATED)
        return Response(courseSerializer.errors)

class CourseDetailView(APIView):

    def get_course(self,pk):
        try:
            return Course.objects.get(pk=pk)

        except Course.DoesNotExist:
            raise Http404

            

    def get(self,request,pk):
        course = self.get_course(pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)


    def delete(self,request,pk):
        course = self.get_course(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def put(self,request,pk):
        course = self.get_course(pk)
        courseSerializer = CourseSerializer(course,data = request.data)

        if courseSerializer.is_valid():
            courseSerializer.save()
            return Response(courseSerializer.data)
        return Response(courseSerializer.errors)
