from django.db import models


class LeaveReportStudent(models.Model):
    tenant = models.ForeignKey('users.Tenant', on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey('users.Student', on_delete=models.CASCADE)
    date = models.CharField(max_length=60)
    message = models.TextField()
    status = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class LeaveReportStaff(models.Model):
    tenant = models.ForeignKey('users.Tenant', on_delete=models.CASCADE, null=True, blank=True)
    staff = models.ForeignKey('users.Staff', on_delete=models.CASCADE)
    date = models.CharField(max_length=60)
    message = models.TextField()
    status = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
