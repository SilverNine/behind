from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers


# class ListAllImages(APIView):
#     def get(self, request, format=None):
#         all_images = models.Image.objects.all()
#         serializer = serializers.ImageSerializer(all_images, many=True)
#         return Response(data=serializer.data)


# class ListAllComments(APIView):
#     def get(self, request, format=None):
#         all_comments = models.Comment.objects.all()
#         serializer = serializers.CommentSerializer(all_comments, many=True)
#         return Response(data=serializer.data)


# class ListAllLikes(APIView):
#     def get(self, request, format=None):
#         all_likes = models.Like.objects.all()
#         serializer = serializers.LikeSerializer(all_likes, many=True)
#         return Response(data=serializer.data)


# class Feed(APIView):
#     def get(self, request, format=None):
#         user = request.user
#         following_users = user.following.all()

#         for following_user in following_users:
#             print(following_user.images.all())

#         return Response(status=200)

class Feed(APIView):

    def get(self, request, format=None):

        user = request.user

        following_users = user.following.all()

        image_list = []

        for following_user in following_users:
            user_images = following_user.images.all()[:2]

            for image in user_images:
                image_list.append(image)

        sorted_list = sorted(image_list, key=lambda image: image.created_at, reverse=True)

        serializer = serializers.ImageSerializer(sorted_list, many=True)

        return Response(serializer.data) 
        