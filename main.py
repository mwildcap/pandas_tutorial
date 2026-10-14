import pandas as pd
import rasterio
import matplotlib.pyplot as plt
data = pd.read_csv("data/kumpula-summer-2024.txt", comment='#')
output_fp = "filename_data"
data.to_csv(output_fp, sep=",")
print(len(data.columns.values))

raster_path = "https://github.com/opengeos/datasets/releases/download/raster/LC09_039035_20240708_90m.tif"
src = rasterio.open(raster_path)
band1 = src.read(1)
print(src)


plt.figure(figsize=(8, 8))
plt.imshow(band1, cmap="gray")  # Toon als grijswaarden
plt.title("TIFF Visualisatie")
plt.colorbar(label="Pixelwaarde")
plt.show()