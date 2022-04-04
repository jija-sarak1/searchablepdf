import pdf2image
def image_conversion(inpath,image_path):
  print("converting to image")
  OUTPUT_FOLDER = None
  FIRST_PAGE = None
  LAST_PAGE = None
  FORMAT = 'jpg'
  USERPWD = None
  USE_CROPBOX = False
  STRICT = False

  pil_images = pdf2image.convert_from_path(inpath,
                                          output_folder = OUTPUT_FOLDER,
                                          first_page = FIRST_PAGE,
                                          last_page = LAST_PAGE,
                                          fmt = FORMAT,
                                          userpw = USERPWD,
                                          use_cropbox= USE_CROPBOX,
                                          strict = STRICT )
  for image in pil_images :
    image.save(image_path+"image_converted.jpg")
inpath = ("/home/jija/Documents/ocrfolder/scannedtosearchablepdf/inpath/caveat.png.pdf")
image_path = ("/home/jija/Documents/ocrfolder/scannedtosearchablepdf/image_path/")
image_conversion(inpath , image_path)

import cv2
import pytesseract

input_dir = "/home/jija/Documents/ocrfolder/scannedtosearchablepdf/image_path/image_converted.jpg"
img = cv2.imread(input_dir , 1)
result = pytesseract.image_to_pdf_or_hocr(img,lang = "eng")
f = open("/home/jija/Documents/ocrfolder/scannedtosearchablepdf/output_pdf/searchablePDF.pdf","w+b")
f.write(bytearray(result))
f.close()