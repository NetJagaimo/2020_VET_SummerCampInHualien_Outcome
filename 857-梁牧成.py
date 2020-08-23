def start():
	print("某個早上\n")
	print("同學揪你去爬自由女神或者101\n")
	print("請問你要去爬\"自由女神\"還是\"自由女神\"不要去\"")
	while True:
		move = input(">")
		if move =="自由女神":
			print("可是\n")
			print("你發現你很窮\n")
			print("沒辦法跟同學搭飛機去\n")
			print("只能用或者游過去\n")
			go()

		elif move =="不要去":
			print("你朋友剛好氣在來\n")
			print("跟你說:是不是朋友拉\n")
			print("我是你男朋友拉\n")
			print("他就不想跟你說那麼多")
			print("他就直接拿出我們可愛的指甲剪")
			print("後面我就不多說")
			over()
		else :
			print("注意你的態度，不要給我亂打")

def go():
	print("請選擇要找\"青蛙\"還是\"自殺\"")
	while True:
		move = input(">")
		if move =="青蛙":
			print("你去了太魯閣\n")
			print("找了找\n")
			print("看到了莫氏樹蛙\n")
			print("你看了看\n")
			print("慢慢走過去之時\n")
			print("他就呱，呱，呱\n")
			print("青蛙OS:這個人一定是來抓我去游泳\n")
			print("青蛙OS:厚，我已經游了N遍了\n")
			print("青蛙OS:到底為甚麼不能找海豚拉\n")
			print("此時我決定用民主的方式[投票],青蛙去游泳的舉手。好!一票。青蛙不去游泳的舉手。此時青蛙舉起了他的腳,好!0票。\n")
			print("青蛙相當生氣押\n")
			frog()
		if move == '自殺':
			print('你已經死了')
			over()
			break
		else:
			print("注意你的態度，不要給我亂打\n")
def over():
	print("遊戲結束")
	exit()

def frog():
	print("回程時遇到了黑熊\n")
	print("這時身上只有一些東西可以防身\n")
	print("青蛙、冷笑話、手機鏡頭\n")
	print("選要用\"青蛙\"、\'冷笑話\'、\"手機鏡頭\"")

	while True:
		move = input(">")
		if move =="青蛙":
			print("你把青蛙丟了出去\n")
			print("青蛙一臉矇逼\n")
			print("灰熊三話不說,直接把青蛙一口shot掉\n")
			over()


		elif move =="冷笑話":
			print("你跟他說:ㄟ灰熊，我跟你說喔.\n")
			print("前幾天我去學校，老師問我說:你昨天怎麼沒來學校?\n")
			print("你說:我爸爸在醫院阿\n")
			print("昨天我去學校，老師問我說:阿你爸爸還在醫院嗎?\n")
			print("對阿!他是位醫生\n")
			print("灰熊覺得傻眼。。。。。也是一把你shot掉\n")
			over()
		elif move =="手機鏡頭":
			print("你拿出了手機鏡頭\n")
			print("灰熊看到了，看起來絲毫沒有動靜，兩秒過後，直接往你這邊衝了過來。\n")
			print("你直接嚇到倒地\n")
			print("請選擇要\"巴頭\"還是\"繼續倒地一臉矇逼\"")
			move2 = input(">")
			if move2 =="巴頭":
				print("灰熊就很氣，一口把你shot掉\n")
				over()
			elif move2 =="繼續倒地一臉矇逼":
				print("你就繼續一臉矇逼\n")
				lie()
			else :
				print("注意你的態度，不要給我亂打")
		else:("注意你的態度，不要給我亂打")
def lie():
	print("接著灰熊搶走你手中那個手機鏡頭")
	print("它跑走了")
	abc()
def abc():
	print("請選擇要去\"花蓮港\"還是\"高雄港\"")
	while True:
		move =input(">")
		if move =="花蓮港":
			print("到了海邊\n")
			print("你看到了遊輪，並且溜了上去\n")
			print("過了7749天，你到了美國遇到了朋友們，跟他們一起去爬自由女神\n")
			print("恭喜你!\n")
			over()

		elif move =="高雄港":
			print("到了海邊\n")
			print("看到了韓國魚\n")
			print("你抓來吃，剛吃完。你的頭馬上光頭。\n")
			print("你因為沒了頭髮,不敢去見同學,所以你回家了\n")
			over()
start()