#当使用（from 包名 import 模块名） 导入包的方式时     使用__init__=["模块名"]
__all__= ["sendmsg"]


#  python2   当使用（import 包名） 导入包的方式时  __init__.py文件  使用 import 模块名

#import Testmsg 导入包
#import sendmsg  导入模块

#python3用下面方式导入模块   当使用（import 包名） 导入包的方式时 __init__.py 文件 使用 from . import 模块名

#import Testmsg

from . import sendmsg 


