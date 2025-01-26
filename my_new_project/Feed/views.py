from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from random import randint
from .seriallizers import PostSerializer


class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        q_params = request.query_params.get('filter[title][$in]', None)
        serializer = PostSerializer(posts, many=True)
        fillter_data = []
        #filtre by title
        if q_params:
            for post in serializer.data:
                if post['title'] not in q_params:
                    serializer.data.remove(post)

        else:
            fillter_data = serializer.data
         #create response
        return Response({
            "data": fillter_data,
            "meta": {
                "total": len(serializer.data)
            },
            "success": True
        }, status=status.HTTP_200_OK)

    def post(self, request):
        payload = request.data["data"]
        payload['document_id'] = randint(0, 100)
        serializer = PostSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "data": serializer.data,
                "meta": {},
                "success": True
            }, status=status.HTTP_201_CREATED)
        return Response({
            "data": None,
            "meta": {},
            "success": False,
            "error": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response({
            "data": serializer.data,
            "meta": {},
            "success": True,
        },status=status.HTTP_200_OK)

    def put(self, request, pk):
        post = Post.objects.get(pk=pk)
        #print("__post",post)
        #TODO: fix issue with required fields
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "data": serializer.data,
                "meta": {},
                "success": True,
            },status=status.HTTP_200_OK)
        return Response({
            "data": None,
            "meta": {},
            "success": False,
            "error": serializer.errors
        },status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response({
            "data": None,
            "meta": {},
            "success": True,
        },status=status.HTTP_200_OK)

