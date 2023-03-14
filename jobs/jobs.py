from users.models import User
from books.serializers import BookSerializer

from loans.models import Loan

from django.core.mail import send_mass_mail
from django.conf import settings


def emails_data():
    email_list = []
    users = User.objects.all()

    for user in users:
        user_email = []
        template_message = f"Olá, {user.first_name}! A seguir você pode conferir a lista dos seus livros preferidos que estão disponíveis para empréstimo:"

        user_email.append(user.email)
        followed_books = user.books.all()

        if len(followed_books) == 0:
            continue

        for index, book in enumerate(followed_books):
            copies = book.copies.filter(is_loaned=False)

            if len(copies) == 0:
                continue

            serializer = BookSerializer(book)

            book_title = serializer.data["title"]
            book_author = serializer.data["author"]
            book_genre = serializer.data["genre"] or "Não identificado"
            book_string = f"\n {index + 1} - {book_title} \n Autor(a): {book_author} \n Gênero: {book_genre}"
            template_message = template_message + book_string

            email_list.append(
                tuple(
                    [
                        "Biblioteca Bates | Livros disponíveis para empréstimo",
                        template_message,
                        settings.EMAIL_HOST_USER,
                        user_email,
                    ]
                )
            )

    return email_list


def send_follow_emails():
    emails = emails_data()
    send_mass_mail(emails, fail_silently=False)


def block_users():
    # active_loans = Loan.objects.filter(is_active=True)
    # print(active_loans)
    ...
