import requests
import image_lib
import os

POKEMON_SEARCH_URL = 'https://pokeapi.co/api/v2/pokemon/'


def main():
    #poke_info = get_pokemon_info('LUGIA')
    #get_pokeman_names()
    download_pokemon_artwork('metapod', r'C:\kcsis')

    return


def get_pokemon_info(search_term):
    """Get the abilities for the specified pokemon

    Args:
        search_term (str): Name of Pokemon or PokeDex number

    Returns:
        list: List of ability. None if failed
    """

    # clean the search term
    search_term = str(search_term).strip().lower()

    # creating clean url for the search term
    CLEAN_POKEMON_SEARCH_URL = POKEMON_SEARCH_URL + search_term

    print(f'Getting information for {search_term}...', end='')
    resp_msg = requests.get(CLEAN_POKEMON_SEARCH_URL)

    # Check whether the request was successful
    if resp_msg.ok:
        print('success')
        body_dict = resp_msg.json()
        # HEIGHT, WEIGHT, TYPE, STATS
        # print(body_dict)
        # ability_portion = body_dict['abilities']
        # ability_list = [j['ability']['name'] for j in ability_portion]
        return body_dict
    else:
        print("failure")
        print(f"respose code: {resp_msg.status_code} ({resp_msg.reason})")

def get_pokeman_names(offset=0, limit=100000):
    query_params = {
        "limit" : limit,
        "offset" : offset
    }
# Send GET request for Pokeman names    
    print(f'Getting list of pokeman names...', end='')
    resp_msg = requests.get(POKEMON_SEARCH_URL, params=query_params)

    # Check whether the request was successful
    if resp_msg.ok:
        print('success')
        resp_dict = resp_msg.json()
        # HEIGHT, WEIGHT, TYPE, STATS
        # print(body_dict)
        # ability_portion = body_dict['abilities']
        # ability_list = [j['ability']['name'] for j in ability_portion]
        pokemon_names = [p["name"]for p in resp_dict['results']]
        return pokemon_names
    else:
        print("failure")
        print(f"respose code: {resp_msg.status_code} ({resp_msg.reason})")    

def download_pokemon_artwork(pokemon_name, folder_path):
           
           poke_info = get_pokemon_info(pokemon_name)
           if poke_info is None:
                return False

           poke_image_url = poke_info['sprites']['other']['official-artwork']['front_default']

           image_data = image_lib.download_image(poke_image_url)
           if image_data is None:
                return False

           #Determine the name of the path at which to save the image file
           image_ext = poke_image_url.split('.')[-1]
           file_name = f'{pokemon_name}.{image_ext}'
           file_path = os.path.join(folder_path, file_name)
           if image_lib.save_image_file(image_data, file_path):
                return file_path
           return False
           

           



if __name__ == '__main__':
    main()
