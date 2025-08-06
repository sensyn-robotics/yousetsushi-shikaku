import cv2
import pymupdf

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

            # TODO: Handle PDF input    
            elif self.file_path.endswith('.pdf'):
                
                pages = []

                doc = pymupdf.open(self.file_path)
                for page in doc:
                    pix = page.get_pixmap()
                    # pix.save("output.jpg")
                    pages.append(pix)

                    # ''''
                    # zoom_x = 2.0  # horizontal zoom
                    # zoom_y = 2.0  # vertical zoom
                    # mat = pymupdf.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension
                    # pix = page.get_pixmap(matrix=mat)  # use 'mat' instead of the identity matrix
                    # '''

                return pages

            else:
                raise ValueError("Unsupported file type: ",self.file_path)
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            return None