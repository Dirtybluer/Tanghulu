# Generated by Django 3.0.3 on 2020-05-24 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('stu_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('user_name', models.TextField(max_length=15)),
                ('password', models.TextField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unknown')], default='U', max_length=1)),
                ('grade', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JU', 'Junior'), ('SE', 'Senior'), ('MA', 'Master'), ('DO', 'Doctor'), ('UN', 'Unknown')], default='UN', max_length=2)),
                ('campus', models.CharField(choices=[('SH', 'ShaHe'), ('XTC', 'XiTuCheng'), ('UN', 'Unknown')], default='UN', max_length=3)),
                ('school', models.CharField(choices=[('IC', 'Information and Communication'), ('EE', 'Electronic Engineer'), ('CS', 'Computer Science'), ('NS', 'Network Security'), ('AI', 'Artificial Intelligence'), ('SF', 'Software'), ('AU', 'Automation'), ('EM', 'Economics and Management'), ('SC', 'Science'), ('HU', 'Humanities'), ('DM', 'Digital Media'), ('MA', 'Marxism'), ('IN', 'International'), ('UN', 'Unknown')], default='UN', max_length=2)),
                ('phone_num', models.BigIntegerField()),
                ('wechat', models.TextField()),
                ('qq', models.TextField()),
                ('mail', models.TextField()),
                ('avatar_add', models.TextField()),
                ('motto', models.TextField(max_length=50)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]