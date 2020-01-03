import sys
import os
import pygame
from pygame.locals import QUIT

#[character][level][title]
title_list = [[["第一關","翻轉高雄"], ["第二關","黑韓產業鏈"],["第三關","國瑜黨內初選"],
               ["第四關","罷免X韓假"],["第五關","2020總統大選"]]]

#story_list[character][level][op_ed][line]  the last empty string is for awaiting users to click and start
story_list = [[[["2002年，政壇失利；11年後，出任北農總經理……開始嶄露頭角", 
                 "距離1124的縣市首長大選只剩不到百日",
                 "靠著「又老又窮」的一席話、「愛情摩天輪與太平島挖石油」、以及「愛與包容」",
                 "他，震撼了整個高雄！！！",
                 "他，究竟是誰？",
                 "他是……韓    國    瑜！",
                 ""], 
                ["眾望所歸、萬庶民擁戴的韓ㄉ…噢不，是韓總",
                 "我大韓總終於打敗了陳其邁，成功地當上高雄市長",
                 "但...",
                 "事情似乎沒有韓總想的辣麼簡單……",
                 ""]], 
               [["韓市長不只市政要忙，同時也忙著應付議會內尖銳的質詢，以及各方媒體的放大檢視",
                 "「黃捷」、「韓總機」、「預算卡韓」、甚至「潘恆旭」…等",
                 "韓市長上任後爭議層出不窮", 
                 "雖然韓市長靠著九二共識競競業業地，到大陸地區簽署各類庶民MOU",
                 "然而，風向似乎與選前稍稍地有了些許不同……",
                 ""], 
                ["歷經韓黑份子、預算卡韓、1450、爵卿等各類黑韓產業鏈的四處抹黑",
                 "韓市長用闢眼看著他們，一派輕鬆地將這些假韓粉們一一擊倒", 
                 "緊接著，摑面黨的2020總統候選人初選即將開始；",
                 "苦民所苦，睡到中午的韓市長",
                 "整日輾轉反側，心想替高雄以外的庶民盡一份心力！",
                 ""]],
               [["相信不只是高雄人",
                 "而是全台灣人",
                 "需要一個富有魅力、幽默的領導來下架民進黨",
                 "挑戰蔡英文！",
                 "為了中華民國不惜粉身碎骨！！！",
                 "不過在那之前要先在國瑜黨內初選勝出，才能取得總統大選的門票",
                 "初選的結果究竟是……",
                 ""],
                ["在經歷腥風血雨的初選，最終不出所料，是由庶民代表韓總機贏得總統大選的門票；",
                 "但，距離總統的寶座還有一段距離……。",
                 ""]],
               [["在經過激烈的黨內初選後，韓國輸距離總統僅一步之遙。",
                 "不過隨著大選的到來……",
                 "「現在有5顆核彈在等著炸死韓國瑜，老大哥正在睜大眼睛看」，民調的結果也隨之變化莫測",
                 "看來又是一場腥風血雨……",
                 ""],
                ["「非常小癟三、非常窩囊的行為」",
                 "「得民心者，得天下；得民調者，得痔瘡！」",
                 "「假民調！」",
                 "韓國輸似乎已經找到對付神掌與香菜英文的絕佳方法了",
                 "終於又離總統寶座近了一步！",
                 ""]],
               [["該來的總是要來，終於來到了最終決戰",
                 "究竟這場三方對決的結果會是如何呢？",
                 "我們的庶民總統、蔣公轉世、世界的偉人韓總機會獲勝嗎？",
                 "讓我們繼續看下去……",
                 ""],
                ["終於！！！！！",
                 "韓總成為了庶民總統，達到了此生的巔峰",
                 "不過，人生就是不斷尋找著下一個目標，就如同韓總統 國瑜曾經說過的：",
                 "「立足台灣，胸懷大陸；",
                 "放眼世界，征服宇宙！」",
                 ""]]]]

#define color
black = (0,0,0)
white = (255,255,255)

def title_font_create(window_surface,character,level):
     font = pygame.font.Font('story\\fonts\\msj.ttf', 30)        #title format (reusable)
     level_num = font.render(title_list[character][level][0],True, white, black)  #str, True, string_color, str_bg_color #level==0
     level_num_rect = level_num.get_rect()
     level_num_rect.center = (400, 100)
     window_surface.blit(level_num,level_num_rect)

     level_title = font.render(title_list[character][level][1],True, white, black)  #str, True, string_color, str_bg_color #level==0
     level_title_rect = level_title.get_rect()
     level_title_rect.center = (400, 140)
     window_surface.blit(level_title,level_title_rect)

def intelude_BG(window_surface, file_name_1, file_name_2, file_name_3):
     intelude_bg = pygame.image.load(os.path.join(file_name_1,file_name_2, file_name_3))
     intelude_bg = pygame.transform.scale(intelude_bg, (800, 600))
     intelude_bg = intelude_bg.convert()
     window_surface.blit(intelude_bg, (0, 0))

def click_continue_line(window_surface):                    #remind user to click continue
     font = pygame.font.Font('story\\fonts\\msj.ttf', 18)
     continue_line = font.render("Click anywhere to continue...",True,white,black)
     continue_line_rect = continue_line.get_rect()
     continue_line_rect.center = (400,550)
     window_surface.blit(continue_line, continue_line_rect)
     

def start(window_surface, character, level, op_ed): #basal_bg,character,(0 is LV 1), 0 is op / 1 is ed
        """
        show the corresponding interlude

        arg:
                window_surface: the window_surface to draw scene
                character: which character's interlude to show
                level: which level to show
                op_ed: show OP(0) or ED(1)
        """

        if not op_ed:            #op = 0 in the begining

             if level == 0:
                  intelude_BG(window_surface, "img","intelude","korean_0_op.png")
                  title_font_create(window_surface,character,level)
                  click_continue_line(window_surface)
                  pygame.display.update()
                  
             elif level == 1:
                  intelude_BG(window_surface,"img","intelude","korean_1_op.png")
                  title_font_create(window_surface,character,level)
                  click_continue_line(window_surface)
                  pygame.display.update()
                  
             elif level == 2:
                  intelude_BG(window_surface,"img","intelude","korean_2_op.png")
                  title_font_create(window_surface,character,level)
                  click_continue_line(window_surface)
                  pygame.display.update()

             elif level == 3:
                  intelude_BG(window_surface,"img","intelude","korean_3_op.png")
                  title_font_create(window_surface,character,level)
                  click_continue_line(window_surface)
                  pygame.display.update()

             elif level == 4:
                  intelude_BG(window_surface,"img","intelude","korean_4_op.png")
                  title_font_create(window_surface,character,level)
                  click_continue_line(window_surface)
                  pygame.display.update()

             line_pos =  200   
             for line in story_list[character][level][op_ed][0:]:
                                           
                  clicked = False
                  while not clicked:
                       for event in pygame.event.get():
                            if event.type == QUIT:
                                 pygame.quit()
                                 sys.exit()
                            elif event.type == pygame.MOUSEBUTTONUP:
                                 if event.button == 1:
                                      print(line)
                                      
                                      font = pygame.font.Font('story\\fonts\\msj.ttf', 18)
                                      line_text = font.render(line,True,white,black)
                                      line_rect = line_text.get_rect()
                                      line_rect.center = (400,line_pos)
                                      line_pos += 40
                                      window_surface.blit(line_text,line_rect)
                                      pygame.display.update() 
    
                                      clicked = True

                                      if line == story_list[character][level][op_ed][len(story_list[character][level][op_ed])-2]:  
                                           font = pygame.font.Font('story\\fonts\\msj.ttf', 18)
                                           line_text = font.render("  Click anywhere to start. . . . ",True,black,white)
                                           line_rect = line_text.get_rect()
                                           line_rect.center = (400,550)
                                           window_surface.blit(line_text,line_rect)
                                           pygame.display.update()
                                      
                                      

        else:   #op_ed == 1, ending bg
             if level == 0:
                  intelude_BG(window_surface,"img","intelude","korean_0_ed.png")
                  click_continue_line(window_surface)
                  
                  pygame.display.update()

             elif level == 1:
                  intelude_BG(window_surface,"img","intelude","korean_1_ed.png")
                  click_continue_line(window_surface)
                  
                  pygame.display.update()

             elif level == 2:
                  intelude_BG(window_surface,"img","intelude","korean_2_ed.png")
                  click_continue_line(window_surface)
                  
                  pygame.display.update()

             elif level == 3:
                  intelude_BG(window_surface,"img","intelude","korean_3_ed.png")
                  click_continue_line(window_surface)
                  
                  pygame.display.update()

                  #level 4 requires new codes
                  
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
