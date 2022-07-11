from django.urls import path
from .views import user_reg, UserProfileView, update_user_profile, LoginUserView
from django.contrib.auth.views import LogoutView, PasswordChangeView,\
    PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView,\
    PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('reg/', user_reg, name='reg'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('profile/<int:pk>', UserProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(template_name='accoutUser/logout.html', next_page=None), name='logout'),
    path('update/', update_user_profile, name='update-profile'),
    path('password_change/', PasswordChangeView.as_view(
        template_name='accoutUser/password_change.html'), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(
        template_name='accoutUser/password_changed.html'), name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(
        template_name='accoutUser/password_change.html',
        subject_template_name='accoutUser/reset_subject.txt',
        email_template_name='accoutUser/reset_email.txt/',
    ), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='accoutUser/password_changed.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='accoutUser/password_change.html',
        post_reset_login=True,
    ), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='accoutUser/password_changed.html',
    ), name='password_reset_complete')
]
