from mymodule import stats_word
import json
#路径前+r，避免转义。
with open(r'C:\Users\CS-Mu\Documents\selfteaching-python-camp\exercises\1901010061\d09\tang300.json',encoding='UTF-8') as f: 
    read_date = f.read()
try:
    print('统计汉字字频最高的前100个字： \n',stats_word.stats_text_cn(read_date,100))
except ValueError as e:
    print(e) 
