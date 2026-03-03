from django.urls import path
from .views import (
    AuthorListCreateAPIView, AuthorRetrieveUpdateDestroyAPIView,
    MembersListCreateAPIView, MembersRetrieveUpdateDestroyAPIView,
    BooksListCreateAPIView, BooksRetrieveUpdateDestroyAPIView,
    BorrowRecordsListCreateAPIView, BorrowRecordsRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    # React calls: .../api/v1/author/
    path('author/', AuthorListCreateAPIView.as_view(), name='author-list'),
    path('author/<int:pk>/', AuthorRetrieveUpdateDestroyAPIView.as_view(), name='author-detail'),

    # React calls: .../api/v1/members/
    path('members/', MembersListCreateAPIView.as_view(), name='members-list'),
    path('members/<int:pk>/', MembersRetrieveUpdateDestroyAPIView.as_view(), name='members-detail'),

    # React calls: .../api/v1/books/
    path('books/', BooksListCreateAPIView.as_view(), name='books-list'),
    path('books/<int:pk>/', BooksRetrieveUpdateDestroyAPIView.as_view(), name='books-detail'),

    # React calls: .../api/v1/borrow-records/
    path('borrow-records/', BorrowRecordsListCreateAPIView.as_view(), name='borrow-records-list'),
    path('borrow-records/<int:pk>/', BorrowRecordsRetrieveUpdateDestroyAPIView.as_view(), name='borrow-records-detail'),
]