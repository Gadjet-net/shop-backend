from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path('category/', CategoryList.as_view()),
    path('category/<int:pk>/', CategoryDetail.as_view()),
    path('subcategory/', SubcategoryList.as_view()),
    path('subcategory/<int:pk>/', SubcategoryDetail.as_view()),
    path('company/', CompanyList.as_view()),
    path('company/<int:pk>/', CompanyDetail.as_view()),
    path('product/', ProductList.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view()),
    path('users/', UsersList.as_view()),
    path('users/<int:pk>/', UsersDetail.as_view()),
    path('comments/', CommentsList.as_view()),
    path('comments/<int:pk>/', CommentsDetail.as_view()),
    path('order/', OrderList.as_view()),
    path('order/<int:pk>/', OrderDetail.as_view()),
    path('token-auth', obtain_auth_token),
]
