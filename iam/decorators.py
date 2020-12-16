
from django.http import HttpResponse
from django.shortcuts import redirect

from account.models import Account


def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated and request.user.role == 'Customer':
			return redirect('landing_page')
		elif request.user.is_authenticated and (request.user.role == 'Admin' or request.user.role == 'Technician'):
			return redirect('dashboard')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

# for now this method only allow one group at a time
def allowed_users(allowed_role):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):
			if not request.user.is_authenticated:
				return redirect('unavailable_page')
			else:
				flag = False
				
				for i in range(len(allowed_role)):
					if request.user.role == allowed_role[i]:
						flag = True

				if (flag):
					return view_func(request, *args, **kwargs)
				else:
					return redirect('unavailable_page')
				# return HttpResponse('You are not authorized')

		return wrapper_func
	return decorator


def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):

		role = Account.role

		if role == 'Admin':
			return view_func(request, *args, **kwargs)

		else:
			return redirect('landing_page')

	return wrapper_function
