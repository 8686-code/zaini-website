from django.shortcuts import render, redirect,HttpResponse

from business.models import Contact

from django.contrib import messages

from django.core.mail import EmailMessage

from django.core.mail import send_mail

from django.conf import settings

from django.core.files.storage import default_storage

from django.core.files.base import ContentFile


def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "home.html")

def product(request):
    return render(request,"home.html")

def dealers(request):
    return render(request, "home.html")

from django.core.exceptions import ValidationError

def contact(request):
    if request.method == "POST":
        # Retrieve form data
        name = request.POST.get("name")
        mobile_number = request.POST.get("mobile_number")
        email = request.POST.get("email")
        state = request.POST.get("state")
        required_part = request.POST.get("required_part")
        make = request.POST.get("make")
        model = request.POST.get("model")
        description = request.POST.get("description")
        image = request.FILES.get("image")

        try:
            Contact._meta.get_field("description").max_length = 500
            contact = Contact(
                name=name, mobile_number=mobile_number, email=email, state=state,
                required_part=required_part, make=make, model=model, description=description,
                image=image
            )
            contact.full_clean()
        except ValidationError as e:
            if "description" in e.error_dict:
                description = description[:500]
                contact = Contact(
                    name=name, mobile_number=mobile_number, email=email, state=state,
                    required_part=required_part, make=make, model=model, description=description,
                    image=image
                )
            else:
                raise

        if image:
            # Save the image file to the storage
            file_name = default_storage.generate_filename(image.name)
            default_storage.save(file_name, image)
            image_url = default_storage.url(file_name)[:256]
    
            # Open the saved image file and read its content
            with default_storage.open(file_name) as file:
                file_content = file.read()
    
            # Create a ContentFile using the read file content and assign it to the contact's image field
            image_file = ContentFile(file_content, name=file_name)
            contact.image.save(file_name, image_file)
    
        contact.save()
    
        send_email(request, name, mobile_number, email, state, required_part, make, model, contact.image, description)
    
    return render(request, "contact.html")


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import COMMASPACE

import imghdr
def send_email(request, name, mobile_number, email, state, required_part, make, model, image, description):
    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = 'zainiomp@gmail.com'
    msg['To'] = 'zainiomp@gmail.com'
    msg['Subject'] = 'New Order From Customer!'
    
    # Create the HTML body of the email
    body = f'''
        <html>
            <body>
                <p>Name: {name}</p>
                <p>Mobile Number: {mobile_number}</p>
                <p>E-Mail: {email}</p>
                <p>State: {state}</p>
                <p>Required Part: {required_part}</p>
                <p>Make: {make}</p>
                <p>Model: {model}</p>
                <p>Description: {description}</p>
                <img src="cid:image">
            </body>
        </html>
    '''
    
    # Attach the HTML body as part of the email
    msg.attach(MIMEText(body, 'html'))

    # Handle the uploaded image
    if image:
        # Determine the MIME type of the image using imghdr
        with default_storage.open(image.name) as image_file:
            image_content_type = imghdr.what(None, h=image_file.read())

        # Attach the image file to the email as an inline attachment
        image.seek(0)
        image_mime = MIMEImage(image.read(), _subtype=image_content_type)
        image_mime.add_header('Content-Disposition', 'inline', filename='image')
        image_mime.add_header('Content-ID', '<image>')
        msg.attach(image_mime)

    # Connect to Gmail SMTP server and send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('zainiomp@gmail.com', 'uqwfrodkqbizxvdb')
        server.send_message(msg)
        server.quit()
        messages.success(request, "Thank you for reaching out! We will get back to you soon.")
    except Exception as e:
        messages.error(request, f"Failed to send email: {e}")

    return redirect('/contact')


