import cv2
import numpy as np
from pdf2image import convert_from_path
# import pymupdf

class FileInput:
    """
    Class to handle file input operations.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        
    def read(self):
        try:
            if self.file_path.endswith('.jpg') or self.file_path.endswith('.png') or self.file_path.endswith('.jpeg'):
                return [cv2.imread(self.file_path)]

                
            elif self.file_path.endswith('.pdf'):
                
                

                images = [cv2.cvtColor(np.array(pil), cv2.COLOR_RGB2BGR) for pil in convert_from_path(self.file_path, dpi=200)]

                # doc = pymupdf.open(self.file_path)
                # for page in doc:
                #     pix = page.get_pixmap()
                #     # pix.save("output.jpg")
                #     pages.append(pix)

                    # ''''
                    # zoom_x = 2.0  # horizontal zoom
                    # zoom_y = 2.0  # vertical zoom
                    # mat = pymupdf.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension
                    # pix = page.get_pixmap(matrix=mat)  # use 'mat' instead of the identity matrix
                    # '''

                return images

            else:
                raise ValueError("Unsupported file type: ",self.file_path)
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            return None
        



'''
Consider this later maybe
import fitz  # PyMuPDF
from PIL import Image
import io

def convert_pdf_to_images(pdf_path: str):
    """
    Converts each page of a PDF file into a list of PIL Image objects.
    """
    pdf_document = fitz.open(pdf_path)
    images = []
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()
        img_data = pix.tobytes("png")
        image = Image.open(io.BytesIO(img_data))
        images.append(image)
    return images
'''