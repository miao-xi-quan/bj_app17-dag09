import yaml

with open("./value2",'r',encoding="utf-8")as f:
    # 加载yaml文件
    data = yaml.safe_load(f)
    # 打印数据
    print("data:{}".format(data))
    # 打印类型
    # print("类型:{}".format(type(data.get("value12"))))
    print("类型:{}".format(type(data.get("info"))))