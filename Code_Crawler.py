import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import json
url0  = 'http://sh.lianjia.com/zufang/pg{}'
houses = pd.DataFrame(columns = ('地址','区域','小区','租凭方式','租金','楼层','面积','户型','朝向','发布日期','具体日期','介绍','看房记录（最新成交日期）','看房记录（最新成交价格）','距离地铁站距离',"入住","租期","看房","电梯","车位","用水","用电","燃气","电视","冰箱","洗衣机","空调","热水器","床","暖气","宽带","衣柜","天然气",'经度','纬度','链接','信息采集时间'))

def earth(location, disctrict, community, latorlng):
	url = 'https://restapi.amap.com/v3/geocode/geo'  
	address1 = location + disctrict + community
	params = { 'key': '53d61289f8a31ae9978b马赛克', 
	           'address': address1,
	           'city': 'shanghai'}   
	res = requests.get(url, params)
	jd =  json.loads(res.text)
	if (jd['geocodes'] != []):
		result = jd['geocodes'][0]['location'].split(',', 1)[0] if latorlng == 'lng' else jd['geocodes'][0]['location'].split(',', 1)[1]
	else:
		address1 = location + community
		res = requests.get(url, params)
		jd =  json.loads(res.text)
		if (jd['geocodes'] != []):
			result = jd['geocodes'][0]['location'].split(',', 1)[0] if latorlng == 'lng' else jd['geocodes'][0]['location'].split(',', 1)[1]
		else:
			address1 = community
			res = requests.get(url, params)
			jd =  json.loads(res.text)
			if (jd['geocodes'] != []):
				result = jd['geocodes'][0]['location'].split(',', 1)[0] if latorlng == 'lng' else jd['geocodes'][0]['location'].split(',', 1)[1]
			else: 
				result = ""
	print(result)
	return result

for pages in range(1,101):
	url = url0.format(pages)
	print("开始解析大页"+url)
	#url = 'http://sh.lianjia.com/zufang/pg1'
	header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}
	page = requests.get(url, headers = header)
	soup = BeautifulSoup(page.text, "lxml")
	for house in soup.find_all('div', class_='content__list--item'):
		my_dict = {}
		des = house.find(class_="content__list--item--des").find_all('a')
		location = des[0].get_text() #地址
		disctrict = des[1].get_text() #区域	
		info = house.find(class_="content__list--item--des").find_all('i')
		post = house.find(class_="content__list--item--time oneline").get_text().strip('发布') #发布日期
		link = house.find(class_="content__list--item--title twoline").a.get('href') #链接
		link = "https://sh.lianjia.com" + link
		title = house.find(class_="content__list--item--title twoline").a.get_text()
		community = re.findall(r"·(.+?) ",title)[0] #小区
		print("我开始解析 " + link + "辣！！！")
		#开始爬详情页
		requests.packages.urllib3.disable_warnings()
		page_detail = requests.get(link, headers=header, verify = False)
		#page_detail = requests.get("https://sh.lianjia.com/zufang/SH2308551380148953088.html", headers=header)
		soup_detail = BeautifulSoup(page_detail.text, "lxml")
		try:
			four = soup_detail.find(class_="content__article__table").find_all('span')
		except AttributeError:
			continue
		way = four[0].get_text() #租凭方式
		type_ = four[1].get_text() #户型
		area = four[2].get_text() #面积
		direction = four[3].get_text() #朝向
		price = soup_detail.find(class_="content__aside--title").span.get_text() #租金
		datetext = soup_detail.find(class_="content__subtitle").get_text()
		accdate = re.findall(r"\d+-\d+-\d+", datetext)[0] #具体日期
		ten = soup_detail.find(class_="content__article__info").ul.find_all('li')
		live = ten[2].get_text() #入住
		live = re.sub('.*：', "", live)
		period = ten[4].get_text() #租期
		period = re.sub('.*：', "", period)
		visit = ten[5].get_text() #看房
		visit = re.sub('.*：', "", visit)
		floor = ten[7].get_text() #楼层
		floor = re.sub('.*：', "", floor)
		lift = ten[8].get_text() #电梯
		lift = re.sub('.*：', "", lift)
		garage = ten[10].get_text() #车位
		garage = re.sub('.*：', "", garage)
		pump = ten[11].get_text() #用水
		pump = re.sub('.*：', "", pump)
		electricity = ten[13].get_text() #用电
		electricity = re.sub('.*：', "", electricity)
		fuel = ten[14].get_text() #燃气
		fuel = re.sub('.*：', "", fuel)
		have = soup_detail.find(class_="content__article__info2")
		television = "有" if have.find(class_="fl oneline television_no ") == None else "无"#电视
		refrigerator = "有" if have.find(class_="fl oneline refrigerator_no ") == None else "无" #冰箱
		washing_machine = "有" if have.find(class_="fl oneline washing_machine_no ") == None else "无" #洗衣机
		air_conditioner = "有" if have.find(class_="fl oneline air_conditioner_no ") == None else "无" #空调
		water_heater = "有" if have.find(class_="fl oneline water_heater_no ") == None else "无" #热水器
		bed = "有" if have.find(class_="fl oneline bed_no ") == None else "无" #床
		heating = "有" if have.find(class_="fl oneline heating_no ") == None else "无" #暖气
		wifi = "有" if have.find(class_="fl oneline wifi_no ") == None else "无" #宽带
		wardrobe = "有" if have.find(class_="fl oneline wardrobe_no ") == None else "无" #衣柜
		natural_gas = "有" if have.find(class_="fl oneline natural_gas_no ") == None else "无" #天然气
		try:
			intro = soup_detail.find('p', class_="threeline").get('data-desc').replace('<br />','') #介绍
		except AttributeError:
			intro = ""
		try:
			transportation = soup_detail.find(class_="content__article__info4").ul.li.find_all('span')
		except AttributeError:
			distance = ""
		else:
			distance = transportation[1].get_text() #距离地铁距离
		try:
			log = soup_detail.find(class_="content__table").find_all('div', class_ = "tr")
			lastest = log[1].find_all('div')
		except AttributeError:
			logdate = ""
			logprice = ""
		else:
			logdate = lastest[0].get_text() #小区最新成交日期
			logprice = lastest[4].get_text() #小区最新成交价格
		lng = earth(location, disctrict, community, 'lng') #经度
		lat = earth(location, disctrict, community, 'lat') #纬度
		time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		houses = houses.append([{'地址':location,
								 '区域':disctrict,
								 '小区':community,
								 '租凭方式':way,
								 '租金':price,
								 '楼层':floor,
								 '面积':area,
								 '户型':type_,
								 '朝向':direction,
								 '发布日期':post,
								 '具体日期':accdate,
								 '介绍':intro,
								 '看房记录（最新成交日期）':logdate,
								 '看房记录（最新成交价格）':logprice,
								 '距离地铁站距离':distance,
								 "入住":live,
								 "租期":period,
								 "看房":visit,
								 "电梯":lift,
								 "车位":garage,
								 "用水":pump,
								 "用电":electricity,
								 "燃气":fuel,
								 "电视":television,
								 "冰箱":refrigerator,
								 "洗衣机":washing_machine,
								 "空调":air_conditioner,
								 "热水器":water_heater,
								 "床":bed,
								 "暖气":heating,
								 "宽带":wifi,
								 "衣柜":wardrobe,
								 "天然气":natural_gas,
								 "经度":lng,
								 "纬度":lat,
								 '链接':link,
								 '信息采集时间':time}], ignore_index=True)
		houses.to_csv('out_4.1.csv',encoding='utf-8-sig')

	






	


	#print(des[0].get_text())
	#for box in soup.find_all('p', class_='content__list--item--title' )
	#print(house.a.get('href'))
	