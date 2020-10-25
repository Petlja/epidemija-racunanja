#%%
import requests 

#%%
# European Centre for Disease Prevention and Control 
# COVID-19 cases worldwide 
r = requests.get('https://opendata.ecdc.europa.eu/covid19/casedistribution/csv')
open('data/covid-worldwide.csv', 'wb').write(r.content)

#%%
# Подаци са covid19.rs. Извор: Институт за јавно здравље Србије ”Милан Јовановић Батут”, СЗО.
r = requests.get('https://covid19.data.gov.rs/api/datasets/statistic/official')
open('data/serbia-offitial.json', 'wb').write(r.content)

