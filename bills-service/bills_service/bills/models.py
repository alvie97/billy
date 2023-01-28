from django.db import models


class Bill(models.Model):
    """
    A bill is a statement of the money owned by a user for an expense.
    """

    user_id = models.CharField(max_length=36, blank=False, unique=True)
    title = models.CharField(max_length=32, blank=False, unique=False)
    description = models.CharField(max_length=256, blank=True, unique=False)
    expense = models.DecimalField(max_digits=9, decimal_places=2, null=False)
