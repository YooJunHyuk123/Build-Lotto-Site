from django.db import models
from django.contrib.auth.models import User
import random

# 사용자가 구매한 로또 번호
class LottoTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    numbers = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.numbers}"

# 관리자가 추첨한 로또 번호
class LottoDraw(models.Model):
    numbers = models.CharField(max_length=50)
    draw_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.numbers