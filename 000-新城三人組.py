def	start():
	print("有一天你穿越了時空")
	print("發現自己到了古代")
	ans = input("你會變成?\n(1)宮廷裏的婢女\n(2)大地主的閨女\n(3)被打入冷宮的貴妃")
	while True:
		if ans == '1':			
			s1()
		elif ans=='2':
			s2()
		elif ans=='3':
			s3()
		else:
			print("輸入錯誤，請重新輸入")
			quit()

def	bad():
	print("一輩子做婢女，永不見皇上")
	quit()

def good():
	print("雖沒有獲得皇上的寵愛，但嫁了個好人家")
	quit()
def	win():
	print("得到皇上青睞")
	quit()
def rich():
	print("從此不愁吃穿")
	quit()
def fight():
	print("奪回貴妃之位")
	quit()
def	dead():
	print("game over")
	quit()

def s1():
	a = input("選擇一個動作:\n(1)出現在皇上面前，假裝跌倒\n(2)認命做事")
	if a=="1":
		print("被皇太后下令打五十大板")
		bad()	
	elif a=="2":
		print("得到五十兩銀子")
		good()


def s2():
	b=input("選擇一個動作:\n(1)答應父親入宮選妃\n(2)繼承自家事業")
	if b=="1":
		print("父親得到好官位，自己也如願以償當上了淑嬪")
		win()
	elif b=="2":
		print("土地豐收，變成大富翁")
		rich()
def s3():
	c=input("選擇一個動作:\n(1)努力討皇上歡心\n(2)重新做人")
	if c=="1":
		print("脫離冷宮")
		fight()

		
	elif c=="2":
		print("上吊自殺")
		dead()

start()