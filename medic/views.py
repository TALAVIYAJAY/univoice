from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from googletrans import Translator  # Google Translate API for text translation
from .models import tln  # Import the model for storing translations
import json

# Home page view
def home(request):
    """
    Renders the home page.

    This function returns the 'home.html' template when the user accesses the root URL.
    Ensure that 'home.html' is placed inside the templates folder.
    """
    return render(request, "home.html")

# Translation API view
@csrf_exempt  # Disable CSRF protection for this view (use with caution in production)
def translate_text(request):
    """
    Handles translation requests via a POST request.

    This function:
    - Parses the JSON request body to extract the input text and selected languages.
    - Uses Google Translate API to translate the text.
    - Stores the translation in the database.
    - Returns the translated text as a JSON response.

    Expected JSON request format:
    {
        "text": "Hello",
        "source_lang_code": "en",
        "source_lang_name": "English",
        "target_lang_code": "hi",
        "target_lang_name": "Hindi"
    }
    """
    if request.method == "POST":
        try:
            # Parse JSON request data
            data = json.loads(request.body)
            input_text = data.get("text", "")  # Extract input text
            source_lang_code = data.get("source_lang_code", "en")  # Default source language is English
            source_lang_name = data.get("source_lang_name", "English")  # Default source language name
            target_lang_code = data.get("target_lang_code", "hi")  # Default target language is Hindi
            target_lang_name = data.get("target_lang_name", "Hindi")  # Default target language name

            # Validate input text
            if not input_text:
                return JsonResponse({"error": "No text provided"}, status=400)

            # Perform translation using Google Translate API
            translator = Translator()
            translated_text = translator.translate(input_text, dest=target_lang_code).text

            # Debugging output (prints to server console)
            print('-----------------')
            print('Input Language Name: ', source_lang_name)
            print('Output Language Name: ', target_lang_name)
            print('Input Language Code: ', source_lang_code)
            print('Output Language Code: ', target_lang_code)
            print('Input Text : ', input_text)
            print('Output Text : ', translated_text)

            # Save translation to the database
            user_translation = tln(
                input_text=input_text,
                output_text=translated_text,
                input_language=source_lang_name,
                output_language=target_lang_name
            )
            user_translation.save()

            # Return the translated text as JSON response
            return JsonResponse({"translation": translated_text})

        except Exception as e:
            # Handle any errors that occur during translation
            return JsonResponse({"error": f"Translation failed: {str(e)}"}, status=500)

    # Return an error if the request method is not POST
    return JsonResponse({"error": "Invalid request method"}, status=400)
