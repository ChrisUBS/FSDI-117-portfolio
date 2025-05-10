from django.shortcuts import render
from portfolio.models import skill
from .forms import ContactForm
from django.core.mail import send_mail

def HomePageView(request):
    skills = skill.objects.all()
    
    return  render(request, 'pages/home.html', {'skills': skills})

def AboutPageView(request):
    skills = skill.objects.all()
    
    return  render(request, 'pages/about.html', {'skills': skills})

def ContactPageView(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        
        # Collect the data of the form
        if form.is_valid():
            print("The Data is Valid")
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            
            # This is the email
            message_body = (
                f"You have a new email from your portfolio\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Message: {message}"
            )
            
            # Try to send the email!
            try:
                # send_email <-- Django Core Email
                send_mail(
                    "Email from Portfolio",            # Subject
                    message_body,                      # Message Body -> What the user typed
                    email,                             # From email -> The user's email
                    ['christian.bonilla@uabc.edu.mx']  # To email -> Here you want to get the email message
                )
                
                print("Email sent successfully")
                
                # Render and redirect user
                return render(request, 'pages/contact.html', {"form": ContactForm()})
            except Exception as e:
                print(f"Error sending the email: {e}")
                return render(request, 'pages/contact.html', {
                    "form": form,
                    "error": str(e)
                })
        else:
            print("The Data is not Valid")
    else:
        # There is not POST request
        form = ContactForm()
    
    return render(request, 'pages/contact.html', {"form": form})
