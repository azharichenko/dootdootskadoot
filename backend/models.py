from django.db import models


# Diet Changes
class Diet(models.Model):
    encouraged = models.BooleanField(default=False)
    activity = models.CharField(max_length=256)
    purpose = models.CharField(max_length=2048)

    def __str__(self):
        return self.activity

    class Meta:
        ordering = ["activity"]


# Environment Warnings
class Environment(models.Model):
    encouraged = models.BooleanField(default=False)
    activity = models.CharField(max_length=256)
    purpose = models.CharField(max_length=2048)

    def __str__(self):
        return self.activity

    class Meta:
        ordering = ["activity"]


# Activity Warnings
class Actions(models.Model):
    encouraged = models.BooleanField(default=False)
    activity = models.CharField(max_length=256)
    purpose = models.CharField(max_length=2048)

    def __str__(self):
        return self.activity

    class Meta:
        ordering = ["activity"]


class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    twilio_number = models.CharField(max_length=50, null=True)

    def __str__(self):
        return "Dr. " + self.first_name + " " + self.last_name + " ID: " + str(self.id)

    class Meta:
        ordering = ["last_name", "first_name"]


class Diagnosis(models.Model):
    diagnosis_name = models.CharField(max_length=256)
    diagnosis_description = models.CharField(max_length=2048)
    diet_change = models.ManyToManyField(Diet, blank=True, null=True)
    environment_warnings = models.ManyToManyField(Environment, blank=True, null=True)
    activity_warnings = models.ManyToManyField(Actions, blank=True, null=True)

    def __str__(self):
        return self.diagnosis_name

    def to_dict(self):
        return  {
            'name': self.diagnosis_name,
            'description': self.diagnosis_description
        }

    class Meta:
        ordering = ["diagnosis_name"]


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    primary_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=True, null=True)
    id = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.last_name + ", " + self.first_name + " ID: " + self.id

    class Meta:
        ordering = ["last_name", "first_name"]


class Treatment(models.Model):
    prescription = models.CharField(max_length=256)
    high_priority = models.BooleanField(default=False)
    duration = models.CharField(max_length=50)
    dosage = models.CharField(max_length=256, blank=True, null=True)
    cycle = models.CharField(max_length=256)
    purpose = models.CharField(max_length=2048)
    diet_change = models.ManyToManyField(Diet, blank=True, null=True)
    environment_warnings = models.ManyToManyField(Environment, blank=True, null=True)
    activity_warnings = models.ManyToManyField(Actions, blank=True, null=True)

    def __str__(self):
        return self.prescription

    class Meta:
        ordering = ["prescription"]


class Visit(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    diagnosis = models.ManyToManyField(Diagnosis)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    treatment = models.ManyToManyField(Treatment, blank=True, null=True)

    def __str__(self):
        return "Visit | " + self.date.__str__() + ' | ' + self.patient.last_name + ", " + self.patient.first_name

    class Meta:
        ordering = ["date"]