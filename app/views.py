from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        email=request.POST.get('email')
        number=request.POST.get('number')

        school=request.POST.get('school')
        sy=request.POST.get('sy')
        ss=request.POST.get('sp')
        college=request.POST.get('college')
        cy=request.POST.get('cy')
        cs=request.POST.get('cs')

        grad=request.POST.get('grad')
        gy=request.POST.get('gy')
        gs=request.POST.get('gs')

        postgrad=request.POST.get('pgrad')
        pgy=request.POST.get('pgy')
        pgs=request.POST.get('pgs')
        '''grad and pgarad here'''

        e1=request.POST.get('e1')
        p1=request.POST.get('p1')
        e2=request.POST.get('e2')
        p2=request.POST.get('p2')
        projt1=request.POST.get('projt1')
        proja1=request.POST.get('proja1')
        projt2=request.POST.get('projt2')
        proja2=request.POST.get('proja2')

        skills=request.POST.get('skills')


        cust1=request.POST.get('cust1')
        cusc1=request.POST.get('cusc1')
        cust2=request.POST.get('cust2')
        cusc1=request.POST.get('cusc2')

        #print(name,email,number,address,school,sy,ss,grad,gs,gy,e1,p1,projt1,proja1,skills,cust1,cusc1)


        
    return render(request,'home.html')

