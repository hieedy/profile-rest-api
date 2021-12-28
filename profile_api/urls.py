from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profile_api import views

#registering ViewSet views with urls is bit different from other approaches.
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name = "hello-viewset") #no need to add "/" after the url
# register("url", view, base_name)
#it will automaticall generate the list of all the url(s) that are associated with our viewset

router.register('profiles', views.UserProfileViewSet) # preffer not to user base_name coz it will automatically get
# base_name from the query_set

urlpatterns = [

    #Because Django’s URL resolver expects to send the request and associated arguments to a callable function, not a class, class-#based views have an as_view() class method which returns a function that can be called when a request arrives for a URL #matching the associated pattern. The function creates an instance of the class, calls setup() to initialize its attributes, and #then calls its dispatch() method. dispatch looks at the request to determine whether it is a GET, POST, etc, and relays the #request to a matching method if one is defined, or raises HttpResponseNotAllowed if not
    path('hello-view', views.HelloApiView.as_view()), #as_view provide entry to class based view that we have created
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),


]
