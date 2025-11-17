from django.contrib import admin
from .models import LottoTicket, LottoDraw

# 관리자 페이지에 모델 등록
admin.site.register(LottoTicket)
admin.site.register(LottoDraw)
