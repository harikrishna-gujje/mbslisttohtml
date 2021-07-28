# import PyPDF2
# import requests
# from bs4 import BeautifulSoup
import pdftotree

# from io import StringIO
# from pdfminer.layout import LAParams
# from pdfminer.high_level import extract_text_to_fp


if __name__ == '__main__':
    try :

        # output_string = StringIO()
        #
        # with open('mbslist.pdf', 'rb') as fn:
        #     extract_text_to_fp(fn, output_string, laparams=LAParams(), output_type='html', codec=None)






        # url = 'https://www.treasury.gov/ofac/downloads/mbs/mbslist.pdf'
        # response = requests.get(url)
        # print(response.text)
        # content = BeautifulSoup(response, 'pdf')



        ht = pdftotree.parse('./mbslist.pdf', './index3.html')
        print(ht)



        # with open('msblist.pdf','rb') as file:
        #     reader = PyPDF2.PdfFileReader(file)
        #     print(reader.documentInfo)
        #     for page in range(reader.getNumPages()):
        #         print(reader.getPage(pageNumber=page).extractText())
    except Exception as e:
        print(f'Error is {e}')