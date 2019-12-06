import sys
import pygame
from pygame.locals import QUIT

#[character][level]
title_list = [["第一關\n翻轉高雄", "第二關\n黑韓產業鏈"]]

#story_list[character][level][op_ed][line]
story_list = [[[["2002年，政壇失利；11年後，出任北農總經理…….開始嶄露頭角", 
                 "距離1124的縣市首長大選只剩不到百日，靠著「又老又窮」的一席話、「愛情摩天輪與太平島挖石油」、以及「愛與包容」，他，震撼了整個高雄！！！", 
                 "他，究竟是誰？", 
                 "他是……韓    國    瑜！"], 
                ["眾望所歸、萬庶民擁戴的韓ㄉ….噢不，韓總終於打敗了陳其邁，成功地當上高雄市長；但，事情似乎沒有韓總想的辣麼簡單……"]], 
               [["韓市長不只市政要忙，同時也忙著應付議會內尖銳的執行，以及各方媒體的放大檢視。「黃捷」、「韓總機」、「中央卡韓不給預算」、甚至「潘恆旭」…等，韓市長上任後爭議層出不窮。", 
                 "雖然韓市長靠著九二共識競競業業地到大陸地區簽署各類庶民MOU，但風向似乎與選前稍稍地有了些許不同……"], 
                ["歷經韓黑份子、預算卡韓、1450、爵卿等各類黑韓產業鏈的四處抹黑，韓市長用闢眼看著他們，一派輕鬆地將這些假韓粉們一一擊倒。", 
                 "緊接著，摑面黨的2020總統候選人初選即將開始；苦民所苦，睡到中午的韓市長漸漸地，開始想替高雄以外的庶民盡一份心力，整日輾轉反側……"]]]]

def start(character, level, op_ed):
	"""
	show the corresponding interlude

	arg:
		character: which character's interlude to show
		level: which level to show
		op_ed: show OP or ED
	"""
	if op_ed:
		print(title_list[character][level])
		clicked = 0
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONUP:
					if event.button == 1:
						print(story_list[character][level][op_ed][0])
						clicked = 1
			if clicked:
				break
	else:
		print(story_list[character][level][op_ed][0])

	for line in story_list[character][level][op_ed][1:]:
		clicked = 0
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONUP:
					if event.button == 1:
						print(line)
						clicked = 1
			if clicked:
				break

class Intelude():
	def __init__(self, window_surface, character, level, op_ed):
		"""
		init variables of Intelude

		arg:
			window_surface: window_surface to draw scene
			character:
				0: korean fish's intelude story
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
		start(self.character, self.level, self.op_ed)
