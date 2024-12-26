from utils.Preprocessing import Preprocessing
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

path_dataset = './dataset_original.csv'

dataset = pd.read_csv(path_dataset, sep = ',', header = 0)
dataset.head(10)

dataset['gender'] = dataset['gender'].str.strip("[]'")
dataset.head(10)

preprocessing = Preprocessing()

print('hola')
dataset['bio'] = dataset['bio'].apply(preprocessing.lowercase)
dataset['bio'] = dataset['bio'].apply(preprocessing.duplicates)
dataset['bio'] = dataset['bio'].apply(preprocessing.remove_numbers)
dataset['bio'] = dataset['bio'].apply(preprocessing.replace_abbreviations)
dataset['bio'] = dataset['bio'].apply(preprocessing.translate_emojis)
print(dataset['bio'].head(10))

tqdm.pandas(desc= 'Traduciendo bios...')
#dataset['bio'] = dataset['bio'].progress_apply(preprocessing.translate_to_english)
# Aplicar traducción en paralelo
with ThreadPoolExecutor(max_workers=5) as executor:  # Number of threads to use
    # Wrap the executor.map with tqdm for progress tracking
    dataset['bio'] = list(tqdm(executor.map(preprocessing.translate_to_english, dataset['bio']), total=len(dataset), desc='Traduciendo bios...'))

dataset.to_csv('dataset_translated.csv', index = False)
print(dataset.head(10))

