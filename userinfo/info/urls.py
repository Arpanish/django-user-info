from django.urls import path
from info.views import SignupView , LoginView, Dashboard, Capture_image_View, SignupViewForDashboard, UserProfileView, UserDelete, UserDetailView,Header_Img, UserTableView,LogoutView, User_Info_Update_View, Image_update,UserDocsView,UserDocsUploadView,UserDocsFormView
urlpatterns = [
    path('signup/',SignupView.as_view(),name="signup"),
    path('dashboard/',Dashboard.as_view(),name="dashboard"),
    path('login/',LoginView.as_view(),name="login"),
    path('image_capture/',Capture_image_View.as_view(),name="capturingimg"),
    path('signupdashboard/',SignupViewForDashboard.as_view(),name="signupdashboard"),
    path('userprofileview/',UserProfileView.as_view(),name="userprofile"),
    path('userdelete/<int:id>', UserDelete.as_view(), name="userdelete"),   
    path('userdetail/', UserDetailView.as_view(), name="userdetail"),   
    path('userimage/', Header_Img.as_view(), name="userimage"),   
    path('usertable/', UserTableView.as_view(), name="usertable"),   
    path('userlogout/', LogoutView.as_view(), name="userlogout"),   
    path('user_info_update/<int:id>/', User_Info_Update_View.as_view(), name="user_info_edit"),   
    path('imageupdate/<int:id>/', Image_update.as_view(), name="imageupdate"),   
    path('userdocs/', UserDocsView.as_view(), name="userdocs"),   
    path('userdocsupload/<int:id>/', UserDocsUploadView.as_view(), name="userdocs_upload"),   
    path('userdocsform/<int:id>/',UserDocsFormView.as_view(), name="userdocs_form"),   
]
