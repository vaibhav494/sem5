from PyPDF2 import PdfWriter, PdfReader
# page numbering starts from 0
start = 23 #start
end = 25 #end SHOULD BE ACTUAL PAGE NUMBER
infile = PdfReader('sem5_6_syllabus.pdf', strict=False) #name of input file
output = PdfWriter()

for i in range(start, end):
    p = infile.pages[i] 
    output.add_page(p)

with open('project_syllabus.pdf', 'wb') as f: #name of output file
    output.write(f)