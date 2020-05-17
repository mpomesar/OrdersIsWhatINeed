from PIL import Image
import pytesseract
from os import walk
from os.path import isfile,join
import sys
from glob import glob
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Marti\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'

def GetFiles(route="./Dataset/"):
    listfiles_def=[]
    for (dirpath,dirname,listfiles) in walk(route):
        listfiles_def.extend([dirpath+"/"+fi for fi in listfiles if isfile(join(dirpath,fi))])
    
    if len(listfiles_def)==0: raise "There's no files in the directory!"
    
    return listfiles_def

def ReadImage(filename=".\\"):

    return "lala"



if __name__ == "__main__":
  GetFiles()