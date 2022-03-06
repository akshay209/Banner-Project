from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from . models import Banner , banner_images
from django.utils.timezone import localtime
import datetime
from myapp.forms import BannerForm
import os
from django.contrib.auth.decorators import login_required
from datetime import date

def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/ban_main')
        else:
            return render(request,'myapp/loginpage.html',context={'Data':'Invalid Credentials'})
    return render(request,'myapp/loginpage.html')

def logoff(request):
    logout(request)
    return redirect('/')

@login_required(login_url="/")
def ban_main(request):
    baner = Banner.objects.all().order_by('position')
    images = banner_images.objects.all()
    
    return render(request,'myapp/admin.html',{'baner':baner,'images':images})

def upload(request):
    if request.method == 'POST':
        position = request.POST.get('position')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        end_time = request.POST.get('end_time')
        type = request.POST.get('type')
        print("before if")
        if  type == "Normal Banner" :    
            img = request.FILES['image']
            baner = Banner(position=position,start_date=start_date,end_date=end_date,end_time=end_time,banner_type=type,image=img)
            print("n",baner)
            baner.save()
        elif type == "Sliding Banner" :
            files = request.FILES.getlist('image')
            baner = Banner.objects.create(position=position,start_date=start_date,end_date=end_date,end_time=end_time,banner_type=type)
            print("in sliding")
            for image in files:
                img = banner_images.objects.create(image=image,position=position)
                img.save()
            baner.save()
                    
        return redirect('ban_main')

@login_required(login_url="/")
def edit(request,id):
    if request.method == 'POST':
        ban = Banner.objects.get(id=id)
        f1 = BannerForm(request.POST or None,request.FILES,instance=ban)
        img = banner_images.objects.filter(position=ban.position)
        files = request.FILES.getlist('image')
        print("BEfore if",request.FILES)
        if ban.banner_type == "Normal Banner" :
            if f1.is_valid():
                img_path = ban.image.path
                if os.path.exists(img_path):
                        os.remove(img_path)
                f1.save()

        elif ban.banner_type == "Sliding Banner" :
            
            c=0
            a=0   
            if len(request.FILES) != 0: 
                print("after if",request.FILES)
                print("after if F1",f1)

                for i in img:
                    if f1.is_valid():
                        i.delete()    
                    for image in files:
                        if a == c:
                            img = banner_images.objects.create(image=image,position=ban.position)
                            print('img',img)
                            img.save()
                    a += 1
                    f1.save()
                c += 1
            else:
                for i in img:
                    if f1.is_valid():
                        i.position=ban.position
                        i.save()
                    f1.save()

        return redirect('/ban_main')
    else:
        ban = Banner.objects.get(id=id)
        if ban.banner_type == "Sliding Banner" :
            img = banner_images.objects.filter(position=ban.position)
            f1 = BannerForm(instance=ban)
            return render(request,'myapp/edit.html',{'form':f1,'img':img})
        else:
            f1 = BannerForm(instance=ban)
            return render(request,'myapp/edit.html',{'form':f1,'ban':ban})

def activate(request,id):
    ban = Banner.objects.get(id=id)
    if ban.active == False:
        ban.active = True
        ban.save() 
    return redirect("ban_main")

def deactivate(request,id):
    ban = Banner.objects.get(id=id)
    if ban.active == True:
        ban.active = False
        ban.save()  
    return redirect("ban_main")

def delete(request,id):
    ban = Banner.objects.get(id=id)
    img = banner_images.objects.filter(position = ban.position)
    if request.method == "GET":
        if ban.banner_type == "Sliding Banner" :
            img.delete()
        ban.delete()
    return redirect("ban_main")





#    date.today()


# def dele(request):
#     banner = Banner.objects.all()
#     images = banner_images.objects.all()
#     time = localtime()
#     dates = date.today()
#     if end_date=date.today():
#         ban = Banner.objects.get()
#         if ban.end_time.strftime('%H:%M') <= datetime.now().strftime('%H:%M'):
#                 ban.delete()    
# 

# rows = MyModel.objects.filter(expired=True) 
 
# for r in rows: 
#     r.delete() 


# @login_required(login_url="/")
# def ban_main(request):
#     baner = Banner.objects.all().order_by('position')
#     images = banner_images.objects.all()
#     if request.method == 'POST':
#         banend = Banner.objects.get['end_date']
#         if banend == datetime.date.today():
#             ban = Banner.objects.get()
#             if ban.end_time.strftime('%H:%M') == datetime.now().strftime('%H:%M'):
#                     ban.delete()    
#     return render(request,'myapp/admin.html',{'baner':baner,'images':images})

# rows = Banner.objects.filter(expired=True) 

# if request.method == 'POST':
#         ban = Banner.objects.get(id=id)
#         img = banner_images.objects.filter(position=ban.position)
