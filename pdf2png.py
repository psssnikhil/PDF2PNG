# -*- coding: utf-8 -*
"""
Created on Mon Dec  3 15:53:16 2018

@author: Nikhil.Pentapalli
"""

from wand.image import Image
from wand.color import Color


def pdf2png(pdf_name):
    
    file_name = []
    try:
        with Image(filename=pdf_name, resolution=300) as img:   
            img.compression_quality = 99
            images = img.sequence
            pages = len(images)
            for i in range(pages):
                  with Image(width=images[i].width, height=images[i].height, background=Color("white")) as bg:
                      bg.composite(images[i],0,0)
                      bg.save(filename=pdf_name+"-"+str(i)+'.png')
                  file_name.append(pdf_name+"-"+str(i)+'.png')
    except:
        file_name = []
        return (file_name , "Not Done")
    
    return (file_name, "Done")


#x=pdf2png("01032019054128_C_2927505_EPAY.pdf")
#print(x)