from django.shortcuts import render
from info.models import User ,UserDoc
from info.forms import SignupForm ,LoginForm, InfoUpdateForm, UserDocsForm
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth import login,authenticate , logout
from django.views.generic import CreateView
import os
from django.conf import settings
import base64
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

# class UserBaseView(TemplateView):
#     template_name = 'info/abc.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['user_id'] = self.request.user.id
#         return context

# class MyChildView(UserBaseView):
#     template_name = 'info/abc.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'My Page'
#         context['content'] = 'This is some content'
#         return context




class UserBaseView(TemplateView):
    model = User
    template_name = 'info/dashboard.html'

    def get_context_data(self,**kwargs):
        request = self.request
        user = User.objects.all()
        user_id = request.user.id
        f_path = os.path.join(settings.MEDIA_ROOT,"profile_pic",str(user_id))
        if os.path.exists(f_path):
              
              image_path = os.listdir(f_path)[0]
              image = f"/media/profile_pic/{user_id}/{image_path}"
        else:
             
             image = None
        context = super(UserBaseView, self).get_context_data(**kwargs)
        context['image'] = image
        context['user'] = user
        return context


class SignupView(CreateView):
    model = User
    form = SignupForm
    def get(self,request):         
            form = SignupForm()
            return render(request,'info/signup.html',{'form':form})
    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():  
              password1 = form.cleaned_data.get("password")
              password2 = form.cleaned_data.get("password2")
              user = form.save(commit=False)
              user.set_password(form.cleaned_data.get("password"))
              user.save()
              return redirect('login')
        return render(request,'info/signup.html',{'form': form})
        


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request,'info/login.html',{"form":form})
        
    def post(self,request):
        form = LoginForm(request.POST ,)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            print(username,password)
            user=authenticate(username=username,password=password)
            # print(user)
            if user is not None:
                print(5555555555)
                login(request, user)
                return redirect('dashboard')
        return render(request,'info/login.html',{'form':form})
        

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class Dashboard(UserBaseView,View):
     template_name = 'info/dashboard.html'
     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'My Page'
        context['content'] = 'This is some content'
        return context   

           
            
@method_decorator(login_required(login_url='/login/'), name='dispatch')        
class UserTableView(View):
    def get(self,request):
        user = User.objects.all()   
        return render(request,'info/table.html',{'user':user})    
       




#    profile image for header
class Header_Img(UserBaseView):
     template_name = 'info/header.html'
     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context





# add user through dashboard
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SignupViewForDashboard(CreateView):
    model = User
    form = SignupForm
    def get(self,request):          
            form = SignupForm()
            return render(request,'info/signup.html',{'form':form})
    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():   
             user = form.save(commit=False)
             user.set_password(form.cleaned_data.get("password"))
             user.save()
             return redirect('capturingimg')
        return render(request,'info/signup.html',{'form': form})



# image capture view
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class Capture_image_View(View):
    def get(self,request):
        return render(request,'info/image_capture.html')
    
    def post(self,request):
        try:
            totalimage = self.request.POST.get("totalimage")
            current_user = request.user
            current_user_id = current_user.id
            current_user_id = str(current_user.id) 
            # print(computer_id)
            folder_path = os.path.join(settings.MEDIA_ROOT,"profile_pic", current_user_id)
            os.makedirs(folder_path)
            # print(totalimage)
            for image_sn in range(0, int(totalimage)):
                
                image =  self.request.POST.get(str(image_sn))
                image_parts = image.split(";base64,")
                image_type_aux = image_parts[0].split("image/")
                image_type = image_type_aux[1]
                image_base64 = image_parts[1]
                image_data = base64.b64decode(image_base64)
                file_name = f'media/profile_pic/{current_user_id}/{image_sn}.{image_type}'
                with open(file_name, 'wb') as f:
                    f.write(image_data)

            return redirect('dashboard')
        except Exception as e:
            print(e, 9090)
            return render(request,"info/image_capture.html")
    





# view to save the images in their respective folders after clicking add button in dashboard page
class UserProfileView(View):
  pass



# to delete the user
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class UserDelete(View):
    def get(self, request, id):
        Userdelete = User.objects.get(id=id)
        Userdelete.delete()
        return redirect('dashboard') 





class UserDetailView(View):
    def get(self,request):  
            id = request.POST.get("id")
            print(id)
            return render(request,'info/dashboard.html')




# logout view
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class LogoutView(View):
 def get(self,request):
        logout(request)
        return redirect('login')





# to edit the user information
class User_Info_Update_View(View):
    def get(self, request,id):
        update = User.objects.get(id=id)
        infoupdate=InfoUpdateForm(instance=update)  
        return render(request,'info/user_info_update.html',{'form':infoupdate})

    def post(self,request,id):
        update = User.objects.get(id=id)
        infoupdate = InfoUpdateForm(request.POST,instance=update)
        if infoupdate.is_valid():
            infoupdate.save()
            return redirect('usertable')
        return render(request,'info/user_info_update.html',{'form':infoupdate})



# image update through user information table
class Image_update(View):
    def get(self,request,id):
         user = User.objects.get(id=id)
         f_path = os.path.join(settings.MEDIA_ROOT,"profile_pic",str(user.id))
         if os.path.exists(f_path):  
              image_path = os.listdir(f_path)
              image_list=list()
              for image in image_path:
                    print(image)
                    image_list.append(image)
              print(image_list)
              return render(request,'info/image_update_through_table.html',{'image':image_list,'user':user})
         return render(request,'info/image_update_through_table.html')



    def post(self,request,id):     
        try:
            totalimage = self.request.POST.get("totalimage")
            current_user =User.objects.get(id=id)
            current_user_id = current_user.id
            current_user_id = str(current_user.id) 
            folder_path = os.path.join(settings.MEDIA_ROOT,"profile_pic", current_user_id)
            if not os.path.isdir(folder_path):
                os.makedirs(folder_path)
                for image_sn in range(0, int(totalimage)):
                    image =  self.request.POST.get(str(image_sn))
                    image_parts = image.split(";base64,")
                    image_type_aux = image_parts[0].split("image/")
                    image_type = image_type_aux[1]
                    image_base64 = image_parts[1]
                    image_data = base64.b64decode(image_base64)
                    file_name = f'media/profile_pic/{current_user_id}/{image_sn}.{image_type}'
                    with open(file_name, 'wb') as f:
                        f.write(image_data)
                return redirect('dashboard')
            else:
                f_path = os.path.join(settings.MEDIA_ROOT,"profile_pic",str(current_user_id))
                image_path = os.listdir(f_path)
                count=0
                for image in image_path:
                    count=count+1
                count=count+1
                for image_sn in range(0, int(totalimage)):
                    count = count
                    image =  self.request.POST.get(str(image_sn))
                    image_parts = image.split(";base64,")
                    image_type_aux = image_parts[0].split("image/")
                    image_type = image_type_aux[1]
                    image_base64 = image_parts[1]
                    image_data = base64.b64decode(image_base64)
                    file_name = f'media/profile_pic/{current_user_id}/{count}.{image_type}'
                    with open(file_name, 'wb') as f:
                        f.write(image_data)
                    count = count+1
                return redirect('dashboard')
        except Exception as e:
            print(e, 9090)
            return render(request,"info/image_update_through_table.html")
        
              
            



# user docs view

class UserDocsView(View):
    def get(self,request):
        user = User.objects.all()
        return render(request,'info/user_docs.html',{'user':user})
    

# user docs upload
class UserDocsUploadView(View):

    def get(self,request,id):
        uername = User.objects.all()
        userdocs = UserDoc.objects.filter(user=id)
        print(userdocs.values())
        return render(request,'info/user_docs_list.html',{'userdocs':userdocs,'id':id})





# add user docs
class UserDocsFormView(CreateView):
    model = UserDoc
    form = UserDocsForm
    def get(self,request,*args, **kwarg):          
            form = UserDocsForm()
            print('aparna')
            return render(request,'info/add_user_doc.html',{'form':form})
    def post(self, request,id):
        form = UserDocsForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
             
             img_url = form.cleaned_data['docs_image_url']
             bbox = form.cleaned_data['bbox'] 
             doc_type = form.cleaned_data['doc_type']
             print(img_url,bbox,doc_type)
             user_name = User.objects.get(id=id)
             print(user_name)
             save_data = UserDoc(user=user_name,bbox=bbox,docs_image_url=img_url,doc_type=doc_type)
             save_data.save()
             return render(request,'info/user_docs_list.html')   
            
        return render(request,'info/add_user_doc.html',{'form': form})
    # model = UserDoc
    # def get(self,request, *args, **kwarg):
    #         try:
    #             form = UserDocsForm()
    #             print("893u782374")
    #             return render(request,'info/2.html',{'form':form})
    #         except Exception as e:
                 
                 
    #              print("Exception: ",e)
    #              raise e
    # def post(self, request,id):
    #         try:
    #             print(6666666666)
    #             img_url=request.FILES.get('docs_image_url')
    #             print(img_url)
    #             form = UserDocsForm(request.POST)
    #             print(form)
    #             try:
    #                 if form.is_valid():
                               
    #                         img_url = form.cleaned_data['docs_image_url']
    #                         bbox = form.cleaned_data['bbox'] 
    #                         doc_type = form.cleaned_data['doc_type']
    #                         print(img_url,bbox,doc_type)
    #                         user_name = User.objects.get(id=id)
    #                         print(user_name)
    #                         save_data = UserDoc(user=user_name,bbox=bbox,docs_image_url=img_url,doc_type=doc_type)
    #                         save_data.save()
    #                         return render(request,'info/user_docs_list.html')
    #                 else:
    #                      print(form.errors, "wuieyiryiwuer")
    #                 return render(request,'info/2.html')
    #             except Exception as e:
    #                 print(11211111,e)
    #                 raise e
    #         except Exception as e:
    #                 print(11111111,e)


       



        #       user = form.save(commit=False)
        #       user.save()
        #       return redirect('userdocs')
        








# def get(self,request):
#             user_id = request.user.id
#             print(user_id)
#             f_path = os.path.join(settings.MEDIA_ROOT,"profile_pic",str(user_id))
#             print(f_path)
#             if os.path.exists(f_path):
#                     return render(request,'info/header.html',{"user":user,"f_path":f_path})
#             return render(request,'info/header.html',{'user':user})
            