import os
import sys
sys.path.insert(0, "/app")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "civiccomments.settings")
import django
django.setup()
import civiccomments
from seattle_buildings.models import SeattleLandUsePermitDoc

def get_html_of_documents_list(id):
    import requests

    cookies = {
        'BIGipServerpool_dmz_web6-http': '435988672.20480.0000',
        '_ga': 'GA1.2.770110884.1538104262',
        '_gid': 'GA1.2.1052752342.1538104262',
    }

    headers = {
        'Origin': 'http://web6.seattle.gov',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Cache-Control': 'max-age=0',
        'Referer': 'http://web6.seattle.gov/dpd/edms/',
        'Connection': 'keep-alive',
    }

    data = {
      '__EVENTTARGET': '',
      '__EVENTARGUMENT': '',
      '__VIEWSTATE': '3m7OoS1V9kD8su3vrvrUe0PBa/kp4douegHL3H2hNTap/4o5ovaHEH7lXvOTNWgJmqpgBJ3P99Xg1Aj9jWjGcvC/gQ7b5ZJpxOo/xWveRGckBIzXd/qMPABMHu0=',
      '__VIEWSTATEGENERATOR': '08477B0D',
      '__EVENTVALIDATION': '5Y0tGjpSYYYvQDkUrjnuUbI3jOwaHAbrIwSzSco+gR7rhZFuGMQrq+QkqPTGqNUxVQaREX1R0YAU6/7YdV6GwJHxKsohc6JrzBAwx9MnA+lvzdqNiyFnZbYvxbvt3jR9+NyIoWuHMS23gVW+IkgaCH/956umJMzfVaOwF79ClwE2HbV0pB94HH5hkW2gSWRQErtY38toFXobLvx0gnmY/FtPqib5DDlNWjaAYRQsMomKUuIOJMjvoHAQJiAQkBWiRjrAhG7DBcNUFjI/yKybEKdOWZ3WM61LBBigpDmxo/1nDsmMkOkK8fijlIQBg9dMbUfIXfa4PPhAThPlLtLZ+ONN3CoYCwNWto/eMQ51P8wxmLt3QhPkKR8V3Mo=',
      'q': '',
      'ctl00$cph$txtRef': id,
      'ctl00$cph$btnSearchRef': 'Go',
      'txtAddressSearch': '',
      'ctl00$cph$ucAddress$hAddrkey': '',
      'ctl00$cph$ucAddress$hStreetNum': '',
      'ctl00$cph$ucAddress$hStreetMod': '',
      'ctl00$cph$ucAddress$hPrefix': '',
      'ctl00$cph$ucAddress$hStreetName': '',
      'ctl00$cph$ucAddress$hStreetType': '',
      'ctl00$cph$ucAddress$hSuffix': '',
      'ctl00$cph$hLastSearchType': 'Ref',
      'ctl00$cph$hLastSearchVal': '6631682-CN'
    }

    response = requests.post('http://web6.seattle.gov/dpd/edms/', headers=headers, cookies=cookies, data=data)
    return response.text

def get_list_of_documents(id):
    html_doc = get_html_of_documents_list(id)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_doc, 'html.parser')
    html_rows = soup.find('tbody').find_all('tr')
    rows = []
    for html_row in html_rows:
        print 'row'
        columns = {}
        html_columns = html_row.find_all('td')
        for i, html_column in enumerate(html_columns):
            if i == 0:
                columns['name'] = html_column.find('a').contents[0].strip()
                columns['url'] = 'http://web6.seattle.gov/dpd/edms/' + html_column.find('a')['href']
                columns['id'] = html_column.find('a')['href'][len('GetDocument.aspx?id='):]
            if i == 2:
                columns['date'] = html_column.text
            if i == 3:
                columns['record_number'] = html_column.find('a').contents[0].strip()
            if i == 4:
                columns['record_type'] = html_column.text
        download_building_document(columns['id'])
        try:
            columns['text'] = pdf2txt('/tmp/%s.pdf' % (columns['id']))
        except:
            columns['text'] = ''
        rows.append(columns)
        import os
        os.system('rm /tmp/%s.pdf' % (columns['id']))
    return rows

def download_building_document(id):
    import urllib2
    download_url = "http://web6.seattle.gov/dpd/edms/GetDocument.aspx?id=%s" % (id)
    response = urllib2.urlopen(download_url)
    file = open("/tmp/%s.pdf" % (id), 'w')
    file.write(response.read())
    file.close()

def pdf2txt(fname, pages=None):
    # http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/Using%20Python%20to%20Convert%20PDFs%20to%20Text%20Files.php#4
    from cStringIO import StringIO
    from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
    from pdfminer.converter import TextConverter
    from pdfminer.layout import LAParams
    from pdfminer.pdfpage import PDFPage
    import os
    import sys, getopt

    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text.strip()

get_list_of_documents('3030517-LU')
