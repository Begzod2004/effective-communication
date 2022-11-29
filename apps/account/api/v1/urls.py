from django.urls import path, include
from apps.account.api.v1.views import AccountView, AccountRegisterView, LoginView, SetNewPasswordView, \
    SetPasswordConfirmAPIView, ResetPasswordAPIView, AccountListView, AccountRetrieveUpdateView, \
    AccountOwnImageUpdateView, EmailVerificationAPIView, ChangePasswordCompletedView

urlpatterns = [
    path('register/', AccountRegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('verify-email/', EmailVerificationAPIView.as_view()),
    path('reset-password/', ResetPasswordAPIView.as_view()),
    path('set-password-confirm/<str:uidb64>/<str:token>/', SetPasswordConfirmAPIView.as_view()),
    path('set-password-completed/', SetNewPasswordView.as_view()),
    path('own/<int:pk>/', AccountView.as_view()),
    path('profile/<int:pk>/', AccountRetrieveUpdateView.as_view()),
    path('profiles/', AccountListView.as_view()),

    # change-password
    path('change-password/<int:pk>/', ChangePasswordCompletedView.as_view())
]
