from django.db import models


class Contact(models.Model):
    """ Save a contact message/model in the database """

    full_name = models.CharField(max_length=25, null=False, blank=False)
    email = models.EmailField(max_length=25, null=False, blank=False)
    message_subject = models.CharField(max_length=100, null=False, blank=False)
    message_body = models.TextField(max_length=1500, null=False, blank=False)
    date_sent = models.DateTimeField(auto_now_add=True)    
    
    def __str__(self):
        return self.message_subject

