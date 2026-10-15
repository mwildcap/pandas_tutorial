import pandas as pd
import rasterio
import matplotlib.pyplot as plt
data = pd.read_csv("data/kumpula-summer-2024.txt", comment='#')
OUTPUT_FP = "filename_data"
data.to_csv(OUTPUT_FP, sep=",")
print(data.head())