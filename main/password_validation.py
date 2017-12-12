import enchant

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

class DictionaryPasswordValidator(object):
    """
    Validates whether the password is in the English dictionary
    """
    def validate(self, password, user=None):
        en_us = enchant.Dict("en_US")
        if en_us.check(password):
            raise ValidationError(
                _("This password is in the English dictionary."),
                code='password_in_dictionary',
            )
    def get_help_text(self):
        return _("Your password can't be in the English dictionary.")