data={1:'ram',2:'krishna',4:'teddy'}
data
data[4]
data.get(1)
data.get(3)
print(data.get(3))# As there is no data or value with index 3,it gives none
data.get(1,'Not found')#because have the value as ram for index 1
data.get(3,'fill me')
keys=['leela','preethi','niharika']
values=['Python','Java','JS']
data = dict(zip(keys,values)) # data is a dictionary of keys and values
data
data['leela']
data['monica'] ='cs'
data['monica']
prog={'JS':'Atom','CS':'VS','Python':['Pycharm','Sublime'],'Java':{'JSE':'Netbeans','JEE':'Eclipse'}}
prog
prog['JS']
prog['CS']
prog['Python']
prog['Python'][1]
prog['Java']
prog['Java']['JEE']
prog['Java']['JSE']
