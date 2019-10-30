from helpers import fetch


def fetch_doggos():
    response = fetch('https://dog.ceo/api/breeds/list/all')
    breed_images = []
    for breed in response['message'].keys():
        url = f'https://dog.ceo/api/breed/{breed}/images/random'
        breed_images.append(fetch(url))
    return breed_images

doggo_responses = fetch_doggos()
for doggo_response in doggo_responses:
    print(doggo_response['message'])
