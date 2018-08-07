from django.urls import path

from tuites.views import PostTuiteView, LikeTuiteView

app_name = "tuites"

urlpatterns = [
    path('postar/', PostTuiteView.as_view(), name='post'),
    path('like/<int:pk>', LikeTuiteView.as_view(), name='like'),
]