import random
import os
import shutil

img = os.listdir("./output_1")
selected_images = random.choices(img, k=500)
print(selected_images)

os.makedirs("./to_label")
for img in selected_images:
    shutil.move("./output_1/" + img, "./to_label")
