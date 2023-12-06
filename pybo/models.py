from django.db import models

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # ForeignKey 속성: 다른모델과 연결, 'on_delete=models.CASCADE' 연결된 속성이 삭제되면 해당속성 함께 삭제.
    content = models.TextField()
    create_date = models.DateTimeField()