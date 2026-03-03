from rest_framework import serializers
from .models import Author, Members, Books, BorrowRecords

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'author_name', 'email']

class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ['id', 'name', 'email', 'phone_number']

class BooksSerializer(serializers.ModelSerializer):
    # 'author' handles the ID for POST/PATCH requests
    # 'author_name' provides the string for your frontend tables
    author_name = serializers.ReadOnlyField(source='author.author_name')

    class Meta:
        model = Books
        fields = ['id', 'title', 'author', 'author_name']

class BorrowRecordsSerializer(serializers.ModelSerializer):
    # These read-only fields show names in your table
    member_name = serializers.ReadOnlyField(source='member.name')
    book_title = serializers.ReadOnlyField(source='book.title')

    class Meta:
        model = BorrowRecords
        # Include 'member' and 'book' (IDs) for saving, and the names for viewing
        fields = [
            'id', 'borrow_date', 'return_date', 
            'member', 'book', 'member_name', 'book_title'
        ]
        read_only_fields = ['borrow_date']