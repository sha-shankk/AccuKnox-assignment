Question 2: Do Django signals run in the same thread as the caller?

Answer: Yes, Django signals run in the same thread as the code that calls them.
Easy Example:

*****python code:*****

import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def user_created_signal(sender, instance, created, **kwargs):
    if created:
        print(f"Signal is running in thread: {threading.current_thread().name}")


def create_user():
    print(f"User creation is running in thread: {threading.current_thread().name}")
    user = User.objects.create(username='testuser')

create_user()

Explanation:

    Both the user creation and the signal print the current thread name.
    Since the thread name will be the same, it means the signal runs in the same thread as the main process.


****Expected Output:****

arduino

User creation is running in thread: MainThread
Signal is running in thread: MainThread

This confirms that signals use the same thread as the code that triggers them.
