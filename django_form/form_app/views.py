from django.shortcuts import render
from .forms import FeedbackForm
import json
import os
from .firebase_config import db

# Create your views here.

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            db.child("feedbacks").push(data)
            file_path = os.path.join(os.path.dirname(__file__), 'responses.json')
            try:
                with open(file_path, 'r') as file:
                    responses = json.load(file)
            except FileNotFoundError:
                responses = []

            responses.append(data)

            with open(file_path, 'w') as file:
                json.dump(responses, file, indent=4)

            return render(request, 'form_app/thank_you.html', {'first_name': data['first_name']})
    else:
        form = FeedbackForm()
    return render(request, 'form_app/form.html', {'form': form})