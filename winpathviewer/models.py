"""
winpathviewer models.
"""
import datetime
import json

from django.db.models import fields
from django.utils.timezone import make_aware

from opal import models

class Demographics(models.Demographics): pass
class Location(models.Location): pass
class Allergies(models.Allergies): pass
class Diagnosis(models.Diagnosis): pass
class PastMedicalHistory(models.PastMedicalHistory): pass
class Treatment(models.Treatment): pass
class Investigation(models.Investigation): pass

class WinPathResult(models.EpisodeSubrecord):
    _read_only = True

    lab_number           = fields.CharField(max_length=200, blank=True, null=True)
    profile_code         = fields.CharField(max_length=200, blank=True, null=True)
    profile_description  = fields.CharField(max_length=200, blank=True, null=True)
    request_datetime     = fields.DateTimeField(blank=True, null=True)
    observation_datetime = fields.DateTimeField(blank=True, null=True)
    last_edited          = fields.DateTimeField(blank=True, null=True)
    result_status        = fields.CharField(max_length=200, blank=True, null=True)
    observations         = fields.TextField(blank=True, null=True)

    @classmethod
    def create_or_update_from_gloss(klass, identifier, data):
        lab_number = data['lab_number']
        print 'lab number', lab_number
        print 'identifier', identifier

        # First, check if we have this lab number...
        if klass.objects.filter(lab_number=lab_number).count() > 0:
            result = klass.objects.get(lab_number=lab_number)
            episode = result.episode
            if not episode.active:
                episode.active = True
                episode.save()
            patient = episode.patient

        else:

            patient, created = models.Patient.objects.get_or_create(
                demographics__hospital_number=identifier)
            if patient.episode_set.count() == 0:
                episode = patient.create_episode()
                episode.active = True
                episode.save()
            else:
                episode = patient.episode_set.first()
            result = klass(episode=episode, lab_number=lab_number)

        def date_from_key(prop):
            return make_aware(datetime.datetime.strptime(data[prop], '%Y/%m/%d %H:%M'))

        result.profile_code = data['profile_code']
        result.profile_description = data['profile_description']
        result.request_datetime = date_from_key('request_datetime')
        result.observation_datetime = date_from_key('observation_datetime')
        result.last_edited = date_from_key('last_edited')
        result.result_status = data['result_status']
        result.observations = data['observations']
        result.save()

        return

    def to_dict(self, user):
        d = super(WinPathResult, self).to_dict(user)
        d['observations'] = json.loads(self.observations)
        return d
