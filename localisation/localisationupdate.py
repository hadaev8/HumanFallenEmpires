# coding: utf-8
import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('localisationupdate.json', scope)
gc = gspread.authorize(credentials)
sh = gc.open_by_key('1wrlW6mMMhEI_EPnSCPDSih1gvnDreK4qV4vyHt0WHK4').get_worksheet(0)

loc_keys = sh.col_values(1)
loc_rows = sh.row_values(1)
loc_indexes = [loc_rows.index(i) for i in loc_rows if i.startswith('l_')]
eng_fallback = sh.col_values(1+loc_rows.index('l_english:'))
for loc_index in loc_indexes:
    loc = sh.col_values(1+loc_index)
    out_file = 'human_fallen_empires_' + loc_rows[loc_index].replace(':', '') + '.yml'
    if os.path.exists(out_file):
        os.remove(out_file)
    with open(out_file, 'a', encoding='utf-8') as f:
        f.write(u'\uFEFF')
        f.write(loc_rows[loc_index] + '\n')
        for i, j in enumerate(loc):
            if loc_keys[i] != '':
                if loc_keys[i].startswith('#'):
                    f.write(' ' + loc_keys[i] + '\n')
                elif loc[i] == '':
                    f.write(' {0}:0 "{1}"\n'.format(loc_keys[i], eng_fallback[i]))
                elif eng_fallback[i] == '':
                    f.write(' {0}:0 "{1}"\n'.format(loc_keys[i], ' '))
                else:
                    f.write(' {0}:0 "{1}"\n'.format(loc_keys[i], loc[i]))