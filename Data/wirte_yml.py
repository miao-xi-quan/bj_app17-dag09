import yaml

data = {'aeb':{
        'sea1':{'ex':{'value':"全哥"},'value':'帅哥'},
        'sea2':{'ex':[1,2,3],'value':456}}}

with open('./ww.yml','a',encoding='utf-8')as f:
    yaml.safe_dump(data,f,encoding='utf-8',allow_unicode=True)