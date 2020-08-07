# Data Pirates Challenge
Autor: Sabrina Schütz

This script will scrap the page "http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm" and extract all locations and CEP ranges from all brazilian states.

## Steps to run:

Install Slenium using pip:
```
pip install selenium
```
Put the drivers directory to the path:
```
export PATH=$PATH:./drivers
```
Run the script:
```
python faixas-cep.py
```

Results will appear in the faixas-cep.jsol file ;)
