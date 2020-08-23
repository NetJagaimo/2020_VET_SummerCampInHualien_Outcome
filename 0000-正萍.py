import random
print("歡迎來到王子農藥")
a=input("請輸入名字")
print("我們生活在和平的世界，突然有天長得很醜的人把阿嬤賣掉，我們知道後，非常的生氣,於是下了戰帖，約在")
i="1"
while True and i=="1" :
	print("1.王者戰場\n2.吃雞戰場\n3.家旁邊的空地\n4.老人公園")
	d=input("選擇地點")
	while True :
		if d=="1" :	
			d1="王者戰場"
			break
		elif d=="2" :	
			d1="吃雞戰場"
			break
		elif d=="3" :	
			d1="家旁邊的空地"
			break
		elif d=="4" :	
			d1="老人公園"
			break
		else :
			print("地點輸入錯誤,請重新選擇")
			d=input("請重新選擇地點")		

	print("\n1.魏嬰\n2.藍湛\n3.金光瑤\n4.江澄\n5.溫寧")
	b=input("請選擇你要的角色")
	while True :
		if b=="1" :	
			b5="魏嬰"
			break
		elif b=="2" :	
			b5="藍湛"
			break
		elif b=="3" :	
			b5="金光瑤"
			break
		elif b=="4" :	
			b5="江澄"
			break
		elif b=="5" :	
			b5="溫寧"
			break
		else :
			print("角色輸入錯誤,請重新選擇")
			b=input("請重新選擇角色")		
	print("\n1.陳情\n2.AK47\n3.閃彈槍\n4.大刀\n5平底鍋")
	c=input("請選擇你要的武器")
	while True :
		if c=="1" :	
			c1="陳情"
			break
		elif c=="2" :	
			c1="AK47"
			break
		elif c=="3" :	
			c1="閃彈槍"
			break
		elif c=="4" :	
			c1="大刀"
			break
		elif c=="5" :	
			c1="平底鍋"
			break
		else :
			print("武器輸入錯誤,請重新選擇")
			c=input("請重新選擇武器")		
	print("我方召喚出了"+b5+",使用了"+c1+",相約在"+d1+"\n以下是我方和敵人的數值")
	b1=random.randint(10,98) #攻擊力數值
	b2=random.randint(10,39) #防禦力數值
	b3=random.randint(15,60) #魅力指數
	b4=random.randint(80,200) #血量數值
	e1=random.randint(10,90) #攻擊力數值
	e2=random.randint(8,38) #防禦力數值
	e3=random.randint(15,60) #魅力指數
	e4=random.randint(50,150) #血量數值
	print("\n我方攻擊力是",b1,"\n我方防禦力是",b2,"\n我方魅力是",b3,"\n我方血量",b4)
	print("\n敵人攻擊力是",e1,"\n敵人防禦力是",e2,"\n敵人魅力是",e3,"\n敵人血量",e4)
	while  b4>0 and e4>0:
		print("\n1.攻擊\n2.魅力\n3.逃跑")
		s=input("請選擇動作")
		if s=="1" :
			q=random.randint(0,1)
			if q==0 :
				print("攻擊失敗,請重新選擇")
				
			elif q==1 :
				e4=e4-(b1-e2) #敵人血量
				print("攻擊成功,敵人剩餘血量為",e4)
				
		elif s=="2" :
			q1=random.randint(0,1)
			if q1==0 :
				print("誘惑失敗,請重新選擇")
				
			elif q1==1 :
				e4=e4-(b3-e3) #敵人血量
				print("魅惑成功,敵人剩餘血量為",e4)
				
		elif s=="3" :
			q2=random.randint(0,1)
			if q2==0 :
				print("逃跑失敗,請重新選擇")
				
			elif q2==1 :
				print("逃跑成功,換地方再戰")
				break
		b4=b4-(e1-b2)
		print("敵人朝"+b5+"打了一拳,我方剩餘血量為",b4)
		if b4<=0 or e4<=0 :
			i=input("\n如果還想繼續請按1,想結束請輸入2")
			
			if i=="1" :
				print("打得不夠盡興,於是我們再約一場")
				continue
			elif i=="2" :
				break
print("遊戲結束,可以回家啦!")
p=input()




