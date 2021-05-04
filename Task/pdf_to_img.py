import tempfile
from pdf2image import convert_from_path

pages = convert_from_path('/home/cgr/PYTHON/Task/images/invoice.pdf', 500)
n = 1
for page in pages:
    page.save('/home/cgr/PYTHON/Task/images/page.jpg', 'JPEG')
    # page.save('/home/cgr/PYTHON/Task/images/page' + str(n) + '.jpg', 'JPEG')
    n += 1

# images = convert_from_bytes(open('/home/cgr/Documents/Task/files.pdf', 'rb').read())
# print(images[0])

# with tempfile.TemporaryDirectory() as path:
#     images_from_path = convert_from_path('/home/cgr/Documents/Task/files.pdf', output_folder='/home/cgr/Documents/Task')