import random
def monster():
	mon = []
	print("你遇到某單位處長")
	print("以下是處長的數值")
	mon_Atk=random.randint(410,500)
	print("西瓜數量",mon_Atk)
	mon_Def=random.randint(300,400)
	print("防護衣",mon_Def)
	mon_Hp=random.randint(700,800)
	print("精神指數",mon_Hp)
	print()
	mon.append(mon_Atk)
	mon.append(mon_Def)
	mon.append(mon_Hp)
	return mon

	
name=input("請輸入你的角色名稱：")
print(name,"你好,歡迎來到花蓮縣政府,以下是你的數值")
Atk=random.randint(650,700)
print("電擊槍電量",Atk)
Def=random.randint(350,400)
print("擋板",Def)
Hp=random.randint(900,950)
print("體力",Hp)
print()

print("即將進入花蓮縣政府冒險,請做好準備")
print()

mon = monster()

print("請問你要?")
a = eval(input("1:電擊他,2:擋瓜,3:逃跑"))

time = 0
while True:
	if a==1:
		mon[2] = mon[2] - (Atk - mon[1])
		Hp = Hp - (mon[0] - Def)
		print("官員受到電擊，官員剩餘精神指數",mon[2])
		print("你的體力",Hp)
	elif a==2:
		x = random.randint(1,2)
		if x == 1:
			mon[2]=mon[2]-100
			print("防禦成功,同時西瓜反砸,官員目前精神指數為",mon[2])
		else:
			Hp=Hp - (mon[0] - Def)
			print("防禦失敗,被砸西瓜,你目前體力為",Hp)
	elif a==3:
		x = random.randint(1,2)
		if x==1:
			print("逃跑成功")
			break
		else:
			Hp=Hp - 50
			print("逃跑失敗,已被縣府官員砸西瓜,你目前體力為",Hp)
	else:
		print("輸入錯誤,請重新輸入")
	
	if Hp <= 0:
		print("你已被西瓜砸昏 遊戲結束")
		print("你電昏了"+str(time)+"位官員")
		break
	elif mon[2] <= 0:
		print("你電昏了縣府官員,遇到下一位官員")
		print()
		mon = monster()
		time = time + 1
	a = eval(input("1:電擊他,2:擋西瓜,3:逃跑"))