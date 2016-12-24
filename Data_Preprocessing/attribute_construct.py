import pandas as pd

input_file = 'electricity_data.xls'
ed_data = pd.read(input_file)

ed_data['线损率'] = (ed_data['供入电量']-ed_data['供出电量'])/ed_data['供入电量']
