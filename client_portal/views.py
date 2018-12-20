from django.shortcuts import render
from backend.models import  *

from pprint import pprint

def patient_information(request, slug):
    # slug == visit.id
    visit = Visit.objects.filter(id=slug).first()
    data = {
        'patient': {
            'name': visit.patient.last_name + ", " + visit.patient.first_name
        },
        'doctor': {
            'name': "Dr. " + visit.doctor.first_name + " " + visit.doctor.last_name,
            'phone_number': visit.doctor.phone_number,
            'email': visit.doctor.email
        },
        'diagnosis': [d.to_dict() for d in visit.diagnosis.all()],
        'treatment': [d.to_dict() for d in visit.treatment.all()],
        'environment': [env.to_dict() for d in visit.diagnosis.all() for env in d.environment_warnings.all()] +
                    [env.to_dict() for d in visit.treatment.all() for env in d.environment_warnings.all()],
        'activity': [act.to_dict() for d in visit.diagnosis.all() for act in d.activity_warnings.all()] +
                    [act.to_dict() for d in visit.treatment.all() for act in d.activity_warnings.all()],
        'diet': [diet.to_dict() for d in visit.diagnosis.all() for diet in d.diet_change.all()] +
                [diet.to_dict() for d in visit.treatment.all() for diet in d.diet_change.all()],
    }
    pprint(data)
    return render(request, template_name='client.html', context=data)
