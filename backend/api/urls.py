from rest_framework.routers import DefaultRouter
from api.user.views import UserViewSet, CompanyViewSet, AddressViewSet
from api.post.views import PostViewSet
from api.comment.views import CommentViewSet
from api.album.views import AlbumViewSet
from api.photo.views import PhotoViewSet
from api.todo.views import TaskViewSet

api_router = DefaultRouter()

api_router.register("users", UserViewSet, basename="users")
api_router.register("companies", CompanyViewSet, basename="company")
api_router.register("address", AddressViewSet, basename="address")
api_router.register("posts", PostViewSet, basename="posts")
api_router.register("comments", CommentViewSet, basename="comment")
api_router.register("albums", AlbumViewSet, basename="album")
api_router.register("photos", PhotoViewSet, basename="photo")
api_router.register("todos", TaskViewSet, basename="todo")