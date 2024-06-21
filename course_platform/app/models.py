from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import send_custom_email
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="1 martalik kurs narxi")

    def __str__(self):
        return f"{self.title}, narxi: {self.price}"


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='teachers/')
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.full_name


class Student(models.Model):
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class Group(models.Model):
    number = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return f"{self.number}-guruh, {self.course}"


class Lesson(models.Model):
    number = models.IntegerField()
    topic = models.CharField(max_length=200)
    video = models.FileField(upload_to='videos/')
    task = models.ImageField(upload_to='images/')
    comment = models.TextField(null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.number}-dars, {self.topic} mavzu, {self.group}-guruh"

    def like_count(self):
        return self.likes.count()

    def dislike_count(self):
        return self.dislikes.count()


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1
    VALUE_CHOICES = (
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, related_name='likes_dislikes', on_delete=models.CASCADE)
    value = models.SmallIntegerField(choices=VALUE_CHOICES)

    class Meta:
        unique_together = ('user', 'lesson')

    def __str__(self):
        return f"{self.user.username} rated {self.lesson.topic} as {self.value}"


class Comment(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text}"


class Update(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}: {self.created_at}'


@receiver(post_save, sender=Update)
def send_update_notification(sender, instance, created, **kwargs):
    if created:
        users = User.objects.all()
        subject = f"New Update: {instance.title}"
        message = instance.content
        for user in users:
            send_custom_email(user.email, subject, message)