from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('hospital-login/', views.hospital_login, name='hospital_login'),
    path('hospital-home/results.html', views.results, name='results'),
    path('logout/', views.logout_view, name='logout'),
    path('hospital-home/', views.hospital_home, name='hospital_home'),
    path('chatbot/', views.chatbot_api, name='chatbot_api'),
    path('home/', views.home_view, name='home'),
    path('result/<str:result>/', views.result_view, name='result'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('process-parameters/', views.process_parameters, name='process_parameters'),
    path('record/', views.record_voice, name='record_voice'),
    path('patient-login/', views.login_view, name='patient_login'),
    path('recording/', views.recording_view, name='recording'),
    path('chatbot_api/', views.chatbot_api, name='chatbot_api'),
    path('aboutus/', views.about_view, name='aboutus'),
    path('gethelp/', views.get_help, name='gethelp'),
    path('faq/', views.faq_view, name='faq'),
    path('doctors/', views.doctors_list_view, name='doctors_list'),
    path('patients/', views.patients_list_view, name='patients_list'),
]