from django.urls import path, include
from accounts.views import *


app_name = 'accounts'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('before_sign_up/', BeforeSignUpView.as_view(), name='before_sign_up'),
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path('sign_in/', SignInView.as_view(), name='sign_in'),
    path('sign_out/', SignOutView.as_view(), name='sign_out'),
    path('mypage/', MyPageView.as_view(), name='mypage'),
    path('mypage/TOEIC/', VocaBookView.as_view(), name='vocabook'),
    path('mypage/TOEIC/Intermediate/', DailyBookView.as_view(), name='vocabook'),
    path('voca', include('voca.urls')),

]