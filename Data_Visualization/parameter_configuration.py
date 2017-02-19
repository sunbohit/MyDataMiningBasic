import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 1, 0.01) #生成t数据列表

sinline = np.sin(2 * np.pi * t) #正弦函数
# 设置线的颜色为红色
plt.plot(t, sinline, color="red", linewidth=3)

cosline = np.cos(2 * np.pi * t)
#设置线的粗细为10
plt.rcParams['lines.linewidth'] = '10'
plt.plot(t,cosline)

# 错误的保存图片的做法
#plt.show()
#plt.savefig('parameter_configuration.png')

# 正确的保存图片的做法
# plt.savefig('parameter_configuration_1.png')
# plt.show()

# 正确的保存图片的做法_2
# gcf: Get Current Figure
fig = plt.gcf() # 句柄
plt.show()
fig.savefig('parameter_configuration_2.png')
