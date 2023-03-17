from django.shortcuts import render,redirect
from django.contrib import messages
from . import resume
from django.http import HttpResponse, Http404
import os

# Create your views here.
def home(request):
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        email=request.POST.get('email')
        number=request.POST.get('number')

        obj=request.POST.get('obj')

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
        gradc=request.POST.get('gradc')
        pgradc=request.POST.get('pgradc')

        e1=request.POST.get('e1')
        p1=request.POST.get('p1')
        e2=request.POST.get('e2')
        p2=request.POST.get('p2')
        y1=request.POST.get('y1')
        y2=request.POST.get('y2')
        projt1=request.POST.get('projt1')
        proja1=request.POST.get('proja1')
        projt2=request.POST.get('projt2')
        proja2=request.POST.get('proja2')
        projg1=request.POST.get('projg1')
        projg2=request.POST.get('projg2')

        skills=request.POST.get('skills')

        cust1=request.POST.get('cust1')
        cusc1=request.POST.get('cusc1')
        ad=[['HSC',cs,cy,college],['SSC',ss,sy,school]] #d-s-y-c
        if grad !='Select Graduation Course(if applies)':
            ad.append([grad,gs,gy,gradc])
        if postgrad != 'Select PostGraduation Course(if applies)':
            ad.append([postgrad,pgs,pgy,pgradc])
        xp=[]
        al=[]
        if projt1:
           al.append([projt1,proja1,projg1])
        if projt2:
           al.append([projt2,proja2,projg2])
        if e1:
            xp.append([e1+":"+p1,y1])
        if e2:
            xp.append([e2+":"+p2,y2])
        #print(name,address,email,number,obj,ad,xp,skills,al,cust1,cusc1)
        resume.generate_resume(name,address,email,number,obj,ad,xp,skills,al,cust1,cusc1)

        
    return render(request,'home.html')

def download(request):
    file = open('H:\\hof\\subm\\resume.docx', 'rb')
    response = HttpResponse(file, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename="resume.docx"'
    return response

