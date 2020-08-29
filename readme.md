安装所需库（那啥，所用都是python自带的库，so这一步不用了。。）
```
pip install  -r requirements.txt
```

根目录下创建`default.ini`

```
[bark]
bark-url = XXXX(Bark软件中对应url)
```

运行

```
 python -m BarkMessage -s 推送内容
```

可能会出现找不到包的情况

```
修改__main__.py中的路径为 BarkMessage文件夹的上一级
# 确认当前所在目录 应该在BarkMessage的上一级
import os
if 'BarkMessage' in os.getcwd():
    os.chdir('D:/PyCharm 2020.1.2/workspace')
print(os.getcwd())
```

