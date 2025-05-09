from django.db import models


class NotificationStaff(models.Model):
    tenant = models.ForeignKey('users.Tenant', on_delete=models.CASCADE, null=True, blank=True)
    staff = models.ForeignKey('users.Staff', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class NotificationStudent(models.Model):
    tenant = models.ForeignKey('users.Tenant', on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey('users.Student', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

