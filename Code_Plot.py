import pandas as pd
import re
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
#from bokeh.plotting import figure, output_file, show
houses = pd.read_csv("out_4.1.csv",index_col=0)
houses.sort_values('具体日期',inplace=True)
houses = houses.iloc[1:]
print(re.search(r"(\d+-\d+)(-\d+)", houses['具体日期'][40]).group(1))

#houses['具体日期'] = houses.apply(lambda x: re.search(r"(\d+-\d+)(-\d+)", x['具体日期']).group(1),axis=1)
#houses.price = houses.price.where(houses.price < 20000)
#houses['具体日期'] = houses.apply(lambda x: re.search(r"(\d+-\d+)(-\d+)", x['具体日期']).group(1),axis=1)
#houses['具体日期'] = houses['具体日期'].mask(houses['具体日期'].duplicated())
#plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(50))


plt.figure(0,figsize=(10,10))
houses["租金1"] = houses["租金"].loc[houses['电视'] == '有']
houses["租金2"] = houses["租金"].loc[houses['电视'] == '无']
x = range(1,340,34)
plt.scatter(houses['具体日期'],houses['租金1'],s=3,color='red', label='With Television')
plt.scatter(houses['具体日期'],houses['租金2'],s=3,color='blue', label='Without Television')
plt.xticks(x,('2018-01','2018-03','2018-05','2018-07','2018-09','2018-11','2019-01','2019-03','2019-05','2019-07'),rotation=30,ha='right')
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Rent of Apartment")
plt.legend(loc='upper right')
#plt.savefig('./house_img/figure0.png')
##plt.show()

plt.figure(1,figsize=(10,10))
houses["租金1"] = houses["租金"].loc[houses['冰箱'] == '有']
houses["租金2"] = houses["租金"].loc[houses['冰箱'] == '无']
x = range(1,340,34)
plt.scatter(houses['具体日期'],houses['租金1'],s=3,color='red', label='With Refrigerator')
plt.scatter(houses['具体日期'],houses['租金2'],s=3,color='blue', label='Without Refrigerator')
plt.xticks(x,('2018-01','2018-03','2018-05','2018-07','2018-09','2018-11','2019-01','2019-03','2019-05','2019-07'),rotation=30,ha='right')
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Rent of Apartment")
plt.legend(loc='upper right')
#plt.savefig('./house_img/figure1.png')
#plt.show()

plt.figure(2,figsize=(10,10))
houses["租金1"] = houses["租金"].loc[houses['洗衣机'] == '有']
houses["租金2"] = houses["租金"].loc[houses['洗衣机'] == '无']
x = range(1,340,34)
plt.scatter(houses['具体日期'],houses['租金1'],s=3,color='red', label='With Washing Machine')
plt.scatter(houses['具体日期'],houses['租金2'],s=3,color='blue', label='Without Washing Machine')
plt.xticks(x,('2018-01','2018-03','2018-05','2018-07','2018-09','2018-11','2019-01','2019-03','2019-05','2019-07'),rotation=30,ha='right')
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Rent of Apartment")
plt.legend(loc='upper right')
#plt.savefig('./house_img/figure2.png')
#plt.show()

plt.figure(3,figsize=(10,10))
houses["租金1"] = houses["租金"].loc[houses['空调'] == '有']
houses["租金2"] = houses["租金"].loc[houses['空调'] == '无']
plt.scatter(houses['具体日期'],houses['租金1'],s=3,color='red', label='With Air Conditioner')
plt.scatter(houses['具体日期'],houses['租金2'],s=3,color='blue', label='Without Air Conditioner')
plt.xticks(x,('2018-01','2018-03','2018-05','2018-07','2018-09','2018-11','2019-01','2019-03','2019-05','2019-07'),rotation=30,ha='right')
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Rent of Apartment")
plt.legend(loc='upper right')
#plt.savefig('./house_img/figure3.png')
#plt.show()

plt.figure(4,figsize=(10,10))
houses["租金1"] = houses["租金"].loc[houses['热水器'] == '有']
houses["租金2"] = houses["租金"].loc[houses['热水器'] == '无']
x = range(1,340,34)
plt.scatter(houses['具体日期'],houses['租金1'],s=3,color='red', label='With Water Heater')
plt.scatter(houses['具体日期'],houses['租金2'],s=3,color='blue', label='Without Water Heater')
plt.xticks(x,('2018-01','2018-03','2018-05','2018-07','2018-09','2018-11','2019-01','2019-03','2019-05','2019-07'),rotation=30,ha='right')
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Rent of Apartment")
plt.legend(loc='upper right')
#plt.savefig('./house_img/figure4.png')
#plt.show()

plt.figure(5,figsize=(10,10))
houses["租金1"] = houses["租金"].loc[houses['床'] == '有']
houses["租金2"] = houses["租金"].loc[houses['床'] == '无']
x = range(1,340,34)
plt.scatter(houses['具体日期'],houses['租金1'],s=3,color='red', label='With Bed')
plt.scatter(houses['具体日期'],houses['租金2'],s=3,color='blue', label='Without Bed')
plt.xticks(x,('2018-01','2018-03','2018-05','2018-07','2018-09','2018-11','2019-01','2019-03','2019-05','2019-07'),rotation=30,ha='right')
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Rent of Apartment")
plt.legend(loc='upper right')
#plt.savefig('./house_img/figure5.png')
#plt.show()

plt.figure(6,figsize=(10,10))
houses["租金1"] = houses["租金"].loc[houses['暖气'] == '有']
houses["租金2"] = houses["租金"].loc[houses['暖气'] == '无']
x = range(1,340,34)
plt.scatter(houses['具体日期'],houses['租金1'],s=3,color='red', label='With Heating')
plt.scatter(houses['具体日期'],houses['租金2'],s=3,color='blue', label='Without Heating')
plt.xticks(x,('2018-01','2018-03','2018-05','2018-07','2018-09','2018-11','2019-01','2019-03','2019-05','2019-07'),rotation=30,ha='right')
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Rent of Apartment")
plt.legend(loc='upper right')
#plt.savefig('./house_img/figure6.png')
#plt.show()

plt.figure(7,figsize=(10,10))
houses["租金1"] = houses["租金"].loc[houses['宽带'] == '有']
houses["租金2"] = houses["租金"].loc[houses['宽带'] == '无']
x = range(1,340,34)
plt.scatter(houses['具体日期'],houses['租金1'],s=3,color='red', label='With Wifi')
plt.scatter(houses['具体日期'],houses['租金2'],s=3,color='blue', label='Without Wifi')
plt.xticks(x,('2018-01','2018-03','2018-05','2018-07','2018-09','2018-11','2019-01','2019-03','2019-05','2019-07'),rotation=30,ha='right')
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Rent of Apartment")
plt.legend(loc='upper right')
#plt.savefig('./house_img/figure7.png')
#plt.show()

plt.figure(8,figsize=(10,10))
houses["租金1"] = houses["租金"].loc[houses['衣柜'] == '有']
houses["租金2"] = houses["租金"].loc[houses['衣柜'] == '无']
x = range(1,340,34)
plt.scatter(houses['具体日期'],houses['租金1'],s=3,color='red', label='With Wardrobe')
plt.scatter(houses['具体日期'],houses['租金2'],s=3,color='blue', label='Without Wardrobe')
plt.xticks(x,('2018-01','2018-03','2018-05','2018-07','2018-09','2018-11','2019-01','2019-03','2019-05','2019-07'),rotation=30,ha='right')
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Rent of Apartment")
plt.legend(loc='upper right')
#plt.savefig('./house_img/figure8.png')
#plt.show()

plt.figure(9,figsize=(10,10))
houses["租金1"] = houses["租金"].loc[houses['天然气'] == '有']
houses["租金2"] = houses["租金"].loc[houses['天然气'] == '无']
x = range(1,340,34)
plt.scatter(houses['具体日期'],houses['租金1'],s=3,color='red', label='With Natural Gas')
plt.scatter(houses['具体日期'],houses['租金2'],s=3,color='blue', label='Without Natural Gas')
plt.xticks(x,('2018-01','2018-03','2018-05','2018-07','2018-09','2018-11','2019-01','2019-03','2019-05','2019-07'),rotation=30,ha='right')
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Rent of Apartment")
plt.legend(loc='upper right')
#plt.savefig('./house_img/figure9.png')
##plt.show()

plt.figure(10,figsize=(10,10))
x = range(1,340,34)
plt.scatter(houses['具体日期'],houses['租金'],s=3,color='red', label='With Natural Gas')
plt.xticks(x,('2018-01','2018-03','2018-05','2018-07','2018-09','2018-11','2019-01','2019-03','2019-05','2019-07'),rotation=30,ha='right')
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Rent of Apartment")
#plt.savefig('./house_img/figure10.png')
##plt.show()

plt.figure(11,figsize=(10,10))
houses["租金1"] = houses["租金"].loc[houses['距离地铁站距离'] == houses['距离地铁站距离']]
houses["租金2"] = houses["租金"].loc[houses['距离地铁站距离'] != houses['距离地铁站距离']]
x = range(1,340,34)
plt.scatter(houses['具体日期'],houses['租金1'],s=3,color='red', label='With Station Nearby')
plt.scatter(houses['具体日期'],houses['租金2'],s=3,color='blue', label='Without Station Nearby')
plt.xticks(x,('2018-01','2018-03','2018-05','2018-07','2018-09','2018-11','2019-01','2019-03','2019-05','2019-07'),rotation=30,ha='right')
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Rent of Apartment")
plt.legend(loc='upper right')
plt.savefig('./house_img/figure_subway.png')
plt.show()


plt.figure(10,figsize=(10,10))
x = range(1,180,18)
houses.sort_values('面积',inplace=True)
plt.scatter(houses['面积'],houses['租金'],s=3,color='red', label='With Natural Gas')
plt.xticks(x,('10','60','90','120','150','180','210','240','270','310'),rotation=30,ha='right')
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Rent of Apartment")
plt.savefig('./house_img/figure_area.png')
plt.show()

plt.figure(11,figsize=(10,10))
houses["租金1"] = houses["租金"].loc[houses['距离地铁站距离'] == houses['距离地铁站距离']]
houses["租金2"] = houses["租金"].loc[houses['距离地铁站距离'] != houses['距离地铁站距离']]
x = range(1,340,34)
plt.scatter(houses['具体日期'],houses['租金1'],s=3,color='red', label='With Station Nearby')
plt.scatter(houses['具体日期'],houses['租金2'],s=3,color='blue', label='Without Station Nearby')
plt.xticks(x,('2018-01','2018-03','2018-05','2018-07','2018-09','2018-11','2019-01','2019-03','2019-05','2019-07'),rotation=30,ha='right')
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Rent of Apartment")
plt.legend(loc='upper right')
plt.savefig('./house_img/figure11.png')