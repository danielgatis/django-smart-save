import sys

from django.conf import settings
from django.db.models import Model
from django.core.exceptions import ValidationError, ImproperlyConfigured


SMART_SAVE_METHOD = getattr(settings, 'SMART_SAVE_METHOD', 'save_if_valid')


if SMART_SAVE_METHOD == 'save':
    raise ImproperlyConfigured("SMART_SAVE_METHOD can't be 'save'")


def save_if_valid(self, throw_exception=False, *args, **kwargs):
    """Make :meth:`save` call :meth:`full_clean`.

    Do you think Django models ``save`` method will validate all fields
    (i.e. call ``full_clean``) before saving or any time at all? Wrong!

    More info:

    * "Why doesn't django's model.save() call full clean?"
        http://stackoverflow.com/questions/4441539/
    * "Model docs imply that ModelForm will call Model.full_clean(),
        but it won't."
        https://code.djangoproject.com/ticket/13100

    """
    try:
        self.full_clean()
        self.save(*args, **kwargs)

        return True

    except ValidationError:
        e = sys.exc_info()[1]

        self._errors = {}
        for k, v in e.message_dict.items():
            self._errors[k] = v

        if throw_exception:
            raise

        return False


Model.add_to_class('_errors', {})
Model.add_to_class(SMART_SAVE_METHOD, save_if_valid)
