from django.db import models


class StudentResult(models.Model):
    tenant = models.ForeignKey('users.Tenant', on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey('users.Student', on_delete=models.CASCADE)
    subject = models.ForeignKey('courses.Subject', on_delete=models.CASCADE)
    test = models.FloatField(default=0)
    exam = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Exam(models.Model):
    tenant = models.ForeignKey('users.Tenant', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Quiz(models.Model):
    tenant = models.ForeignKey('users.Tenant', on_delete=models.CASCADE, null=True, blank=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    total_marks = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Assignment(models.Model):
    tenant = models.ForeignKey('users.Tenant', on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey('courses.Subject', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Gradebook(models.Model):
    tenant = models.ForeignKey('users.Tenant', on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey('users.Student', on_delete=models.CASCADE)
    subject = models.ForeignKey('courses.Subject', on_delete=models.CASCADE)
    grade = models.CharField(max_length=10)
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ReportCard(models.Model):
    tenant = models.ForeignKey('users.Tenant', on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey('users.Student', on_delete=models.CASCADE)
    session = models.ForeignKey('courses.Session', on_delete=models.CASCADE)
    grades = models.ManyToManyField(Gradebook)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ExamTimetable(models.Model):
    tenant = models.ForeignKey('users.Tenant', on_delete=models.CASCADE, null=True, blank=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    subject = models.ForeignKey('courses.Subject', on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.exam.name} - {self.subject.name} on {self.date}"


class ExamDocument(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(max_length=255)
    document = models.FileField(upload_to='exam_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ExamFeedback(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='feedbacks')
    student = models.ForeignKey('users.Student', on_delete=models.CASCADE)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.student} on {self.exam}"
