'''
①数据加载和概览：加载CSV，输出行数、列数、每列数据类型

②空值检查：输出每列有多少空值

③描述统计分析：对数值列输出均值、最大值、最小值等

④分组分析：按性别分组统计存活率、按船舱等级分组统计存活率

⑤年龄段分析：把乘客分成儿童（0-18）、成人（19-60）、老人（60+）三组，统计每组存活率

⑥结果导出：把分组统计结果导出为一个新的CSV文件
'''
import pandas as pd
#加载CSV
df = pd.read_csv("train.csv")

#输出行数、列数
print(df.shape)

#输出每列数据类型
print(df.dtypes)

#输出每列有多少空值
print(df.isna().sum())

#对数值列输出均值、最大值、最小值
print(df.describe().to_string())

#按性别分组统计存活率
group_sex = df.groupby("Sex")
print(group_sex["Survived"].mean())

#按船舱等级分组统计存活率
group_level = df.groupby("Pclass")
print(group_level["Survived"].mean())

#把乘客分成儿童（0-18）、成人（19-60）、老人（60+）三组，统计每组存活率
#定义切割点0-18,18-60,60-100
bins = [0,18,60,100]
labels = ["儿童（0-18）","成人（19-60）","老人（60+）"]
df["agegroup"] = pd.cut(df["Age"],bins=bins,labels=labels)
group_age = df.groupby("agegroup")
print(group_age["Survived"].mean())


#导出csv
df.to_csv("output.csv")












































