from PIL import Image
import pytesseract
from os import walk
from os.path import isfile,join
import sys
from glob import glob

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Marti\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'

def GetFiles(route="./Dataset/"):
    listfiles_def=[]
    for (dirpath,dirname,listfiles) in walk(route):
        listfiles_def.extend([dirpath+"/"+fi for fi in listfiles if isfile(join(dirpath,fi))])
    
    if len(listfiles_def)==0: raise "There's no files in the directory!"
    
    return listfiles_def

def ReadImage(filename=".\\"):
    pass





if __name__ == "__main__":
  GetFiles()