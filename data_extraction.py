from ucimlrepo import fetch_ucirepo 
from google.cloud import bigquery
import os
import pandas as pd

# Get le dossier de travail actuel
current_dir = os.path.dirname(os.path.abspath(__file__))

# Crée le chemin complet
key_path = os.path.join(current_dir, 'projet-integration-au-2024-81640cb2db70.json')

# Remplacer par le chemin vers votre fichier de clé JSON
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path

# Fetch dataset
phiusiil_phishing_url_website = fetch_ucirepo(id=967)

# Données
X = phiusiil_phishing_url_website.data.features
y = phiusiil_phishing_url_website.data.targets

# Combiner les features et les targets en un seul DataFrame pour importation
df = pd.concat([X, y], axis=1)

# Afficher un aperçu des données
print(df.head())

# Initialiser le client BigQuery
client = bigquery.Client()

# Définir le dataset_id
dataset_id = 'sacha_phishing_url_website'  # Juste le nom du dataset, sans le projet

# Créer le dataset s'il n'existe pas déjà
try:
    client.get_dataset(dataset_id)  # Tenter de récupérer le dataset
    print(f"Dataset {dataset_id} existe déjà.")
except Exception:
    # Si le dataset n'existe pas, il sera créé
    dataset = bigquery.Dataset(f"{client.project}.{dataset_id}")
    dataset.location = "US"  # Spécifiez la région du dataset si nécessaire
    dataset = client.create_dataset(dataset, timeout=30)
    print(f"Dataset {dataset_id} créé avec succès.")

# Définir la référence à la table
table_id = 'sacha_table_initial_raw'
table_ref = client.dataset(dataset_id).table(table_id)

# Créer la table si elle n'existe pas
try:
    client.get_table(table_ref)  # Tenter de récupérer la table
    print(f"Table {table_id} existe déjà.")
except Exception:
    # Si la table n'existe pas, elle sera créée
    schema = [
        bigquery.SchemaField(name, "STRING") if dtype == 'object' else bigquery.SchemaField(name, "FLOAT64")
        for name, dtype in df.dtypes.items()
    ]
    table = bigquery.Table(table_ref, schema=schema)
    table = client.create_table(table)
    print(f"Table {table_id} créée avec succès.")

# Charger les données dans BigQuery
job = client.load_table_from_dataframe(df, table_ref)

# Attendre que la tâche soit terminée
job.result()

print(f"Les données ont été importées dans la table {table_id}.")

# Exécuter une requête pour vérifier les données
query = f"SELECT * FROM `{client.project}.{dataset_id}.{table_id}` LIMIT 10"
query_job = client.query(query)

for row in query_job:
    print(row)
