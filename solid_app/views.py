# solid_app/views.py
import io
from django.shortcuts import render
from httpx import HTTPStatusError
from solid.auth import Auth
from solid.solid_api import SolidAPI


#  python manage.py runserver 
def add_text_file_to_solid(request):
 if request.method == 'POST':
    # Replace with your Solid Pod details from solidcommunity.net
    
    #https://engarif5.solidcommunity.net/
    # POD_ENDPOINT = 'https://engarif5.solidcommunity.net/'
    # engarif5
    # Germany@-14 
    USERNAME = request.POST.get('username') 
    PASSWORD = request.POST.get('password')
    POD_ENDPOINT = f'https://{USERNAME}.solidcommunity.net/'
    PRIVATE_RES = POD_ENDPOINT + f'private/{USERNAME}.txt'

    # Initialize SolidAPI with authentication
    auth = Auth()
    api = SolidAPI(auth)
    auth.login(POD_ENDPOINT, USERNAME, PASSWORD)

    # Check if the file exists
    file_exists = api.item_exists(PRIVATE_RES)

    if not file_exists:
        try:
            # Create a text file
            file_content = f"Hello {USERNAME}"
            f = io.BytesIO(file_content.encode('UTF-8'))
            api.put_file(PRIVATE_RES, f, 'text/plain')

            # Read the folder to verify the file creation
            folder_data = api.read_folder(POD_ENDPOINT)
            files_in_folder = [item.name for item in folder_data.files]

            return render(request, 'success.html', {'files_in_folder': files_in_folder})
        except HTTPStatusError as e:
            return render(request, 'error.html', {'error_message': f"Error during request: {str(e)}"})
    else:
        return render(request, 'success.html', {'message': 'File already exists'})
 else:
  return render(request, 'login.html')

