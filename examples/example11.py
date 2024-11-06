books = ['System Design', 'Python и DevOps', 'Git. Практическое руководство']

def book_list(books, func):
    for book in books:
        print(func(book))

def book_print(book):
    if book.startswith('P'):
        return book.upper() + ' - прочитано'
    else:
        return book.lower() + ' - не прочитано'

book_list(books, book_print)