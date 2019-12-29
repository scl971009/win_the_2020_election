import sys
import pygame
from pygame.locals import QUIT

#[character][level]
title_list = [["第一關\n翻轉高雄", "第二關\n黑韓產業鏈","第三關\n摑面黨內初選",
               "第四關\n罷免X韓假","第五關\n2020總統大選"]]

#story_list[character][level][op_ed][line]
story_list = [[
               [["2002年，政壇失利；11年後，出任北農總經理……開始嶄露頭角", 
                 "距離1124的縣市首長大選只剩不到百日，靠著「又老又窮」的一席話、「愛情摩天輪與太平島挖石油」、以及「愛與包容」，他，震撼了整個高雄！！！",
                　"他，究竟是誰？", "他是……韓    國    瑜！"], 
                ["眾望所歸、萬庶民擁戴的韓ㄉ….噢不，韓總終於打敗了陳其邁，成功地當上高雄市長；但，事情似乎沒有韓總想的辣麼簡單……"]], 
               [["韓市長不只市政要忙，同時也忙著應付議會內尖銳的質詢，以及各方媒體的放大檢視。「黃捷」、「韓總機」、「中央卡韓不給預算」、甚至「潘恆旭」…等，韓市長上任後爭議層出不窮。", 
                 "雖然韓市長靠著九二共識競競業業地到大陸地區簽署各類庶民MOU，但風向似乎與選前稍稍地有了些許不同……"], 
                ["歷經韓黑份子、預算卡韓、1450、爵卿等各類黑韓產業鏈的四處抹黑，韓市長用闢眼看著他們，一派輕鬆地將這些假韓粉們一一擊倒。", 
                 "緊接著，摑面黨的2020總統候選人初選即將開始；苦民所苦，睡到中午的韓市長漸漸地，開始想替高雄以外的庶民盡一份心力，整日輾轉反側……"]],
               [["相信不只是高雄人，全台灣人需要一個富有魅力、幽默的領導來下架民進黨，挑戰蔡英文。為了中華民國不惜粉身碎骨。",
                 "不過在那之前要先在黨內出選勝出，才能取得總統大選的門票。",
                 "初選的結果究竟是……"],
                ["在經歷腥風血雨的初選，最終是由人民的韓國瑜贏得總統大選的門票；",
                 "但，距離總統的寶座還有一段距離……。"]],
               [["在經過激烈的黨內初選後，韓國輸距離總統僅一步之遙。",
                 "不過隨著大選的到來，「現在有5顆核彈在等著炸死韓國瑜，老大哥正在睜大眼睛看」，民調的結果也隨之變化莫測。",
                 "看來又是一場腥風血雨……"],
                ["「非常小癟三、非常窩囊的行為」",
                 "「得民心者，得天下；得民調者，得痔瘡！」。",
                 "「假民調！」",
                 "韓國輸似乎已經找到對付神掌與香菜英文的絕佳方法了，終於又離總統寶座近了一步……"]],
               [["該來的總是要來，終於來到了最終決戰，究竟這場三方對決的結果會是如何呢?",
                 "我們的庶民總統會獲勝嗎?",
                 "讓我們繼續看下去……"],
                ["終於，韓總成為了庶民總統。達到了此生的巔峰。",
                 "不過，人生就是不斷尋找著下一個目標，就如同曾經說過的：",
                 "「立足台灣，胸懷大陸；」",
                 "「放眼世界，征服宇宙！」"]]]]

def start(window_surface, character, level, op_ed):
	"""
	show the corresponding interlude

	arg:
		window_surface: the window_surface to draw scene
		character: which character's interlude to show
		level: which level to show
		op_ed: show OP or ED
	"""
	if not op_ed:
		print(title_list[character][level])
		clicked = False
		while not clicked:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONUP:
					if event.button == 1:
						print(story_list[character][level][op_ed][0])
						clicked = True
	else:
		print(story_list[character][level][op_ed][0])

	for line in story_list[character][level][op_ed][1:]:
		clicked = False
		while not clicked:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONUP:
					if event.button == 1:
						print(line)
						clicked = True

class Intelude():
	def __init__(self, window_surface, character, level, op_ed):
		"""
		init variables of Intelude

		arg:
			window_surface: window_surface to draw scene
			character:
				0: korea fish's intelude story
			level: which level the player is reading
			op_ed:
				0: OP
				1: ED
		"""
		self.window_surface = window_surface
		self.character = character
		self.level = level
		self.op_ed = op_ed

	def run(self):
		"""call start with its arguments"""
		start(self.window_surface, self.character, self.level, self.op_ed)
