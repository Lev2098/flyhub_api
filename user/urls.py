from django.urls import path
from user.views import CreateUserView, ManageUserView

app_name = "user"

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("account/", ManageUserView.as_view(), name="manage"),
]