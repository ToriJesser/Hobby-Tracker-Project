from django.shortcuts import render, redirect, get_object_or_404
from .models import LegoSet
from .forms import LegoSetForm


#View function that renders the home page - no context needed
def home(request):
    return render(request, 'mylegos/mylegos_home.html')

#View function that controls the main index page - list of lego sets
def index(request):
    get_legoset = LegoSet.LegoSets.all()      #Gets all the current lego sets from the database
    context = {'legosets': get_legoset}      #Creates a dictionary object of all the lego sets for the template
    return render(request, 'mylegos/mylegos_index.html', context)

#View function to add a new jersey to the database
def add_set(request):
    form = LegoSetForm(request.POST or None)     #Gets the posted form, if one exists
    if form.is_valid():                         #Checks the form for errors, to make sure it's filled in
        form.save()                             #Saves the valid form/jersey to the database
        return redirect('listLegos')                #Redirects to the index page, which is named 'mylegos' in the urls
    else:
        print(form.errors)                      #Prints any errors for the posted form to the terminal
        form = LegoSetForm()                     #Creates a new blank form
    return render(request, 'mylegos/mylegos_create.html', {'form':form})

#View function to look up the details of a jersey
def details_set(request, pk):
    pk = int(pk)                                #Casts value of pk to an int so it's in the proper form
    legoset = get_object_or_404(LegoSet, pk=pk)   #Gets single instance of the jersey from the database
    context={'Lego_Set':legoset}                   #Creates dictionary object to pass the jersey object
    return render(request,'mylegos/mylegos_details.html', context)

#View function to edit the database
def edit_set(request, pk):
    pk = int(pk)
    legoset = get_object_or_404(LegoSet, pk=pk)
    if request.method == 'POST':
        form = LegoSetForm(request.POST, instance=legoset)
        if form.is_valid():
            legoset = form.save()
            legoset.save()
            return redirect('setDetails', pk=legoset.pk)
    else:
        form = LegoSetForm(instance=legoset)
    context = {'form':form}
    return render(request, 'mylegos/mylegos_edit.html', context)

def delete(request, pk):
    pk = int(pk)
    legoset = get_object_or_404(LegoSet, pk=pk)
    if request.method == 'POST':
        legoset.delete()
        return redirect('listLegos')
    context = {'legoset': legoset}
    return render(request, "mylegos/mylegos_confirmdelete.html", context)


