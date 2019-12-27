import pandas as pd
import re
houses = pd.read_csv("out_4.1.csv",index_col=0)
def distance(org):
	strdis = str(org)
	if (strdis == "nan"):
		return None
	else:
		return int(strdis.replace('m',''))
#houses['发布日期'] = houses.apply(lambda x: date(x['发布日期']),axis=1) #将日期数据转为数值
houses['subway'] = houses.apply(lambda x: 0 if(str(x['距离地铁站距离']) == "nan") else 1 ,axis=1) #判断附近是否有地铁站
houses['距离地铁站距离'] = houses.apply(lambda x: distance(x['距离地铁站距离']),axis=1) 
houses['面积'] = houses.apply(lambda x: int(x['面积'].replace('㎡','')),axis=1) #将面积数据转为数值
houses['楼层'] = houses.apply(lambda x: re.findall(r"\d+",x['楼层'])[0],axis=1)
houses = houses.replace({"有": 1, "无": 0}) #将有、无转化为虚拟变量
#除去暂时作用不大的数据：
houses = houses.drop(columns=['地址','区域','小区','租凭方式','户型','朝向','介绍','看房记录（最新成交日期）','看房记录（最新成交价格）', '入住', '租期', '看房', '电梯', '车位', '用水', '用电', '燃气', '链接', '信息采集时间','发布日期','经度','纬度'])
#将列名改为英文方便EViews读取：
houses.rename(columns={'租金': 'price', '楼层': 'floor', '面积': 'area', '具体日期': 'post',  '距离地铁站距离':'subway_distance', '电视':'television','冰箱':'refrigerator','洗衣机':'washing_machine','空调':'air_conditioner','热水器':'water_heater','床':'bed','暖气':'heating','宽带':'wifi','衣柜':'wardrobe','天然气':'natural_gas'}, inplace=True) 
houses.to_csv('out_neat2.1.csv',encoding='utf-8-sig')
