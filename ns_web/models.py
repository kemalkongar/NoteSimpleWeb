from django.db import models
from django.contrib.auth.models import User


# More details about models can be found at:
# https://docs.djangoproject.com/en/2.2/ref/models/fields/

class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)  # 200 was chosen to cover most topic names.
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # Cascading delete: Deletes all corresponding entries
    # ForeignKey connects the information to another location in the database.
    # It indicates that entries are a subsidiary of Topics.
    text = models.TextField()  # Unlimited length.
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """This holds extra information for the Entry class."""
        verbose_name_plural = 'entries'
        # Without this line Django would refer to multiple entries as "Entrys"

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text}"
        # Which information to show when referring to individual entries.
        # First 50 characters are shown as the text can be longer. We also indicate that it may be longer.
