from django.db import models


class User(models.Model):
    class Meta:
        db_table = 'users'

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unknown')
    ]
    GRADE_CHOICES = [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JU', 'Junior'),
        ('SE', 'Senior'),
        ('MA', 'Master'),
        ('DO', 'Doctor'),
        ('UN', 'Unknown')
    ]
    CAMPUS_CHOICES = [
        ('SH', 'ShaHe'),
        ('XTC', 'XiTuCheng'),
        ('UN', 'Unknown')
    ]
    SCHOOL_CHOICES = [
        ('IC', 'Information and Communication'),
        ('EE', 'Electronic Engineer'),
        ('CS', 'Computer Science'),
        ('NS', 'Network Security'),
        ('AI', 'Artificial Intelligence'),
        ('SF', 'Software'),
        ('AU', 'Automation'),
        ('EM', 'Economics and Management'),
        ('SC', 'Science'),
        ('HU', 'Humanities'),
        ('DM', 'Digital Media'),
        ('MA', 'Marxism'),
        ('IN', 'International'),
        ('UN', 'Unknown')
    ]

    stu_id = models.AutoField(primary_key=True)
    user_name = models.TextField(max_length=15)
    password = models.TextField(max_length=50)  # to-do: store passwords properly
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='U'
    )
    grade = models.CharField(
        max_length=2,
        choices=GRADE_CHOICES,
        default='UN'
    )
    campus = models.CharField(
        max_length=3,
        choices=CAMPUS_CHOICES,
        default='UN'
    )
    school = models.CharField(
        max_length=2,
        choices=SCHOOL_CHOICES,
        default='UN'
    )
    phone_num = models.BigIntegerField()
    wechat = models.TextField()
    qq = models.TextField()
    mail = models.TextField()
    avatar_add = models.TextField()
    motto = models.TextField(max_length=50)


