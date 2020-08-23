import	random

def	enemy():
	Attributes=	[]
	Hp	=	random.randint(50,100)
	Act	=	random.randint(3,65)
	Def	=	random.randint(-7,7)
	Attributes.append(Hp)
	Attributes.append(Act)
	Attributes.append(Def)
	return	Attributes

def	fire():
		fire_act	=	random.randint(20,40)
		return	fire_act

def	flee():
	success	=	random.randint(0,50)
	if	(success	%	5)	==	0:
		return	True
	else:
		return	False

name	=	input("請輸入你的角色名稱:")
protagoist_hp	=	random.randint(200,400)
protagoist_mp	=	random.randint(40,80)
protagoist_act	=	random.randint(5,50)
protagoist_def	=	random.randint(0,10)

print(name,"嗨,歡迎飛到豬豬世界,以下是你的能力值表")
print("血量:",	protagoist_hp)
print("魔力:",	protagoist_mp)
print("功擊:",	protagoist_act)
print("防禦:",	protagoist_def)

print("我們即將進入菜鳥的初次戰鬥,祝你早點掛掉")
print()

enemy_tribe	=	random.randint(1,3)
print("你這次面臨的野豬有",enemy_tribe	,"頭")
enemys	=	[]
die	=	-1
for	i	in	range(enemy_tribe):
	enemys.append(enemy())

while	len(enemys)	>	0	and	protagoist_hp	>	0:
	print("請選擇要執行的操作")
	print("1.	功擊")
	print("2.	法術")
	print("3.	逃跑")
	chose	=	eval(input())
	if	chose	==	1:
		Critical_strike	=	random.randint(1,10)	#爆擊率

		for	i	in	range(len(enemys)):
			if	enemys[i]	!=[]:
				print("野豬",	i+1,	end="	")
				print()
		fighting	=	eval(input("請選擇要攻擊的野豬："))	-	1
		if	Critical_strike	%	3	==	0:
			if	protagoist_act	*	2	>	enemys[fighting][2]:
				enemys[fighting][0]	=	enemys[fighting][0]	-	(protagoist_act	*	2	-	enemys[fighting][2])
				print("給予了致命一擊!!!,造成",	(protagoist_act		*	-	enemys[fighting][2]),	"點傷害")
			else:
				print("雖然大力的砍下去,但是野豬皮很硬")	
		else:
			if	protagoist_act>	enemys[fighting][2]:
				enemys[fighting][0]	=	enemys[fighting][0]	-	(protagoist_act	-	enemys[fighting][2])
				print("擊中造成",(protagoist_act	-	enemys[fighting][2]),	"點傷害")	
			else:
				print("野豬成功擋開了功擊")
	elif	chose	==	2:
		for	i	in	range(len(enemys)):
			if	enemys[i]	!=	[]:
				print("野豬",i+1,	end="	")
				print()
		fighting	=	eval(input("請選擇要功擊的野豬:"))	-	1
		if	protagoist_mp	>	0:
			magic_act	=	fire()
		if	magic_act	>	enemys[fighting][2]:
			enemys[fighting][0]	=	enemys[fighting][0]	-	(magic_act -enemys[fighting][2])
			protagoist_mp	=	protagoist_mp	-	10
			print("你射出的火弓箭成功刺傷野豬造成",(magic_act	-	enemys[fighting][2]),"點傷害")	
			print("弓箭上的火似乎變小了")
		else:
			print("你的魔力不足")
			continue
	elif	chose	==3:
		if	flee()	==	True:
			print("逃跑成功")
			break
		else:
			print("逃跑失敗")
	else:
		print("你放棄了動作")
		print()

	for	i	in	range(len(enemys)):
		if	enemys[i][0]	>	0:
			if	enemys[i][1]	>	protagoist_def:
				protagoist_hp	=	protagoist_hp	-	(enemys[i][1]	-	protagoist_def)
				print("大野豬",i+1,"飛了上來,狠狠咬了一口,受到",	enemys[i][1]	-	protagoist_def,	"傷害")
			else:
				print("野豬",i+1,"的功擊對你來說沒什麼")
		else:
			die	=	i	
		print(enemys[i])

if	die	!=	-1:
	enemys.remove(enemys[die])
	die	=	-1	

	print()
	print("你的血量:",	protagoist_hp)
	print("你的魔力",	protagoist_mp)
	print("你的功擊",	protagoist_act)
	print("你的防禦:",		protagoist_def)
	print()

if	protagoist_hp	>= 0:
	print("重打吧,你太爛了")
else:
	print("你竟然在初戰裡打敗了這些臭豬,去村辦公室領取你收穫的寶物吧")
print("等待下一場戰鬥")	

