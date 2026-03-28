from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import pydicom

metadata = pd.read_csv('Metadata.csv')
data_dir = Path('data')

available_files = sorted(
    path
    for path in data_dir.iterdir()
)
available_ids = {path.name for path in available_files}

# Filter metadata to include only rows with ImageIDs that have corresponding files in the data directory
metadata_subset = metadata[metadata['ImageID'].isin(available_ids)].head(6)



if metadata_subset.empty:
    raise RuntimeError(
        'No matching ImageID between Metadata.csv and files in data/. '
        'Check dataset download/extraction.'
    )

fig, axes = plt.subplots(2, 3, figsize=(12, 8))
axes = axes.flatten()

# for axis in axes:

for axis, (_, row) in zip(axes, metadata_subset.iterrows()):
    axis.axis('off')
    image_id = row['ImageID']
    image_path = data_dir / image_id
    
    ds = pydicom.dcmread(str(image_path))
    image = ds.pixel_array

    axis.imshow(image, cmap='gray')
    axis.set_title(f'Image ID: {image_id}')

fig.tight_layout()
plt.show()