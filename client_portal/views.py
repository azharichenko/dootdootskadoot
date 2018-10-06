from django.shortcuts import render


def patient_information(request, slug):
    return render(request, template_name='client.html')