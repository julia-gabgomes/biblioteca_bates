from users.models import User
from users.serializers import UserSerializer
from books.serializers import BookSerializer

from loans.models import Loan
from loans.serializers import LoanSerializer

from django.core.mail import send_mass_mail
from django.conf import settings

from datetime import datetime, date, timezone


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
    active_loans = Loan.objects.filter(is_active=True)

    for loan in active_loans:
        today_date = datetime.now(timezone.utc)
        expected_return = loan.expected_return

        if today_date > expected_return:
            loan.is_delayed = True
            loan.save()

            user_id = loan.user.id
            user = User.objects.get(id=user_id)
            user.is_blocked = True
            user.save()


def unblock_users():
    blocked_users = User.objects.filter(is_blocked=True)

    for user in blocked_users:
        blocked_until = user.blocked_until

        today_date = date.today()
        blocked_until_date = datetime.strptime(blocked_until, "%Y-%m-%d").date()

        if blocked_until_date == today_date:
            user.is_blocked = False
            user.save()
