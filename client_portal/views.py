from django.shortcuts import render
from backend.models import  *

def patient_information(request, slug):
    # slug == visit.id
    visit = Visit.objects.filter(id=slug).first()
    data = {
        'patient': {
            'name': visit.patient.last_name + ", " + visit.patient.first_name
        },
        'diagnosis': {
            'name': visit.diagnosis.diagnosis_name + "\n",
            'description': visit.diagnosis.diagnosis_description
        },
        'treatment': {
            'prescription': visit.treatment.prescription + "\nHow many days of treatment: " + visit.treatment.duration +
            "\nDosage: " + visit.treatment.dosage + "\nTime Between Usage: " + visit.treatment.cycle
        },
    }
    return render(request, template_name='client.html', context=data)
