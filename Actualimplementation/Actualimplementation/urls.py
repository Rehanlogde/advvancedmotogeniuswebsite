from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('homepage', views.homepage),
    path("login", views.loginuser),
    path('registration', views.registration),
    path('virtualassistant', views.virtualassistance),
    path('registrationacknowledgement', views.registrationresult),
    path('dashboard', views.userdashboard),
    path('showroom', views.showroom),
    path('learnmoresustainability', views.sustainabilitypage),
    path('dbtesting', views.test_db_connection),
    path('book/', views.booking),
    path('bookingresult', views.bookingsuccess),
    path('logout', views.loggingout),
    path('cardetailspage/', views.cardetaildynamicone),
    path('spfinder', views.sparepartsfinder),
    path("spfinderorderpage/", views.spfinderordering),
    path("ordersuccess/", views.ordersuccess),
    path("recot", views.chatbot),
    path("botresp/", views.chatbotresponse),
    path("customization/", views.customization),
    path("logout", views.logoutuser)
]
