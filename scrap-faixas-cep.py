from urllib import urlopen
from bs4 import BeautifulSoup

try:
    html = urlopen("http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm")
except HTTPError as httpError:
    print(httpError)
except URLError as urlError:
    print(urlError)
else:
    page = BeautifulSoup(html.read(), "html5lib")

    option = page.find('option', {'value':"SC"})
    option['selected'] = True

    selectedOp = page.find('option',  {'selected': True})

    submitBtn = page.find('div', {'class': 'btnform'}).find('input')

    if submitBtn is None:
        print("Button not found")
    else:        
        submitBtn.click()

        if page.title is None:
            print("Not found")
        else:
            print(page.title)