from django.contrib.auth import authenticate, login
from django.conf import settings
from django.db.models import Q
from django.shortcuts import redirect, render
from .models import Visitor, VisitorForm

# Create your views here.
# query objects
def get_queryset(request): # new
    if request.method== "POST":
        query = request.POST.get('search_visitors')
        print(query)
        return Visitor.objects.filter(
            Q(name__icontains=query))
    return Visitor.objects.all()


# Send a home_page with details of visitors
def home_page(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    all_visitors =  get_queryset(request);
    return render(request,'design_hub_app/homepage.html', {'visitors' : all_visitors })

# Send a login page 
def login_page(request):  
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('/home')    
    else:  
        if request.method == "POST":
            context = { 'message': 'Please login with right credentials' }
            return render(request, 'design_hub_app/login.html',context= context )       
        return render(request, 'design_hub_app/login.html')       


# Add new visitor
def add_new_visitor(request):
    submitted = False

    if request.method == 'POST':
        form = VisitorForm(request.POST)
        
        if form.is_valid():
             form.save()
             return redirect('/add_new_visitor/?submitted=True')
    else:
        form = VisitorForm()
        if 'submitted' in request.GET:
             submitted = True 
    return render(request, 'design_hub_app/add_new_visitor.html', {'form': form, 'submitted': submitted})
   