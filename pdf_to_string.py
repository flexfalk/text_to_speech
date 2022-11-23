import PyPDF2


# class pdf to string
#

# import PyPDF2
#
# # create file object variable
# # opening method will be rb
# pdffileobj = open('some_book.pdf', 'rb')
#
# # create reader variable that will read the pdffileobj
# pdfreader = PyPDF2.PdfFileReader(pdffileobj)
#
# # This will store the number of pages of this pdf file
# # x = pdfreader.numPages
# x = 1
#
# print(x)
# # create a variable that will select the selected number of pages
# pageobj = pdfreader.getPage(x)
#
# # (x+1) because python indentation starts with 0.
# # create text variable which will store all text datafrom pdf file
# text = pageobj.extractText()
#
# # save the extracted data from pdf to a txt file
# # we will use file handling here
# # dont forget to put r before you put the file path
# # go to the file location copy the path by right clicking on the file
# # click properties and copy the location path and paste it here.
# # put "\\your_txtfilename"
# file1 = open(r"some_book.pdf", "a")
# file1.writelines(text)

import PyPDF2
pdfFileObject = open('some_book.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
# count = pdfReader.numPages
output = ""
count = 3
start_page = 67
end_page = 67

pages_to_read = [(i + start_page) for i in range(end_page- start_page + 1)]
print(pages_to_read)
for page_num in pages_to_read:
    page = pdfReader.getPage(page_num)
    output += page.extractText()





file1 = open("somefile.txt", "w", encoding="utf-16")
file1.writelines(output)
