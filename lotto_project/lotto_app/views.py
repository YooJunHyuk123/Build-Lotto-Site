from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import LottoTicket, LottoDraw
import random

# 홈 페이지
def home(request):
    return render(request, 'lotto_app/home.html')

# 회원가입
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'lotto_app/signup.html', {'form': form})

# 로그인 (사용자/관리자 공용)
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # 관리자 계정이면 관리 페이지로 이동
            if user.is_superuser:
                return redirect('lotto_draw')
            else:
                return redirect('buy_lotto')
    else:
        form = AuthenticationForm()
    return render(request, 'lotto_app/login.html', {'form': form})

# 로그아웃
def logout_view(request):
    logout(request)
    return render(request, 'lotto_app/logout.html')

# 로또 구매 (사용자)
def buy_lotto(request):
    if request.method == 'POST':
        numbers = request.POST.get('numbers')
        auto = request.POST.get('auto')
        if auto == 'on':
            numbers = ','.join(map(str, random.sample(range(1, 46), 6)))
        LottoTicket.objects.create(user=request.user, numbers=numbers)
        return redirect('check_lotto')
    return render(request, 'lotto_app/buy.html')

# 당첨 확인 (사용자)
def check_lotto(request):
    tickets = LottoTicket.objects.filter(user=request.user)
    draws = LottoDraw.objects.all()
    return render(request, 'lotto_app/check.html', {'tickets': tickets, 'draws': draws})

# 관리자용 로또 추첨
def lotto_draw(request):
    if request.method == 'POST':
        numbers = ','.join(map(str, random.sample(range(1, 46), 6)))
        LottoDraw.objects.create(numbers=numbers)
        return redirect('admin_check')
    return render(request, 'lotto_app/lotto.html')

# 관리자용 당첨자 조회
def admin_check(request):
    draws = LottoDraw.objects.all()
    tickets = LottoTicket.objects.all()
    return render(request, 'lotto_app/admin_check.html', {'draws': draws, 'tickets': tickets})
