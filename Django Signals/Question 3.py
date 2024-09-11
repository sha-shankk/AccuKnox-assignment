Question 3: Do Django signals run in the same database transaction as the caller?

Answer: Yes, Django signals run in the same database transaction as the code that calls them. If the transaction fails, everything (including the signal) will be rolled back.
Easy Example:

*****python Code snippet******

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import connection

@receiver(post_save, sender=User)
def user_created_signal(sender, instance, created, **kwargs):
    if created:
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM auth_user")
        user_count = cursor.fetchone()[0]
        print(f"Number of users inside signal: {user_count}")

def create_user():
    with transaction.atomic():
        user = User.objects.create(username='testuser')
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM auth_user")
        user_count = cursor.fetchone()[0]
        print(f"Number of users inside transaction: {user_count}")
        raise Exception("Oops! Something went wrong, rolling back transaction.")

try:
    create_user()
except Exception as e:
    print(f"Transaction failed due to: {e}")

# Check the number of users after the rollback
cursor = connection.cursor()
cursor.execute("SELECT COUNT(*) FROM auth_user")
final_user_count = cursor.fetchone()[0]
print(f"Number of users after rollback: {final_user_count}")

Explanation:

    Inside the transaction, a user is created, and the signal is triggered.
    After the exception is raised, the transaction rolls back (meaning the user is not actually saved).
    Both inside the transaction and inside the signal, the number of users is counted.
    After the rollback, there are 0 users, showing that everything (including the signal's changes) was undone.

*****Expected Output:******

yaml

Number of users inside transaction: 1
Number of users inside signal: 1
Transaction failed due to: Oops! Something went wrong, rolling back transaction.
Number of users after rollback: 0

This shows that signals are part of the same transaction, and when the transaction fails, changes made by the signal are also rolled back.
