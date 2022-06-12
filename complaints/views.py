from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *
from .forms import ComplaintForm, ComplaintUpdateForm, ComplaintTransUpdateForm, ComplaintTransForm
from .decorators import unauthenticated_user, allowed_users, admin_only


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'complaints/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url='/login')
@admin_only
def home(request):
    complaints_cust = Complaint.objects.filter(complaint_type = "Customer Complaints")
    complaints_sect = Complaint.objects.filter(complaint_type = "Section Initiated Complaints")
    complaints_trans = Complaint_Transformer.objects.all()

    total_customer_cmp_cust = complaints_cust.count() 
    total_customer_cmp_sect = complaints_sect.count() 
    total_trans_cmp = complaints_trans.count()
    context = {'total_customer_cmp_cust':total_customer_cmp_cust, 'total_customer_cmp_sect':total_customer_cmp_sect, 'total_trans_cmp': total_trans_cmp}

    return render(request, 'complaints/homepage.html', context)

@login_required(login_url='/login')
@allowed_users(allowed_roles=['staff'])
def userPage(request):
    complaints_cust = Complaint.objects.filter(complaint_type = "Customer Complaints")
    complaints_sect = Complaint.objects.filter(complaint_type = "Section Initiated Complaints")
    complaints_trans = Complaint_Transformer.objects.all()

    total_customer_cmp_cust = complaints_cust.count() 
    total_customer_cmp_sect = complaints_sect.count() 
    total_trans_cmp = complaints_trans.count()
    username = request.user
    complaint = Complaint.objects.filter(user = username)
    complaint_transformer = Complaint_Transformer.objects.filter(user = username)
    context = {
                'total_customer_cmp_cust':total_customer_cmp_cust, 
                'total_customer_cmp_sect':total_customer_cmp_sect, 
                'total_trans_cmp': total_trans_cmp,
                'complaint': complaint,
                'complaint_transformer':complaint_transformer
                }

    return render(request, 'complaints/user.html', context)

@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin'])
def cust_complaints(request, types):
    return render(request, 'complaints/cust_complaint_form.html', {'types':types})

@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin'])
def sect_complaints(request, types):
    return render(request, 'complaints/sect_complaint_form.html', {'types':types})

@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin'])
def trans_sect_complaints(request, types):
    return render(request, 'complaints/trans_complaint_form.html', {'types':types})

@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin'])
def trans_cust_complaints(request):
    return render(request, 'complaints/trans_complaint_form.html')

@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin'])
def assign_jobs(request):
    complaints = Complaint.objects.all()
    complaints_trans = Complaint_Transformer.objects.all()

    return render(request, 'complaints/assign_jobs.html', {'complaints':complaints, 'complaints_trans':complaints_trans})

@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin'])
def rectify_jobs(request):
    complaints = Complaint.objects.all()
    complaints_trans = Complaint_Transformer.objects.all()

    return render(request, 'complaints/rectify_jobs.html', {'complaints':complaints, 'complaints_trans':complaints_trans})

@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin'])
def cancel_jobs(request):
    complaints = Complaint.objects.all()
    complaints_trans = Complaint_Transformer.objects.all()

    return render(request, 'complaints/cancel_jobs.html', {'complaints':complaints, 'complaints_trans':complaints_trans})

@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin'])
def transformer_maintenance(request, types):
    return render(request, 'complaints/trans_complaint_form.html', {'types':types})

@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin'])
def reports(request):
    return render(request, 'complaints/reports.html')

@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin'])
def create_cust_cmp(request, types):
    if types == "cust":
        form = ComplaintForm()
        if request.method == 'POST':
            #print('Printing POST:', request.POST)
            form = ComplaintForm(request.POST)
            if form.is_valid():
                form.complaint_type = "Customer Complaint"
                form.save()
                return redirect('/assign_jobs/')
    elif types == "trans":
        form = ComplaintTransForm()
        if request.method == 'POST':
            #print('Printing POST:', request.POST)
            form = ComplaintTransForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/assign_jobs/')
    else:
        form = ComplaintForm()
        if request.method == 'POST':
            #print('Printing POST:', request.POST)
            form = ComplaintForm(request.POST)
            if form.is_valid():
                form.complaint_type = "Section Initiated Complaint"
                form.save()
                return redirect('/assign_jobs/')
    context = {'form':form}
    return render(request, 'complaints/create_cust_cmp_form.html', context)

@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin','staff'])
def assign_complaint(request, pk, trans):
    if trans == "False":
        complaint = Complaint.objects.get(complaint_id=pk)
        form = ComplaintUpdateForm(instance=complaint)
        if request.method == 'POST':
            form = ComplaintUpdateForm(request.POST, instance=complaint)
            if form.is_valid():
                form.save()
                return redirect('')
    else:
        complaint = Complaint_Transformer.objects.get(complaint_id=pk)
        form = ComplaintTransUpdateForm(instance=complaint)

        if request.method == 'POST':
            form = ComplaintTransUpdateForm(request.POST, instance=complaint)
            if form.is_valid():
                form.save()
                return redirect('')

    context = {'form':form}
    return render(request, 'complaints/create_cust_cmp_form.html', context)

@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin'])
def delete_complaint(request, pk, trans='None'):
    if trans == "False":
        complaint = Complaint.objects.get(complaint_id=pk) 
        if request.method == "POST":
            complaint.delete()
            return redirect('/cancel_jobs/')
    else:
        complaint = Complaint_Transformer.objects.get(complaint_id=pk)
        if request.method == "POST":
            complaint.delete()
            return redirect('/cancel_jobs/')
    context = {'item':complaint, 'trans':trans}
    return render(request, 'complaints/delete.html', context)