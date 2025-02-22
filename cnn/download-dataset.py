from pathlib import Path
from quickdraw import QuickDrawDataGroup, QuickDrawData
import json

image_size = (28, 28)

def generate_class_images(name, max_drawings, recognized):
    directory = Path("dataset/" + name)

    if not directory.exists():
        directory.mkdir(parents=True)

    images = QuickDrawDataGroup(name, max_drawings=max_drawings, recognized=recognized)
    for img in images.drawings:
        filename = directory.as_posix() + "/" + str(img.key_id) + ".png"
        img.get_image(stroke_width=3).resize(image_size).save(filename)

f = open('labels2.json', 'r')
labels_obj = json.load(f)
labels = list(labels_obj.keys())
f.close()

for label in QuickDrawData().drawing_names:
    if label in labels:
        generate_class_images(label, max_drawings=1200, recognized=True)