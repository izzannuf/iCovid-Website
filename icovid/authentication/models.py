import json

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_cas_ng.signals import cas_user_authenticated

LANG = settings.SSO_UI_ORG_DETAIL_LANG
ORG_CODE = {}
with open(settings.SSO_UI_ORG_DETAIL_FILE_PATH, 'r') as ORG_CODE_FILE:
  ORG_CODE.update(json.load(ORG_CODE_FILE))


@receiver(cas_user_authenticated)
def save_cas_user_attributes(user, attributes, **kwargs):
  """Save attributes for user that authenticated from CAS"""

  full_name = attributes.get('nama', 'mr. anonymous').split()
  user.first_name = full_name[0]
  user.last_name = full_name[-1]

  if (attributes.get('peran_user') == 'mahasiswa'):
    user.email = f'{user.username}@ui.ac.id'
  
  user.save()