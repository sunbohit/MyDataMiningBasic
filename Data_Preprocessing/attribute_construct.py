'''
属性构造
'''

import pandas as pd

input_file = 'electricity_data.xls' #数据集
output_file = 'electricity_data_after.xls' #输出路径
ed_data = pd.read_excel(input_file)

ed_data['线损率'] = (ed_data['供入电量']-ed_data['供出电量'])/ed_data['供入电量']

ed_data.to_excel(output_file,index=False) #pandas生成excel
