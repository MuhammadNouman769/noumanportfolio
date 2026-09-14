from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thanks for reaching out! Your message has been received — I'll get back to you soon."
            )
            return redirect('contact:contact')
        messages.error(request, 'Please fix the errors below and try again.')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
