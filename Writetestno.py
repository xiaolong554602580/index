'''
測試單號的數據庫
基於SPLITE3
'''

import os
import sqlite3
import json
import pandas as pd

def dbExist(db_file,*sql_Datas):
	try:
		conn = sqlite3.connect(db_file)#嘗試讀取文件，如果不在則創建
		c = conn.cursor()
		c.execute('create table if not exists testproject(TN text primary key,PJ,TR,AP,DR,RD,ID,DLSD,DLAD,SLSD,SLAD,Tester,MSSD,UD,RM)')
		#TN,PJ,TR,AP,DR,RD,ID,DLSD,DLAD,SLSD,SLAD,Tester,MSSD,UD,RM
		for dts in sql_Datas:
			for dt in dts:
				TN = dt[0]
				PJ= dt[1]
				TR= dt[2]
				AP= dt[3]
				DR= dt[4]
				RD= dt[5]
				ID= dt[6]
				DLSD= dt[7]
				DLAD= dt[8]
				SLSD= dt[9]
				SLAD= dt[10]
				Tester= dt[11]
				MSSD= dt[12]
				UD= dt[13]
				RM= dt[14]
				sql_text = (str(TN),
					str(PJ),
					str(TR),
					str(AP),
					str(DR),
					str(RD),
					str(ID),
					str(DLSD),
					str(DLAD),
					str(SLSD),
					str(SLAD),
					str(Tester),
					str(MSSD),
					str(UD),
					str(RM))
				c.execute('insert or ignore into testproject values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(sql_text))
				conn.commit()
		conn.close()
	except Exception as e:
		raise
	else:
		pass
	finally:
		pass


def dataProcessing():
	df = pd.read_excel("NTD測試報告查閱總表（1999~2014） .xlsx",sheet_name=None)
	#print(help(df))
	for i in df:
		#print(df[i].iterrows())
		for index,row in df[i].iterrows():
			print('{}-->'.format(index))
			print(row)
	'''
	sql_text = []
	for index,dt in df.iterrows():
		sql_text.append(dt)
		print("已寫入第{}條信息".format(index+1))
		
		TN = dt[0]
		PJ= dt[1]
		TR= dt[2]
		AP= dt[3]
		DR= dt[4]
		RD= dt[5]
		ID= dt[6]
		DLSD= dt[7]
		DLAD= dt[8]
		SLSD= dt[9]
		SLAD= dt[10]
		Tester= dt[11]
		MSSD= dt[12]
		UD= dt[13]
		RM= dt[14]
		print('{}{}'.format(TN,PJ))
		
	return sql_text
	'''

def dataWrite():
	pass

def config(config_f):
	try:
		f = open(config_f,"r",encoding="utf-8-sig")
		config_data = json.load(f)
	except Exception as e:
		print("config file in not exists")
		raise e

def main():
	#g = getData()
	#dbExist('1990-2014年測試單數據庫.db',g)
	dataProcessing()

main()