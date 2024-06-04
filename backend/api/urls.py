from rest_framework.routers import DefaultRouter
from api.user.views import UserViewSet, CompanyViewSet, AddressViewSet
from api.post.views import PostViewSet
from api.comment.views import CommentViewSet
from api.album.views import AlbumViewSet
from api.photo.views import PhotoViewSet
from api.todo.views import TaskViewSet

api_router = DefaultRouter()

api_router.register("users", UserViewSet)
api_router.register("companies", CompanyViewSet)
api_router.register("address", AddressViewSet)
api_router.register("posts", PostViewSet)
api_router.register("comments", CommentViewSet)
api_router.register("albums", AlbumViewSet)
api_router.register("photos", PhotoViewSet)
api_router.register("todos", TaskViewSet)