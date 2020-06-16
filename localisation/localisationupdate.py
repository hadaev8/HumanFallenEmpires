# update localisation
# coding: utf-8
import gspread
import os
from google.oauth2.service_account import Credentials
from oauth2client.service_account import ServiceAccountCredentials
import re
import numpy as np

mod_prefix = 'hfe_'

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('..\\..\\localisationupdate.json', scope)
gc = gspread.authorize(credentials)
sht = gc.open_by_key('1wrlW6mMMhEI_EPnSCPDSih1gvnDreK4qV4vyHt0WHK4')
worksheets = sht.worksheets()

localisations = []
texts = {}
for worksheet in worksheets:
    sh = sht.worksheet(re.search("'.*'", str(worksheet)).group().replace("'", ''))
    sh_all_values = np.array(sh.get_all_values()).transpose()
    for collumn in sh_all_values:
        if collumn[0].startswith('l_') or '# loc keys' in collumn[0]:
            if collumn[0].startswith('l_'):
                localisations.append(collumn[0])
            if collumn[0] in texts:
                texts[collumn[0]] = np.concatenate([np.array(texts[collumn[0]]), collumn[1:]])
            else:
                texts[collumn[0]] = collumn[1:]

loc_keys = texts['# loc keys']
for localisation in set(localisations):
    out_file = mod_prefix + localisation.replace(':', '') + '.yml'
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(u'\uFEFF' + localisation + '\n')
        for i, j in enumerate(texts[localisation]):
            if loc_keys[i] != '':
                if loc_keys[i].startswith('#'):
                    f.write(' ' + loc_keys[i] + '\n')
                elif j != '':
                    f.write(' {0}:0 "{1}"\n'.format(loc_keys[i], j))
                else:
                    f.write(' {0}:0 "{1}"\n'.format(loc_keys[i], texts['l_english:'][i]))