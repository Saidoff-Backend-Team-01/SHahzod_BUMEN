from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from subject.models import *
from subject.serializers import *
from rest_framework.generics import ListAPIView, ListCreateAPIView


class CategoryAPIView(APIView):
    def get(self, request, pk):
        categories = Category.objects.all().order_by('-clicked_count')
        # orderby clicked_count buyicha
        categories_serializer = CategorySerializer(categories, many=True)
        content = {
            'categories': categories_serializer.data,
        }
        return Response(content, status=status.HTTP_200_OK)


class StartSubjectApi(APIView):
    def get(self, request, subject_id):
        try:
            subject = Subject.objects.get(id=subject_id)
            serializer = SubjectSerializer(subject)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Subject.DoesNotExist:
            return Response({'error': 'Subject not found'}, status=status.HTTP_404_NOT_FOUND)


class StartSubjectAPIView(ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer





