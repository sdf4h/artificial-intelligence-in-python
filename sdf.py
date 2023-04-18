from tkinter import *
def wer():
 root = Tk()
 root.title('Текстовый редактор')
 root.geometry('600x700')


 f_text = Frame(root)
 f_text.pack(fill=BOTH, expand=1)

 text_fild = Text(f_text,
                 bg='black',
                 fg='lime',
                 padx=10,
                 pady=10,
                 wrap=WORD,
                 insertbackground='brown',
                 selectbackground='#8D917A',
                 spacing3=10,
                 width=30
                 )
 text_fild.pack(expand=1, fill=BOTH, side=LEFT)

 scroll = Scrollbar(f_text, command=text_fild.yview)
 scroll.pack(side=LEFT, fill=Y)
 text_fild.config(yscrollcommand=scroll.set)

 root.mainloop()
import cv2
def ccc():
 image = cv2.imread("pic.jpg")
 cv2.imshow("Cat", image)
 cv2.waitKey(0)

 gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 cv2.imshow("black and white cat", gray_image)
 cv2.waitKey(0)

 inverted_image = 255 - gray_image
 cv2.imshow("negativity cat", inverted_image)
 cv2.waitKey()

 blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

 inverted_blurred = 255 - blurred

 pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
 cv2.imshow("sketch cat", pencil_sketch)
 cv2.imwrite('sketch cat.jpg', pencil_sketch)
 cv2.waitKey(0)