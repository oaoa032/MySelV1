import requests
import sys
from colorama import init, Fore
from tqdm import tqdm

# Initialisation de Colorama
init(autoreset=True)

print(Fore.YELLOW + """
███╗░░░███╗██╗░░░██╗░██████╗███████╗██╗░░░░░  ██╗░░░██╗░░███╗░░
████╗░████║╚██╗░██╔╝██╔════╝██╔════╝██║░░░░░  ██║░░░██║░████║░░
██╔████╔██║░╚████╔╝░╚█████╗░█████╗░░██║░░░░░  ╚██╗░██╔╝██╔██║░░
██║╚██╔╝██║░░╚██╔╝░░░╚═══██╗██╔══╝░░██║░░░░░  ░╚████╔╝░╚═╝██║░░
██║░╚═╝░██║░░░██║░░░██████╔╝███████╗███████╗  ░░╚██╔╝░░███████╗
╚═╝░░░░░╚═╝░░░╚═╝░░░╚═════╝░╚══════╝╚══════╝  ░░░╚═╝░░░╚══════╝
""")

# Vérifier si il n'y a pas eu de mis à jours 
def check_latest_version(repo_owner, repo_name, current_version):
    try:
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
        response = requests.get(url)
        if response.status_code == 200:
            latest_version = response.json()["tag_name"]
            if latest_version != current_version:
                print(f"There is a new version available: {latest_version}")
                input("[+] Press any key for conitnue")
            else:
                print("You have the latest version.")
                check_internet_connection()
        else:
            print("Failed to retrieve latest version information.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Remplacez ces valeurs par votre propre nom de dépôt, propriétaire du dépôt et numéro de version actuelle
repo_owner = "owner_name"
repo_name = "repository_name"
current_version = "1.0.0"

check_latest_version(repo_owner, repo_name, current_version)



# Fonction pour vérifier si l'utilisateur est connecté à Internet
def check_internet_connection():
    try:
        response = requests.get("http://www.google.com")
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError:
        return False

# Clé d'authentification
pass_key = "noxW0LimEg6vw28LofnOUenqxSjoigjM"
user_input = input(Fore.YELLOW + "[+] Enter a passkey: ")

# Vérification de la clé d'authentification
if user_input == pass_key:
    print(Fore.GREEN + "[+] Thanks you for downloading my v1 of python project! #madebyneon")
    
    # Vérification de la connexion Internet
    if check_internet_connection():
        # Lien de téléchargement depuis MediaFire
        url = 'https://download1501.mediafire.com/rirppiu0555gqSCUukuyEhp0AKZYl9iVmVC64hREMBoirO0Kdu9RlpKGDyD0OLNWCZbt8NahgeKtPOwvOVtNmhmUYhl2DRj-gWzA5s_vTngTJTwTeCrIXC49PBBLaNcgO3aRMY74gxhfoOkL5L5d4Nr78Nr5Qw1AvDOdIJYVWYYH/oyv3l594ew4lmmi/MegaHackV8.zip'

        # Début du téléchargement
        print(Fore.CYAN + f'[+] Download has started !')

        # Vérification et téléchargement du fichier
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            total_size_in_bytes = int(response.headers.get('content-length', 0))
            block_size = 1024 # 1 Kilobyte
            progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True, desc=f"{Fore.GREEN}[+] Download... Please wait: ")
            
            # Écriture des données téléchargées dans un fichier
            with open('downloaded_file.zip', 'wb') as file:
                for data in response.iter_content(block_size):
                    progress_bar.update(len(data))
                    file.write(data)
            progress_bar.close()
            
            print(Fore.GREEN + '[+] Download completed successfully!')
        else:
            print(Fore.RED + "[-] Something went wrong... Please check your Internet connection and try again!")
    else:
        print(Fore.RED + "[-] Something went wrong... Please check your Internet connection and try again!")
else:
    print(Fore.RED + " [+] Wrong Auth Key!")
    sys.exit()

# Made by neon 
# No skid
# Share with credits @neon_321
