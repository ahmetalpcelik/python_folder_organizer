import os
import shutil
from datetime import datetime

#made by Alp. Instagram: ahmetalpcelik

src = os.path.join(os.path.expanduser('~'), 'Desktop')
dst_x = os.path.join(os.path.expanduser('~'), 'Desktop', 'x')
dst_png = os.path.join(os.path.expanduser('~'), 'Desktop', 'pngler')
dst_blender = os.path.join(src, "blender")
dst_resimler = os.path.join(src, "resimler")
dst_dae = os.path.join(src, "dae")
dst_acnh = os.path.join(src, "acnh")
dst_objmtl = os.path.join(src, "obj ve mtl")

# create destination folders if they don't exist
if not os.path.exists(dst_blender):
    os.mkdir(dst_blender)
if not os.path.exists(dst_x):
    os.mkdir(dst_x)
if not os.path.exists(dst_png):
    os.mkdir(dst_png)

for file in os.listdir(src):
    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    # Get the file name and extension
    name, ext = os.path.splitext(file)
    # Add the timestamp to the file name
    new_name = f"{name} {timestamp}{ext}"
    if ext == '.x':
        # Move the file to the 'x' folder
        shutil.move(os.path.join(src, file), os.path.join(dst_x, new_name))
    elif ext == '.png':
        # Move the file to the 'pngler' folder
        shutil.move(os.path.join(src, file), os.path.join(dst_png, new_name))
    elif ext == '.blend':
        # Move the file to the 'pngler' folder
        shutil.move(os.path.join(src, file), os.path.join(dst_blender, new_name))
