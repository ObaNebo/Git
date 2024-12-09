from django.http import JsonResponse

def book_list(request):
    books = [
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
        {"title": "1984", "author": "George Orwell"}
    ]
    return JsonResponse({"books": books})
