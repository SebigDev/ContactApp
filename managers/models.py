from django.db import models
from django.urls import reverse


class Manager(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list',)


class StaffManager(models.Model):
    company = models.CharField(max_length=200)
    current_level = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=200)
    is_staff = models.BooleanField(default=True)
    manager_name = models.ForeignKey(Manager, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Staff Manager'

    def __str__(self):
        return self.manager_name.name

    def get_absolute_url(self):
        return reverse('staff_list', )


class ActiveManager(models.Model):
    company = models.CharField(max_length=200)
    current_level = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    manager_name = models.ForeignKey(Manager, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Active Manager'

    def __str__(self):
        return self.manager_name.name

    def get_absolute_url(self):
        return reverse('student_list', )

