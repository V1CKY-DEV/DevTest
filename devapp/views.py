from django.core.mail import send_mail
from django.shortcuts import render
from django.http import JsonResponse
from .forms import UploadFileForm
from django.core.files.storage import default_storage
import pandas as pd
import os

def handle_uploaded_file(f):
    upload_dir = 'uploads/'
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    file_path = os.path.join(upload_dir, f.name)
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path

def generate_summary(file_path):
    try:
        ext = os.path.splitext(file_path)[1].lower()
        if ext == '.csv':
            df = pd.read_csv(file_path)
        elif ext in ['.xls', '.xlsx']:
            df = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file type")
        summary = df.describe().to_string()
    except Exception as e:
        summary = f"Error generating summary: {str(e)}"
    return summary

def upload_file(request):
    if request.method == 'POST':
        if 'filepond' in request.FILES:
            file = request.FILES['filepond']
            file_path = handle_uploaded_file(file)
            summary = generate_summary(file_path)
            subject = 'Python Assignment - Burhan Farooq Dar'
            try:
                send_mail(
                    subject=subject,
                    message=summary,
                    from_email='your-email@gmail.com',
                    recipient_list=['recipient1@example.com', 'recipient2@example.com'],
                )
                return JsonResponse({'success': True, 'summary': summary})
            except Exception as e:
                return JsonResponse({'success': False, 'error': f"Error sending email: {str(e)}"})
        else:
            return JsonResponse({'success': False, 'error': 'No file uploaded'})
    else:
         return JsonResponse({'success': False, 'error': 'Invalid request method'})

def home(request):
    if request.method == 'POST':
        return upload_file(request)
    else:
        form = UploadFileForm()
    return render(request, 'devapp/home.html', {'form': form})

def success(request):
    return render(request, 'devapp/success.html')
