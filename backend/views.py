from django.shortcuts import render

import requests

from backend.models import *


def send_to_twilio(id):
    visit = Visit.objects.filter(id = id).first()
    payload = \
    {
        "name": visit.patient.last_name + ", " + visit.patient.first_name,
        "phone_number": visit.patient.phone_number,
        "email": visit.patient.email,
        "url": id
    }

    if visit.treatment is None:
        payload["prescription"] = None
    else:
        payload["prescription"] = \
        {
            "treatment": visit.treatment.prescription,
            "high_priority": visit.treatment.high_priority,
            "duration": visit.treatment.duration,
            "dosage": visit.treatment.dosage,
            "cycle": visit.treatment.cycle
        }

    requests.post('10.0.0.1', payload=payload)

