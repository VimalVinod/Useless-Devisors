from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    index,
    login_view,
    signup_view,
    citizenship_exam,
    tier_1_exam,
    tier_2_exam,
    tier_3_exam,
    welcome,
    submit_tier_1_exam,
    submit_tier_2_exam,
    submit_tier_3_exam,
    create_pet_profile,
)

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('citizenship_exam/', citizenship_exam, name='citizenship_exam'),
    path('tier_1_exam/', tier_1_exam, name='tier_1_exam'),
    path('tier_1_exam/submit/', submit_tier_1_exam, name='submit_tier_1_exam'),
    path('tier_2_exam/', tier_2_exam, name='tier_2_exam'),
    path('tier_2_exam/submit/', submit_tier_2_exam, name='submit_tier_2_exam'),
    path('tier_3_exam/', tier_3_exam, name='tier_3_exam'),
    path('tier_3_exam/submit/', submit_tier_3_exam, name='submit_tier_3_exam'),
    path('create_pet_profile/', create_pet_profile, name='create_pet_profile'),  # Fixed the view name
    path('welcome/', welcome, name='welcome'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files
