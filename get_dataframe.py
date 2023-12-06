import requests
import tarfile
import os
import shutil

destination_folder = "dataframe"
temp_extract_path = "temp_extract"
final_file_path = f"{destination_folder}/"
tar_file_path = f"{destination_folder}.tar"


try:
    if not os.path.exists(f"{destination_folder}"):
        os.makedirs(f"{destination_folder}")
        print("Le dossier dataframe a bien été créé.")
        print("Téléchargement du dataframe...")
        response = requests.get(
            "https://data.musicbrainz.org/pub/musicbrainz/listenbrainz/"
            "incremental/listenbrainz-dump-1565-20231206-000003-incremental/"
            "listenbrainz-spark-dump-1565-20231206-000003-incremental.tar"
        )

        with open(f"{destination_folder}.tar", "wb") as f:
            f.write(response.content)

        with tarfile.open(tar_file_path, 'r') as tar:
            # Parcourir les membres de l'archive
            for member in tar.getmembers():
                if member.name.endswith('0.parquet'):
                    # Extraire le fichier dans un chemin temporaire
                    tar.extract(member, path=temp_extract_path)
                    extracted_file_path = os.path.join(temp_extract_path, member.name)

                    # Déplacer le fichier à l'emplacement final
                    shutil.move(extracted_file_path, final_file_path)
                    print(f"Le fichier {member.name} a été extrait et déplacé.")

                    # Supprimer le dossier temporaire
                    shutil.rmtree(temp_extract_path)
                    break

        os.remove(f"./{destination_folder}.tar")

        print(f"{response.status_code} OK - Téléchargement du dataframe terminé.")
    else:
        print("Le dataframe est déjà téléchargé.")

except Exception as e:
    print(e)
