import os
import shutil
import datetime

#alp was here

src = os.path.join(os.path.expanduser('~'), 'Desktop')

for file in os.listdir(src):
    if os.path.isfile(os.path.join(src, file)):
        # uzantiyi al
        extension = os.path.splitext(file)[1]
        # uzantiye gore klasor yap
        dst = os.path.join(src, extension[1:])
        # If the destination folder doesn't exist, create it
        if not os.path.exists(dst):
            os.mkdir(dst)
        # Saati tarihi falan al
        now = datetime.datetime.now()
        # Gun saat dakika yazdirdim. Saniye luzumsuz 
        timestamp = now.strftime("%Y-%m-%d_%H-%M")
        # dosya adını uzantisiz al
        file_name = os.path.splitext(file)[0]
        # yeni dosyayı olustur
        new_file_name = file_name + '_' + timestamp + extension
        # yeni ismiyle dosyayi tasi
        shutil.move(os.path.join(src, file), os.path.join(dst, new_file_name))
