import cv2

from utils.file_input import FileInput
from utils.card import Card



def main():
    print("Hello, World!")

    jpg_file = "data/溶接免許_難波豊.jpg"
    pdf_file = "data/M-111_仲野信人_C-2P_20160731.pdf"

    # Get images and pdfs into usable format
    pages = FileInput(jpg_file).read()
    # print(file)
    # cv2.imshow("hi",file[0])
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    # Isolate the card from the images/pages


    # Perform OCR


    # Perform masking


    

if __name__ == "__main__":
    main()