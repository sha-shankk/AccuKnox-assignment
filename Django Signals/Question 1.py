Question 1: Are Django signals executed synchronously or asynchronously by default?

Answer: By default, Django signals are run synchronously. This means they happen immediately when called and block the process until they finish.
Easy Example:

CODE SNIPPET

import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def user_created_signal(sender, instance, created, **kwargs):
    if created:
        print(f"Signal received for user: {instance.username}")
        time.sleep(5)  # Wait for 5 seconds to simulate a long process
        print("Signal handler finished.")

# This is where we create a new user
user = User.objects.create(username='testuser')
print("User created.")

Explanation:

    The signal (user_created_signal) runs right after creating the user.
    The time.sleep(5) causes a 5-second delay before the next line runs, showing that it waits for the signal to finish.

Expected Output:

sql

Signal received for user: testuser
(Wait 5 seconds...)
Signal handler finished.
User created.

This shows that signals are synchronous because the main process waits for the signal to complete.

