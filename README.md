# 北航自动化spoc课程网站作业提交脚本
## 简介
本脚本用于流程化在北航spoc网站上当助教的工作，节省工作中的重复性劳动，提高效率。

# 项目数据库设计
在所有脚本中都有 HOMEWORK_PATH 变量，用于指定每周的作业文件夹
例如 example_data\第一次作业

## 1.聚合作业
combineHomework.py
用于将  example_data\第一次作业\学生作业附件 中的作业重命名并合并到 example_data\第一次作业\批改后  example_data\第一次作业\批改前 文件夹中

参数:
工作路径
HOMEWORK_PATH = "D:\\Document\\Study\\研二上_电路助教\\buaa_spoc_automation\\data\\第一次作业"
第几次作业序列号
serial = "1"


## 2.手动批改作业
将 example_data\第一次作业\批改后 下的pdf文件进行作业批改，并在作业情况.xlsx 中撰写评语和作业评级

同时将典型易错题 放入 example_data\第一次作业\典型错误 文件夹中

手动将三个ABC3个评级的作业选择3份放入好、中、差 三个文件夹

作业评级分为A B C D N

A: 优秀

B: 良好

C: 较差

D: 驳回重做

N: 未提交

## 4.自动提交作业
commitResult.py

参数:
工作路径
HOMEWORK_PATH = "D:\\Document\\Study\\研二上_电路助教\\buaa_spoc_automation\\data\\第一次作业"
第几次作业序列号
serial = "1"

在commitREsult.py 同级目录中构建 password.py 文件
文件内容

class PW:
    def __init__(self) -> None:
        self.ID = 'zy2203203'
        self.password = '*******'

等等 

