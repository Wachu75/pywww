from django.shortcuts import render, get_object_or_404
from main.forms import ContactForm, UserProfileForm
from . import services
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper



# Create your views here.
def contact(request):
    if request.method == "POST":    # jeżeli metoda przesyłania danych to POST wtedy utwórz formularz
        form = ContactForm(data=request.POST) # z danych które są w POST
        if form.is_valid():         # jeżeli dane są poprawne to ...
            print("zwrotka")
            services.send_message(form.cleaned_data) #wyślij mi je jako wyczyszczone-sformatowane
            return HttpResponseRedirect(reverse("main:contact"))  # ponieważ po wysłaniu nie czyści formularza i nie wiadomo co
            # tak właściwie zaszło to możemy użyć redirect - przekierowanie urzytkownika na konkretny adres które w tym przypadku
            # przekieruje nas do formularza "contakt", reverse zamieni zawartość w () na konkretny adres url
    else:       # jeżeli to nie jest metoda POST utwórz
        form = ContactForm() #pusty formularz
    return render(request, "main/contact.html", {"form": form}) # i wyświetl go na stronie


def hello_world(request):
    return render(request, 'main/about.html')


def user_profile(request, user_id):
    user = get_object_or_404(get_user_model(), id=user_id)
    if request.method == "POST":
        try:
            profile = user.userprofile
            form = UserProfileForm(request.POST, instance=profile)
        except AttributeError: pass
        if form.is_valid(): form.save()
    else:
        try:
            profile = user.userprofile
            form = UserProfileForm(instance=profile)
        except AttributeError:
            form = UserProfileForm(initial={"user": user, "bio": "---"})
        if request.user != user:
            for field in form.fields:
                form.fields[field].disabled = True
            #form.inputs = []
            print(form)
    return render(request, 'main/userprofile.html', {'form': form})

