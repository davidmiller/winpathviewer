"""
Patient lists for the winpathviewer
"""
from opal.core import patient_lists
from opal.models import Episode

from winpathviewer import models

class WithResultsList(patient_lists.PatientList):

    @classmethod
    def slug(klass):
        return 'with-results'

    schema = [
        models.Demographics,
        models.WinPathResult
    ]

    def get_queryset(self):
        return Episode.objects.all()
