from account.models import Account
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from iam.decorators import unauthenticated_user, allowed_users, admin_only
from incident_management.models import *
from account.models import *
from administrator.models import *

# ---------------------------------------------------------------------------- #
#                                 USERS SECTION                                #
# ---------------------------------------------------------------------------- #

# ------------------------------ MAIN USER VIEW ------------------------------ #


@login_required(login_url='login')
@allowed_users(allowed_role=['Admin', 'Technician'])
def users(request):

    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        full_name = request.POST['full_name']
        role = request.POST['role']
        company = Company.objects.get(name=request.POST['company'])

        if request.POST.get('PIC') == None:
            PIC_val = False
        else:
            PIC_val = request.POST['PIC']

        PIC = PIC_val

        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if Account.objects.filter(email=email).exists():
                messages.info(request, 'Email is taken')
                return redirect('users')
            else:
                user = Account.objects.create_user(password=password1, first_name=first_name, last_name=last_name,
                                                   email=email, role=role, full_name=full_name, company_link=company, is_pic=PIC)
                user.save()
                return redirect('users')
        else:
            messages.info(request, 'Password not matching')
            return redirect('users')
    else:
        obj = Account.objects.all()
        company_objs = Company.objects.all()
        context = {
            'user_list': obj,
            'company_name': company_objs,
        }

        return render(request, 'users.html', context)

# -------------------------------- UPDATE USER ------------------------------- #


@allowed_users(allowed_role=['Admin'])
def update_user(request, pk):
    first_name_val = request.POST['first_name']
    last_name_val = request.POST['last_name']
    full_name_val = request.POST['full_name']
    role_val = request.POST['role']
    group_val = request.POST['group']

    if request.POST.get('PIC') == None:
        PIC_val = False
    else:
        PIC_val = request.POST['PIC']

    # Save changes of update field based on user_id
    update_account = Account.objects.get(id=pk)

    # update_technician = Technician.objects.get(email__email=update_account.email)
    update_account.first_name = first_name_val
    update_account.last_name = last_name_val
    update_account.full_name = full_name_val
    update_account.role = role_val
    update_account.group = group_val
    update_account.is_pic = PIC_val
    # update_technician.group.name = group_val

    update_account.save()
    # update_technician.save()

    return redirect('users')

# ------------------------ USER AND GROUP UPDATE MODAL ----------------------- #


@allowed_users(allowed_role=['Admin'])
def update_modal(request, pk):
    update = get_object_or_404(Account, pk=pk)
    support_group_objs = Group.objects.all()
    group_obj = Group.objects.all()
    return render(request, 'users_update_modal.html', {'user': update, 'support_group': support_group_objs, 'group_list': group_obj})

# -------------------------------- DELETE USER ------------------------------- #


@allowed_users(allowed_role=['Admin'])
def delete_user(request, pk):
    user = Account.objects.get(id=pk)

    if request.method == 'POST':
        user.delete()
        return redirect('users')

    context = {
        'object': user,
    }
    return render(request, 'users', context)

# ------------------------ USER AND GROUP DELETE MODAL ----------------------- #


@allowed_users(allowed_role=['Admin'])
def delete_user_modal(request, pk):

    user = Account.objects.get(id=pk)
    context = {
        'user': user,
    }
    return render(request, 'users_delete_modal.html', context)


@allowed_users(allowed_role=['Admin'])
def delete_technician_modal(request, pk):

    user = Account.objects.get(id=pk)
    technician = Technician.objects.get(email__email=user.email)
    context = {
        'user': user,
        'technician': technician,
    }

    return render(request, 'technicians_delete_modal.html', context)


@allowed_users(allowed_role=['Admin'])
def delete_technician(request, pk):

    technician = Technician.objects.get(id=pk)
    technician_account = Account.objects.get(email=technician.email.email)
    if request.method == 'POST':
        technician.delete()
        technician_account.group = 'Not Set'
        technician_account.save()

        return redirect('groups')

    return render(request, 'groups')


# ---------------------------------------------------------------------------- #
#                                GROUPS SECTION                                #
# ---------------------------------------------------------------------------- #


@allowed_users(allowed_role=['Admin'])
@login_required(login_url='login')
def groups(request):

    if request.method == 'POST':
        group_name = Group.objects.get(name=request.POST["group_name"])
        members_list = request.POST.getlist("member")

        for member in members_list:
            member_specific = Account.objects.get(email=member)
            member_specific.group = str(group_name)
            group_member_set = Technician.objects.create(
                group=group_name, email=member_specific)
            group_member_set.save()
            member_specific.save()

        return redirect('groups')

    else:
        technician_obj = Technician.objects.all()
        group_obj = Group.objects.all()
        user_obj = Account.objects.filter(role='Technician')
        company_obj = Company.objects.all()
        context = {
            'technician_list': technician_obj,
            'group_list': group_obj,
            'user_list': user_obj,
            'company_list': company_obj,
        }

        return render(request, 'groups.html', context)

# ------------------------------- CREATE GROUP ------------------------------- #


def create_group(request):
    if request.method == 'POST':

        group_name = request.POST['group_name']

        if request.POST.get('group_round_robin') == None:
            group_round_robin = False
        else:
            group_round_robin = request.POST['group_round_robin']

        # saving the input to the models
        group_set = Group.objects.create(
            name=group_name, round_robin=group_round_robin)
        group_set.save()
        return redirect('groups')

    else:
        return render(request, 'groups.html')


@allowed_users(allowed_role=['Admin'])
def group_create_modal(request):
    return render(request, 'groups_create_modal.html')

# ---------------------------------------------------------------------------- #
#                               COMPANIES SECTION                              #
# ---------------------------------------------------------------------------- #

# --------------------------- MAIN COMPANIES VIEWS --------------------------- #


@allowed_users(allowed_role=['Admin'])
@login_required(login_url='login')
def companies(request):
    if request.method == 'POST':

        if request.POST.get('round_robin') == None:
            round_robin_val = False
        else:
            round_robin_val = request.POST['round_robin']

        x = request.POST.get('email')
        domain_val = x.split('@')[1]

        companySet = Company(
            company_id=request.POST['ID'],
            name=request.POST['name'],
            email=request.POST['email'],
            domain=domain_val,
            contact_number=request.POST['contact_number'],
            PIC=request.POST['PIC'],
            round_robin=round_robin_val
        )

        companySet.save()
        return redirect('companies')
    else:
        account_obj = Account.objects.filter(is_pic=True)
        company_obj = Company.objects.all()
        context = {
            'companies': company_obj,
            'accounts': account_obj,
        }

        return render(request, 'companies.html', context)


@allowed_users(allowed_role=['Admin'])
def update_company_modal(request, pk):
    company = Company.objects.get(company_id=pk)
    account_obj = Account.objects.filter(is_pic=True)

    return render(request, 'companies_update_modal.html', {'company': company, 'accounts': account_obj})

# ------------------------------ UPDATE COMPANY ------------------------------ #


@allowed_users(allowed_role=['Admin'])
def update_company(request, pk):
    id_val = request.POST['ID']
    name_val = request.POST['name']
    email_val = request.POST['email']
    PIC_val = request.POST['PIC']

    contact_number_val = request.POST['contact_number']

    if request.POST.get('round_robin') == None:
        round_robin_val = False
    else:
        round_robin_val = request.POST['round_robin']

    x = request.POST.get('email')
    domain_val = x.split('@')[1]

    # Save changes of update field based on user_id
    update_account = Company.objects.get(company_id=pk)
    update_account.company_id = id_val
    update_account.name = name_val
    update_account.email = email_val
    update_account.domain = domain_val
    update_account.PIC = PIC_val
    update_account.contact_number = contact_number_val
    update_account.round_robin = round_robin_val
    update_account.save()

    # Disable all support groups' RR state and their corresponding RR-select state as well
    if round_robin_val == False:
        company_groups = Group.objects.filter(
            company_link__name=request.user.company_link.name)
        technician_groups = Technician.objects.filter(
            email__company_link__name=request.user.company_link.name)

        for group in company_groups:
            group.round_robin = False
            group.save()

        for tech in technician_groups:
            tech.round_robin_selected = False
            tech.save()

    return redirect('companies')

# ------------------------------ DELETE COMPANY ------------------------------ #


@allowed_users(allowed_role=['Admin'])
def delete_company(request, pk):
    company = Company.objects.get(company_id=pk)

    if request.method == 'POST':
        company.delete()
        return redirect('companies')

    context = {
        'companies': company,
    }
    return render(request, 'companies', context)

# --------------------------- DELETE COMPANY MODAL --------------------------- #


@allowed_users(allowed_role=['Admin'])
def delete_company_modal(request, pk):
    company = Company.objects.get(company_id=pk)
    return render(request, 'companies_delete_modal.html', {'company': company})
