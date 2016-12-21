import pandas as pd
import matplotlib.pyplot as plt

read_file = "catering_dish_profit.xls"
cdp_data = pd.read_excel(read_file,index_col = "菜品名")

print(cdp_data['盈利'])
