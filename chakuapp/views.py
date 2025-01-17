from django.http import HttpResponse
from django.shortcuts import redirect, render
from chakuapp.models import Person
from django.contrib import messages

# Create your views here.
def index(request):
    persons = Person.objects.all()
    return render(request,"index.html",{"persons":persons})

def about(request):
    return render(request,"about.html")

def form(request):
    if request.method == "POST":
        name = request.POST["name"]
        age = request.POST.get("age")
        print(f"""name : {name}, age : {age}""")

        # -- save DB
        # person = Person.objects.create(
        #     name=name,
        #     age=age
        # )
        person = Person()
        person.name = name
        person.age = age
        eqm = request.POST.getlist("eqm[]")
        print(request.POST)
        print(eqm)
        # person.save()
        messages.success(request,"save success")

        return redirect("/")
    else :
        chk = [{"id":1,"name":"pen"},{"id":2,"name":"pencil"}]
        return render(request,"form.html",{"chk":chk})
    
def edit(request,person_id):
    person = Person.objects.get(id=person_id)
    if request.method == "POST":
        person.name = request.POST["name"]
        person.age = request.POST["age"]
        person.save()

        messages.success(request,"update success")
        return redirect("/")
    else :
        return render(request,"edit.html",{"person":person})
    
def delete(request,person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    messages.success(request,"delete success")
    return redirect("/")