import pandas as pd
import os, sys
import random
import time
from time import sleep
from colorama import init, Fore, Back #字體顏色
init(autoreset=True)#字體顏色
from ctypes import windll, byref
from ctypes.wintypes import SMALL_RECT
from time import sleep
WindowsSTDOUT = windll.kernel32.GetStdHandle(-11)
dimensions = SMALL_RECT(-10, -10, 120, 40) # (left, top, right, bottom)
# Width = (Right - Left) + 1; Height = (Bottom - Top) + 1
windll.kernel32.SetConsoleWindowInfo(WindowsSTDOUT, True, byref(dimensions))



#程式開始


print('')
print(Fore.CYAN +"{:=^100s}".format("歡迎使用_群旭CNC_圖到底在哪裡啊_小幫手"))
#授權時間
def now():
	return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
s = '2023-06-14 23:59:59'

if now() > s :
	print('f0614 Error :some files are missing or connection time out')
	os._exit(0)

counterror1 = 0	
counterror2 = 0
try:
	while True:
		ans = '5931'
		x = 3 #初始機會
		while x > 0 :
			x = x -1
			pwd = input('請輸入登入密碼: ')
			if pwd == ans:
				print('')
				print('')
				break
			else:
				print('密碼錯誤!')
				if x > 0:
					print('還有', x,'次機會')
				else:
					print('輸入錯誤三次，程式結束')
					print('')
					print('')
					print('3秒後程式關閉', end = '')
					for i in range(6):
						print("",end = ' ',flush = True)  #flush - 输出是否被缓存通常决定于 file，但如果 flush 关键字参数为 True，流会被强制刷新
						time.sleep(0.5)
						print('')
					os._exit(0)					
		break

	os.system('cls') #登入後清除畫面
	print('')
	print(Fore.CYAN +"{:=^100s}".format("歡迎使用_群旭CNC_圖到底在哪裡啊_小幫手"))
	print('登入成功')
	print('')
	print('')
	print('檔案讀取中', end = '')
	for i in range(3):
	    print(".",end = '',flush = True)  #flush - 输出是否被缓存通常决定于 file，但如果 flush 关键字参数为 True，流会被强制刷新
	    time.sleep(0.3)
	while True:
		try:
			
			path = '//192.168.10.61/F2-Mcx Data/'
			dir_1= []
			dir_path = []
			f = []
			xx = []
			log = []
			alldata = []
			customer = []
			cn = []#廠商編號
			print('')

		#讀取路徑
			#project_dir = 'C:/Users/cnc-3/Desktop/新增資料夾3' 
			project_dir = '//192.168.10.61/F2-Mcx Data'
			data = os.listdir(project_dir)

			name = input('請輸入查詢檔案之關鍵字(大小寫有區別):  ')

			#讀取效果	
			conversation = ['正在執行一秒幾十萬上下的讀取，請稍後','莫急莫慌莫害怕，等等就好了','已經加班在趕了，等等', '人稱找東西三十秒俠就是我，不覺得很猛嗎 ?',
			'檔案有點多，你知道嗎','別這樣，大家都是操過來的,等等','這個需求不難，很快就', '剛剛好像夢到我找完了', '你知道嗎，等等找出來的東西都是血跟淚換的', 
			'認真找起來，連我自己都會怕', '快好了，稍等一下','大哥，你這要找的也太多了吧','群旭CNC部門是最棒低','終於肯來找我幫忙了喔', '謝謝你的耐心等候','想當年找的速度超快，但現在可能要等會',
			'東西太多翻得有點亂了欸，糟糕','先說好找不到別怪我，去找辦公室的','大哥，我才快睡著又被你叫起來','已經開三班幫你找了，等等','是不是又遇到了點麻煩呢','正在從深淵搜尋中','這是小Case,真的',
			'這資料也藏得有點深，看起來很難挖','相信我真的不會很隨便找，真的','已經在找了，別急','正在裝模作樣尋找中','是不是跟著點點點呢','喝個水，等等就好了','正在執行一天大概只有三下的讀取，慢慢等吧',
			'等得有點無聊嗎，我也沒辦法','糟糕看到不該看的東西，別滅我口','沒有人在處理中，請稍後，', '你好，已依照您的指示 【調高薪資】 ，正確請按 Enter鍵 ', '別用這眼神看我，已經在找了', 
			'已經100%全力找了，看～快到連手都看不見了','警告! 正在刪除所有檔案，請稍後','正在從總經理的資料夾搜尋中','不要羨慕我找東西的能力，真的','正在塗改檔案中，反正你也不知道數字對不對', 
			'只給' + str(name) + '這幾個字，找到都不知道民國幾年了欸','正在為你搜尋公司的內部機密中','現在流行只給' + str(name) + '這幾個字，就要給你全世界？', '資料讀取中，請稍後','馬上找給你，請等會',
			'早就知道你要找有關' + str(name) + '的檔案，放心吧，都丟了','你覺得要很認真找，還是大概就可以了呢','悄悄的我走了，正如我悄悄的來； 揮一揮衣袖， 不帶走一片雲彩','找阿找，找阿找，找到外婆橋',
			'由于內容敏感，你要搜寻的资讯已被领导人屏蔽','別愣在那看，你也可以自己找找阿','已依照您的指示搜尋有關 【董事長】之相關職缺 ，請稍後','別愣在那，幫忙用愛發電給個能量好嗎']
			ha = random.choice(conversation)

			for a in data:
				if '@Rec' in a :
					continue
				else:
					dir_1.append(a)
			for d in dir_1:
				x = project_dir + '/' + d
				xx.append(x)
				for t in xx:
					cc = t.replace('//', '\\\\')
					ok_p = cc.replace('/', '\\')
				dir_path.append(ok_p)

			for d in dir_1:
				if '.' in d:
					continue
				else:
					customer.append(d)

			count_customer = 1
			for c in customer:
				num	= str(count_customer) + '.' + c
				num1 = num.split('.')
				cn.append(num1)
				count_customer = count_customer + 1

			print(Fore.CYAN +"{:=^100s}".format(''))
			for cn_single in cn:
				if '公旭' in cn_single[1]:
					print( '',Back.GREEN + Fore.RED + cn_single[0]+ '.' + cn_single[1] + Fore.BLUE +'<<<<<<<<<<常用資料夾')
				elif '史密斯' in cn_single[1]:
					print('',Back.GREEN + Fore.RED + cn_single[0]+ '.' + cn_single[1] + Fore.BLUE +'<<<<<<<<常用資料夾')
				elif '現品修改' in cn_single[1]:
					print('',Back.GREEN + Fore.RED + cn_single[0]+ '.' + cn_single[1] + Fore.BLUE +'<<<<<常用資料夾')
				elif '史密斯' in cn_single[1]:
					print('',Back.GREEN + Fore.RED + cn_single[0]+ '.' + cn_single[1] + Fore.BLUE +'<<<<<<<<常用資料夾')
				elif '穎威' in cn_single[1]:
					print('',Back.GREEN + Fore.RED + cn_single[0]+ '.' + cn_single[1] + Fore.BLUE +'<<<<<<<<<常用資料夾')	
				elif '群旭' in cn_single[1]:
					print('',Back.GREEN + Fore.RED + cn_single[0]+ '.' + cn_single[1] + Fore.BLUE +'<<<<<<<<<常用資料夾')
				elif '量產' in cn_single[1]:
					print('',Back.GREEN + Fore.RED + cn_single[0]+ '.' + cn_single[1] + Fore.BLUE +'<<<<<<<<<常用資料夾')	
				else:
					print('',cn_single[0]+ '.' +cn_single[1])
			print('')	
			

			print(Fore.CYAN +"{:=^100s}".format(''))
			print('查詢的檔案名稱關鍵字為 :' + Fore.RED + name)
			print('搜尋全部資料夾，請輸入(', Fore.YELLOW + '520',')')
			num_c = input('請輸入想搜尋的主要資料夾號碼:  ')
			print('')

			if num_c != '520':
				num_c = int(num_c) - 1
				print('輸入搜尋的資料夾為【' + Fore.RED + cn[int(num_c)][1], '】，' + '查詢之關鍵字為【', Fore.RED + name, '】')
				print('')
				print(Fore.YELLOW + ha, end = '')
				for i in range(4):
				    print(".",end = '',flush = True)
				    time.sleep(0.5)
				print('')
				print('')
				for ad in dir_path:
					count = 0
					temp = 0
					total = 300
					data_path = os.walk(ad)
					for root ,dirs, files in data_path:
						if cn[int(num_c)][1] in root:
							for ff in files:
								alldata.append(ff)
								if name in ff:
									if root in f:
										continue
									else:
										if 'old' in root:
											continue
										elif 'Old' in root:
											continue
										elif 'OLD' in root:
											continue
										else:
											f.append(root)
								else:
									continue
					for n in range(300):
						temp += 1
						print(Fore.YELLOW +'\r' + '[正在執行超激烈讀取]:[%s%s]%.2f%%;' % (
					    '█' * int(temp*20/total), ' ' * (20-int(temp*20/total)),
					    float(temp/total*100)), end='')
					sleep(0.01)
				print('')
				print('')
				print('檔案已載入完成，結果如下：')

				count1 = 1
				for final in f:
					cc = final.replace('\\\\\\\\', '\\\\')	
					print(Fore.CYAN +"{:=^100s}".format(""))
					print('第',Fore.RED + str(count1),'個路徑')
					print(cc)		
					count1 = count1 + 1
				print('')
				print(Fore.GREEN +"{:=^100s}".format(""))
				print('已從', Fore.RED + cn[int(num_c)][1], '的資料夾的' ,Fore.RED + str(len(alldata)),'筆路徑過濾出結果')
				print('共有', Fore.RED + str(len(f)),'筆路徑含有', Fore.RED + str(name), '關鍵字')
				print('')
				#搜尋紀錄LOG	
				with open('//192.168.10.61/f2-共用資料/設定檔/設定檔/cnclog.csv', 'r', encoding = 'cp950') as f:
					for txtlog in f:
						log.append(str(txtlog))

				with open('//192.168.10.61/f2-共用資料/設定檔/設定檔/cnclog.csv', 'w', encoding = 'cp950') as f:
					for l in log:
						f.write(str(l))
					f.write(str(name) + '\n')
			elif num_c == '520':
				#讀取效果
					print('')
					ha = random.choice(conversation)
					print(Fore.YELLOW + ha, end = '')
					for i in range(4):
					    print(".",end = '',flush = True)
					    time.sleep(0.5)
					print('')
					print('')
					for ad in dir_path:
						data_path = os.walk(ad)
						for root ,dirs, files in data_path:
							for ff in files:
								alldata.append(ff)
								if name in ff:
									if root in f:
										continue
									else:
										f.append(root)
								else:
									continue
						count = 0
						temp = 0
						total = 300			
						for n in range(300):
							temp += 1
							print(Fore.YELLOW +'\r' + '[正在執行超激烈讀取]:[%s%s]%.2f%%;' % (
						    '█' * int(temp*20/total), ' ' * (20-int(temp*20/total)),
						    float(temp/total*100)), end='')
						sleep(0.01)


					print('')
					print('')
					print('檔案已載入完成，結果如下：')
					print('')		

					count1 = 1
					for final in f:
						cc = final.replace('\\\\\\\\', '\\\\')	
						print(Fore.CYAN +"{:=^100s}".format(""))
						print('第',Fore.RED + str(count1),'個路徑')
						print(cc)		
						count1 = count1 + 1
					print('')
					print(Fore.GREEN +"{:=^100s}".format(""))
					print('已從',Fore.RED + str(len(alldata)),'筆路徑過濾出結果')
					print('共有',Fore.RED + str(len(f)),'筆路徑含有', Fore.RED + str(name), '關鍵字')
					print('')
					#搜尋紀錄LOG	
					with open('//192.168.10.61/f2-共用資料/設定檔/設定檔/cnclog.csv', 'r', encoding = 'cp950') as f:
						for txtlog in f:
							log.append(str(txtlog))

					with open('//192.168.10.61/f2-共用資料/設定檔/設定檔/cnclog.csv', 'w', encoding = 'cp950') as f:
						for l in log:
							f.write(str(l))
						f.write(str(name) + '\n')			
		except :
			print('發生錯誤，請確認資訊再重新查詢')
			if counterror1 >= 5:
				print('發生錯誤，程式結束')
				print('')
				print('3秒後程式關閉', end = '')
				for i in range(6):
					print("",end = ' ',flush = True)  #flush - 输出是否被缓存通常决定于 file，但如果 flush 关键字参数为 True，流会被强制刷新
					time.sleep(0.5)
					print('')
				os._exit(0)
			else:
				counterror1 = counterror1 + 1

except :
		print('Error :something went wrong')
		if counterror2 >= 5:
			print('Error，interrupt')
			print('')
			print('程式關閉', end = '')
			for i in range(6):
				print("",end = ' ',flush = True)  #flush - 输出是否被缓存通常决定于 file，但如果 flush 关键字参数为 True，流会被强制刷新
				time.sleep(0.5)
				print('')
			os._exit(0)
		else:
			counterror2 = counterror2 + 1
