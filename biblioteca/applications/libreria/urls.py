from django.urls import path, re_path

from . import views

app_name = "libreria_app"

urlpatterns = [
    path('', views.ListAuthor.as_view(), name="list-author"),
    path('books-author/<pk>/', views.ListBooksAuthor.as_view(), name="list-book"),
    path('add-author', views.AddAuthor.as_view(), name="add-author"),
]
