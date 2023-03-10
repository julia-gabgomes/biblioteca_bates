from datetime import datetime

from users.models import User
from books.serializers import BookSerializer

from django.core.mail import send_mass_mail
from django.conf import settings


# carderanhenrique@gmail.com


def emails_data():

    email_list = []

    users = User.objects.all()

    for user in users:
        user_email = []
        available_books = []
        # template_message

        result = [
            "Biblioteca Bates | Livros disponíveis para empréstimo",
            available_books,
            settings.EMAIL_HOST_USER,
            user_email,
        ]

        user_email.append(user.email)

        followed_books = user.books.all()
        # validação -> segue algum livro

        if len(followed_books) > 0:
            for book in followed_books:
                copies = book.copies.all()
                # filter

                for copy in copies:
                    if copy.is_loaned == False:
                        serializer = BookSerializer(book)
                        available_books.append(serializer.data)

            email_list.append(tuple(result))

    return email_list


# message = "Olá, user.email! A seguir você pode conferir a lista de livros disponíveis para empréstimo:"


"""
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
"""


def schedule_follow_emails():
    emails = emails_data()
    print(emails)
    send_mass_mail(emails, fail_silently=False)


"""
OBJETIVO:
- tupla de dados de envio

formato dos dados de envio:
# (
#     subject,
#     corpo,
#     settings.EMAIL_HOST_USER,
#     ["user@mail.com"],
# )
"""
