from django.db import models

# Create your models here.


class Department(models.Model):
    title = models.CharField(verbose_name='Title', max_length=32)


class UserInfo(models.Model):
    name = models.CharField(verbose_name='name', max_length=48)
    password = models.CharField(verbose_name='password', max_length=64)
    age = models.IntegerField(verbose_name='age')
    account = models.DecimalField(verbose_name='credit', max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name='enroll time')

    # Foreign Key to Department id
    # on_delete specifies what should be done when a row in Department is deleted
    # there are many options: CASCADE, SET_NULL
    department_id = models.ForeignKey(to='Department', to_field='id', on_delete=models.CASCADE)
    # department_id = models.ForeignKey(to='Department', to_field='id', blank=True,
    #                                   null=True, on_delete=models.SET_NULL)

    gender_choices = (
        (1, 'male'),
        (2, 'female'),
        (3, 'trans')
    )
    gender = models.SmallIntegerField(verbose_name='gender', choices=gender_choices)


