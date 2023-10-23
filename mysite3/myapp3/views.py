from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from django.db.utils import IntegrityError
from datetime import timedelta
from .forms import CreateContactForm,UpdateContactForm
from .models import ContactList


def home(request):
    return render(request, 'myapp3/home.html')
    
def create_contact(request):
    if request.method == 'POST':
        form = CreateContactForm(request.POST)
        try:
            if form.is_valid():
              formdata = form.cleaned_data
              name = formdata['name']
              address = formdata['address']
              profession = formdata['profession']
              telnumber = formdata['telnumber']
              email = formdata['email']
              datejoined= formdata['datejoined']
              dateexpired = formdata['dateexpired']

              ContactList.objects.create(name=name, address=address,profession=profession, telnumber=telnumber,email=email,datejoined=datejoined,dateexpired=dateexpired)
              return render(request, 'myapp3/success.html')
        except IntegrityError as e:
            if 'UNIQUE constraint failed: myapp3_contact.name' in str(e):
                return render(request, 'myapp3/success.html')#ignore request but pretend the request was successful
            else:
                raise e
    else:
        form = CreateContactForm()
    
    return render(request, 'myapp3/createcontact.html', {'form': form})

def contact_list(request):
    contacts = ContactList.objects.all()
    return render(request, 'myapp3/contact_list.html', {'contacts': contacts})


def update_contact(request, pk):
    contact = get_object_or_404(ContactList, pk=pk)
    
    if request.method == 'POST':
        form = UpdateContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = UpdateContactForm(instance=contact)
    
    return render(request, 'myapp3/update_contact.html', {'form': form, 'contact': contact})


def delete_contact(request, pk):
    contact = get_object_or_404(ContactList, pk=pk)
    
    if request.method == 'POST':
        # Calculate the difference between dateexpired and datejoined
        date_difference = contact.dateexpired - contact.datejoined

        # Check if the difference is less than 1 year (365 days)
        if date_difference < timedelta(days=365):
            # Display a message to the user
            return HttpResponse("Contact cannot be deleted because the expiry date is less than 1 year from the join date.")
        
        # If the condition is not met, proceed with deletion
        contact.delete()
        return redirect('contact_list')
    
    return render(request, 'myapp3/delete_contact.html', {'contact': contact})