import uuid

from django.db import models
from django.utils.crypto import get_random_string


def get_random_string_value():
    return get_random_string(length=32)



class BaseModel(models.Model):
    """
    An abstract base class model that provides self-updating
    `created` and `modified` fields and overrides the id field to be a UUID field.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    updated_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # Manually append `modified_at` to the field list if `update_fields`
        # argument is sent while saving the instance.
        if kwargs.get('update_fields'):
            kwargs.update(
                {
                    'update_fields': kwargs.get('update_fields').append('modified_at'),
                }
            )
        return super().save(*args, **kwargs)
    

class APIKey(BaseModel):
    """
    Model for storing the API keys for authenticating the requests
    """

    api_key = models.UUIDField(
        db_index=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    api_secret_key = models.CharField(
        max_length=32,
        default=get_random_string_value,
        editable=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        verbose_name = 'API Keys'
        verbose_name_plural = 'API Keys'
