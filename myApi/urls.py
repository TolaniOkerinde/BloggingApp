from django.urls import path,include

from rest_framework.routers import DefaultRouter

from myApi import views

router = DefaultRouter()

router.register ('profile', views.UserProfileViewSet)
# NO NEED FOR base name because we are usinga query set and dont have to define manually
#   all the list, create etc functions
router.register ('feed', views.ProfileFeedViewset)
urlpatterns= [

    path('login/' , views.UserLoginApiView.as_view()),
    # this is an api view and not a view set 

    path ('', include(router.urls))

]