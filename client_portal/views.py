from django.shortcuts import render


def patient_information(request, slug):
    # slug == visit.id

    data = {
        'patient': {
            'name': "John" # visit.patient.last_name
        }
    }
    return render(request, template_name='client.html', context=data)
