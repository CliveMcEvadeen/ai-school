from django.db import models


class FeedbackStudent(models.Model):
    tenant = models.ForeignKey('users.Tenant', on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey('users.Student', on_delete=models.CASCADE)
    feedback = models.TextField()
    reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FeedbackStaff(models.Model):
    tenant = models.ForeignKey('users.Tenant', on_delete=models.CASCADE, null=True, blank=True)
    staff = models.ForeignKey('users.Staff', on_delete=models.CASCADE)
    feedback = models.TextField()
    reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
