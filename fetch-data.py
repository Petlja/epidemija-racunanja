import requests 

# European Centre for Disease Prevention and Control 
# COVID-19 cases worldwide 
r = requests.get('https://opendata.ecdc.europa.eu/covid19/casedistribution/csv')
open('data/covid-worldwide.csv', 'wb').write(r.content)