from django.db import models
from django.contrib.auth.models import User
import random

# 사용자 구매 로또 티켓
class LottoTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    numbers = models.CharField(max_length=50)  # 1,2,3,4,5,6
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.numbers}"

# 로또 추첨 결과
class LottoDraw(models.Model):
    numbers = models.CharField(max_length=50)  # 1,2,3,4,5,6
    draw_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.numbers
