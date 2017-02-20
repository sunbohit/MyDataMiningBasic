'''
从json文件中读取数据
'''
import requests

url = 'https://github.com/timeline.json' #github网站最近活动时间表

r = requests.get(url) #用requests通过url获取json文件,r为Response对象
json_obj = r.json() #转化为json格式的对象

repos = set() 
for entry in json_obj:
    try:
        repos.add(entry['repository']['url']) #json相当于python中的“字典的字典”
    except KeyError as e:
        print("No key %s. Skipping..." % (e))

from pprint import pprint 
pprint(repos) #输出收集到的url
