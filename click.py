import pygame, sys
from pygame.locals import QUIT
import time
import math
import random

pygame.init()
# assigning variables
width, height = 800, 600
clock = pygame.time.Clock()
player = pygame.Rect((width / 2) - 16, (height / 2) - 16, 32, 32)
screen = pygame.display.set_mode((width, height))
money = 0
page = 1
font = pygame.font.SysFont("Oswald", 45)
button_font = pygame.font.SysFont("Oswald", 30)
menu = pygame.Rect(400, 0, 400, height)
show_menu = False
show_stats = False
clicked = False
multiplier = 1
income = 1
red = (255, 0, 0)
blue = (0, 0, 255)
x , y = 0,0
xp = 0
max_xp = 50
xp_bar_bg = pygame.Rect(245 , 0 , 310 , 40)
shop_menu = pygame.Rect(400, 0, 400, height)
better_upgrade_cost = 50000
better_upgrade_level = 1
clicks = 0
tutorial = True
#
randomx = 0
randomy = 0
multiply_cost = 100
multiply_level = 0
earn_cost = 50
earn_level  = 0
auto_cost = 500
autoclick = 0
autoclick_level = 0
xp_cost = 200
xp_gain = 1
xp_level = 0
level = 0
luck = 0
luck_cost = 300
luck_level = 0
not_unlocked = pygame.Rect(0,0,400, 60)
player_colour = (255,255,255)
shop_level = 0
shop_cost = 5000
shop_open = False
show_stats = False
rainbow_cost = 60000
rainbow_level = 0
rainbow_list = [(255,0,0), (255,165,0),(255,255,0),(0,255,0),(0,0,255),(75,0,130),(127,0,255)]
rainbow_index = 1
assistant_cost = 5000
assistant_level = 0
shop_things = ["Assistant", "Better help"]
assistant_list = []
assistant_colour_list = [(255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (128, 0, 128),  # Purple
    (0, 128, 128),  # Teal
    (255, 165, 0),  # Orange
    (0, 255, 255),  # Cyan
    (139, 69, 19),  # Brown
    (255, 192, 203) # Pink
                         ]
lubricant_cost = 6000
lubricant_level = 0
better_assistant_cost = 50000
better_assistant_level = 1
show_merge_menu = False
merge_find = 1
fast_fingers_cost = 10000
fast_fingers_level = 1



#tutorial
def do_tutorial(page):
    if page == 1:
        screen.fill((0,0,0))
        pygame.draw.rect(screen , (50,50,50), pygame.Rect(200, 200, 400, 200))
        screen.blit(button_font.render("Welcome to the game!", True, (255,255,255)), (200,200))
        screen.blit(button_font.render("The goal of this game is to earn money.", True, (255,255,255)), (200, 230))
        screen.blit(button_font.render("Press Space to continue", True, (255,255,255)), (width / 2 - 100, height - 220))
    if page == 2:
        screen.fill((0,0,0))
        pygame.draw.rect(screen , (50,50,50), pygame.Rect(200, 200, 400, 200))
        screen.blit(button_font.render("Pressing spacebar earns money!", True, (255,255,255)), (200,200))
        pygame.draw.rect(screen , (255,25,255) , pygame.Rect(0, 0, 250 , 40))
        pygame.draw.line(screen , (0,0,0) , (0 , 0) , (250,0), width = 5)
        pygame.draw.line(screen, (0, 0, 0), (0,0), (0,40), width=5)
        pygame.draw.line(screen, (0, 0, 0), (0,40), (250,40), width=5)
        pygame.draw.line(screen, (0, 0, 0), (250,0), (250,40), width=5)
        screen.blit(font.render("Money: 0", True, (0,0,0)), (10, 10))
        screen.blit(button_font.render("You can use money to buy things in shops", True, (255,255,255)), (200, 230))
        screen.blit(button_font.render("Press B to open shops", True, (255,255,255)), (200, 260))
        screen.blit(button_font.render("Press Space to continue", True, (255,255,255)), (width / 2 - 100, height - 220))
    if page == 3:
        screen.fill((0,0,0))
        pygame.draw.rect(screen , (50,50,50), pygame.Rect(200, 200, 400, 200))
        screen.blit(button_font.render("You will unlock more things as you gain XP", True, (255,255,255)), (200,200))
        screen.blit(button_font.render("This speeds up the earning process", True, (255,255,255)), (200,230))
        screen.blit(button_font.render("Press Space to continue", True, (255,255,255)), (width / 2 - 100, height - 220))
        
        displayed_xp = button_font.render("{0}/{1}XP".format(xp , max_xp), True, (200,120,193))
        displayed_xp_rect = displayed_xp.get_rect(center=(width / 2, 60))
        pygame.draw.rect(screen, (255,255,255), xp_bar_bg)
        pygame.draw.line(screen, (0,0,0) , (245 , 1) , (555, 1), width  = 3)
        pygame.draw.line(screen, (0,0,0) , (245 , 0) , (245 , 40) , width = 3)
        pygame.draw.line(screen, (0,0,0) , (555 , 0) , (555, 40), width  = 3)
        pygame.draw.line(screen, (0,0,0) , (245 , 40) , (555 , 40) , width = 3)
        pygame.draw.rect(screen , (0,100,255) , pygame.Rect(250 , 5 , 150 , 30))
        screen.blit(displayed_xp , displayed_xp_rect)
        screen.blit(button_font.render("Press Space to continue", True, (255,255,255)), (width / 2 - 100, height - 220))
    if page == 4:
        screen.fill((0,0,0))
        pygame.draw.rect(screen , (50,50,50), pygame.Rect(200, 200, 400, 200))
        screen.blit(button_font.render("There can be new instructions that appear on screen", True, (255,255,255)), (200,200))
        screen.blit(button_font.render("Do be alert for these new instructions!", True, (255,255,255)), (200,230))
        screen.blit(font.render("Click space to earn money" , True, (255,255,255)) , (0 , height - 30))
    if page == 5:
        screen.fill((0,0,0))
        pygame.draw.rect(screen , (50,50,50), pygame.Rect(200, 200, 400, 200))
        screen.blit(button_font.render("This is the end of the tutorial", True, (255,255,255)), (200,200))
        screen.blit(button_font.render("Press Space to continue", True, (255,255,255)), (width / 2 - 100, height - 220))
        
        
        
        
    
# classes and def
def find_space(string):
    return len(string) - (string[::-1].find(' '))
class button(pygame.sprite.Sprite):
    button_col = (0, 255, 0)
    hover_col = (200, 200, 100)
    text_col = (0, 0, 0)
    width = 120
    height = 40

    def __init__(self, x, y, text, cost , level_req, descp):
        self.x = x
        self.y = y
        self.text = text
        self.cost = cost
        self.level_req = level_req
        self.descp = descp
        global level

    def draw_button(self):
        global shop_things
        global shop_level

        global clicked
        action = False

        pos = pygame.mouse.get_pos()
        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, check_if_can_buy(self.cost), button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_col, button_rect)
                if len(self.descp) > 18:
                    screen.blit((pygame.font.SysFont("Oswald" , 20)).render(self.descp[0:find_space(self.descp)], True , (0,0,0)) , (self.x + 250 , self.y + 40))
                    screen.blit((pygame.font.SysFont("Oswald" , 20)).render(self.descp[find_space(self.descp):len(self.descp)], True , (0,0,0)) , (self.x + 250 , self.y + 60))
                else:
                    screen.blit((pygame.font.SysFont("Oswald" , 20)).render(self.descp, True , (0,0,0)) , (self.x + 250 , self.y + 40))

                    
        else:
            pygame.draw.rect(screen, self.button_col, button_rect)

        text_img = button_font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        

        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 10))
        pygame.draw.line(screen , (0,0,0) , (self.x , self.y) , (self.x + 120, self.y), width = 2)
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (self.x, self.y + 40), width=2)
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y + 40), (self.x + 120, self.y + 40), width=2)
        pygame.draw.line(screen, (0, 0, 0), (self.x + 120, self.y), (self.x + 120, self.y + 40), width=2)
        if level < self.level_req and self.text not in shop_things:
            not_unlocked = pygame.Rect(403 , self.y - 10, 400 , 60)
            pygame.draw.rect(screen ,(0,20,0),not_unlocked )
            pygame.draw.line(screen, (255,255,255), (403, self.y - 10) , (799, self.y - 10), width = 3)
            pygame.draw.line(screen, (255,255,255), (403, self.y - 10) , (403, self.y + 50), width = 3)
            pygame.draw.line(screen, (255,255,255), (799, self.y - 10) , (799, self.y + 50), width = 3)
            pygame.draw.line(screen, (255,255,255), (403, self.y + 50) , (799, self.y + 50), width = 3)
            
            screen.blit(button_font.render('Unlocked at level {0}'.format(self.level_req), True , (255,0,0)), (500 , self.y))
        if self.text in shop_things and shop_level < self.level_req:
            not_unlocked = pygame.Rect(403 , self.y - 10, 400 , 60)
            pygame.draw.rect(screen ,(0,20,0),not_unlocked )
            screen.blit(button_font.render('Unlocked at shop level {0}'.format(self.level_req), True , (255,0,0)), (500 , self.y))
            pygame.draw.line(screen, (255,255,255), (403, self.y - 10) , (799, self.y - 10), width = 3)
            pygame.draw.line(screen, (255,255,255), (403, self.y - 10) , (403, self.y + 50), width = 3)
            pygame.draw.line(screen, (255,255,255), (799, self.y - 10) , (799, self.y + 50), width = 3)
            pygame.draw.line(screen, (255,255,255), (403, self.y + 50) , (799, self.y + 50), width = 3)

 
        
        return action
multiply = button(410, 20, 'Multiplier', 100, 0, "Multiplies income")
earn = button(410 ,80 , 'Income' , 50, 0, "Amount per click")
auto = button(410 , 140 , 'Autoclick' , 500,0 , "Auto-earns money")
extra_xp = button(410 , 200 , '+XP' , 200,0, "More xp per click")
lucky = button(410 , 260 , 'Luck' , 300,3, "Chance for more money")
shop = button(410 , 320 , "Shop" , 5000, 7 , "Upgrades shop")
open_shop = button(20 , height / 2, "Shop", 0, 0, '')
better_upgrade = button(410, 20, 'Upgrade+1', 50000 , 0 , "+1 upgrade level")
stats = button(20 , height / 2 - 50, "Stats", 0, 0 , '')
rainbow = button(410 , 80 , "Rainbow" , 60000, 0 , "rainbow")
assistant = button(410 , 140 , "Assistant" , 5000, 3 , "Helps to click")
merge = button(540, height / 2 - 20, "Merge" , 0, 0, "")
lubricant = button(410 , 380, "Lubricant", 6000, 10, "Smooth button, +2 income")
better_assistant = button(410 , 200, "Better help", 10000, 15, "Assistant level +1")
faster_fingers = button(410, 440, "Fast Fingers", 10000, 17, "XP x2")
def simple_money(num):
    num = str(num)
    if len(num) == 4:
        return '{0}.{1}{2}K'.format(num[0] , num[1] , num[2])
    elif len(num) == 5:
        return '{0}{1}.{2}K'.format(num[0] , num[1] , num[2])
    elif len(num) == 6:
        return '{0}{1}{2}K'.format(num[0] , num[1] , num[2])
    elif len(num) == 7:
        return '{0}.{1}{2}M'.format(num[0] , num[1] , num[2])
    elif len(num) == 8:
        return '{0}{1}.{2}M'.format(num[0] , num[1] , num[2])
    elif len(num) == 9:
        return '{0}{1}{2}M'.format(num[0] , num[1] , num[2])
    elif len(num) == 10:
        return '{0}.{1}{2}B'.format(num[0] , num[1] , num[2])
    elif len(num) == 11:
        return '{0}{1}.{2}B'.format(num[0] , num[1] , num[2])
    else:
        return num
        

        
        
def autoclik():
    global money
    global autoclick
    money += autoclick + sum(assistant_list)
    time.sleep(0.1)
def find_centre(rect):
    global x
    global y
    x = (rect.left + rect.right) / 2
    y = (rect.top + rect.bottom) / 2
    return x
    return y
def check_if_can_buy(cost):
    if money >= cost:
        return blue
    else:
        return red


def show_cost(cost, x, y, colour):
    displayed_cost = button_font.render(str(cost), True, colour)
    screen.blit(displayed_cost, (x, y + 10))

def draw_everything():
    global shop_menu , menu,  open_shop ,shop_level,shop_cost, shop_open, shop, xp_level, multiply_level, autoclick_level
    global show_stats, rainbow, rainbow_cost, rainbow_level
    global earn_level, better_upgrade, show_menu
    global luck_level, better_upgrade_cost, assistant , assistant_cost, assistant_level
    global luck_cost, better_upgrade_level, show_merge_menu , assistant_list, merge_find
    global lucky, merge, lubricant, lubricant_cost, lubricant_level
    global xp_gain, better_assistant, better_assistant_cost, better_assistant_level
    global xp, assistant_colour_list
    global xp_cost, fast_fingers, fast_fingers_cost, fast_fingers_level
    global auto
    global auto_cost
    global money
    global income
    global multiplier
    global multiply_cost
    global earn_cost
    global multiply
    global earn
    global autoclick
    pygame.draw.rect(screen, player_colour, player)
    for i in range(len(assistant_list)):
        pygame.draw.circle(screen , (assistant_colour_list[assistant_list[i] - 1]),(width / 2 , height / 2) ,i * 10 + assistant_list[i] * 5 + 5 , width = assistant_list[i] * 2)
    if show_merge_menu == True:
        pygame.draw.rect(screen , (255,100,100), menu)
        pygame.draw.line(screen , (0, 0, 0), (400, 0), (400, height), width = 5)
        pygame.draw.line(screen, (0, 0, 0), (400, 2), (width , 2), width = 5)
        pygame.draw.line(screen, (0, 0, 0), (400, height - 3), (width , height - 3), width = 5)
        screen.blit(font.render("merge level " + str(merge_find) + " assistants", True, (0,0,0)), (420, height / 2 - 200))
        screen.blit(font.render("Use up and down arrow", True, (0,0,0)), (420, height / 2 + 100))
        screen.blit(font.render("to change merge level", True, (0,0,0)), (420, height / 2 + 140))
        if merge.draw_button():
            if assistant_list.count(merge_find) > 10:
                for i in range(10):
                    assistant_list.remove(merge_find)
            else:
                screen.blit(font.render("Not Enough Assistants", True, (255,0,0)), (400, height / 2 ))
        
    if show_stats == True:
        pygame.draw.rect(screen , (0,255,0) , pygame.Rect( 200 , 150,400 , 300))
        pygame.draw.line(screen , (0,0,0), (200,150) , (200 , 450), width = 5)
        pygame.draw.line(screen , (0,0,0), (200,150) , (600 , 150), width = 5)
        pygame.draw.line(screen , (0,0,0), (600,150) , (600 , 450), width = 5)
        pygame.draw.line(screen , (0,0,0), (200,450) , (600 , 450), width = 5)
        show_cost("Clicks: " + str(clicks) , 210 , 160 , (0,0,0))
        show_cost("Multiplier: " + str(multiplier) , 210 , 190 , (0,0,0))
        show_cost("Income: " + str(income) , 210 , 220 , (0,0,0))
        show_cost("Luck: " + str(luck_level) + "%" , 210 , 250 , (0,0,0))

    if shop_open == True:
        pygame.draw.rect(screen , (0,255,255), shop_menu)
        pygame.draw.line(screen , (0, 0, 0), (400, 0), (400, height), width = 5)
        pygame.draw.line(screen, (0, 0, 0), (400, 2), (width , 2), width = 5)
        pygame.draw.line(screen, (0, 0, 0), (400, height - 3), (width , height - 3), width = 5)
        show_cost('Level ' + str(better_upgrade_level), 600, 20, (0,0,255))
        show_cost('Level ' + str(rainbow_level), 600, 80, (0,0,255))
        show_cost('Level ' + str(assistant_level), 600, 140, (0,0,255))
        show_cost('Level ' + str(better_assistant_level), 600, 200, (0,0,255))
        show_cost(simple_money(better_upgrade_cost), 540, 20 , check_if_can_buy(better_upgrade_cost))
        show_cost(simple_money(rainbow_cost), 540, 80 , check_if_can_buy(rainbow_cost))
        show_cost(simple_money(assistant_cost), 540, 140 , check_if_can_buy(better_upgrade_cost))
        show_cost(simple_money(better_assistant_cost), 540, 200 , check_if_can_buy(better_assistant_cost))
        show_cost(simple_money(temp_income_cost), 540, 200 , check_if_can_buy(temp_income_cost))
        
        if better_upgrade.draw_button():
            if check_if_can_buy(better_upgrade_cost) == blue:
                money -= better_upgrade_cost
                better_upgrade_level += 1
                better_upgrade_cost = better_upgrade_cost * 5
        if rainbow.draw_button():
            if check_if_can_buy(rainbow_cost) == blue and rainbow_level < 1:
                money -= rainbow-cost
                rainbow_level += 1
            if rainbow_level == 1:
                rainbow_level = 'MAX'
        if assistant.draw_button() and show_level >= 3:
            if check_if_can_buy(assistant_cost) == blue:
                if len(assistant_list) < 20:
                    assistant_list.append(better_assistant_level)
                    money -= assistant_cost
                    assistant_level += 1
                    assistant_cost += int(assistant_cost / 2)
                else:
                    screen.blit(font.render("Max reached" , True , (255,0,0)), (width - 350 , height - 50))
        if better_assistant.draw_button() and shop_level >= 15:
            if check_if_can_buy(better_assistant_cost) == blue:
                money -= better_assistant_cost
                better_assistant_level += 1
                better_assistant_cost = better_assistant_cost * 7
                for i in range(len(assistant_list)):
                    if assistant_list[i] == better_assistant_level - 1:
                        assistant_list[i] = better_assistant_level

                
                
                
        
        
    if show_menu == True:
        pygame.draw.rect(screen, (0, 200, 100), menu)
        show_cost('Level ' + str(multiply_level), 640, 20, (0,0,255))
        show_cost('Level ' + str(earn_level) ,640,80, (0,0,255))
        show_cost('Level ' + str(autoclick_level), 640, 140, (0,0,255))
        show_cost('Level ' + str(xp_level), 640, 200, (0,0,255))
        show_cost('Level ' + str(luck_level), 640, 260, (0,0,255))
        show_cost('Level ' + str(shop_level), 640, 320, (0,0,255))
        show_cost('Level ' + str(lubricant_level), 640 , 380 , (0,0,255))
        show_cost('Level ' + str(fast_fingers_level), 640 , 440 , (0,0,255))
        show_cost(simple_money(multiply_cost), 560, 20, check_if_can_buy(multiply_cost))
        show_cost(simple_money(earn_cost) , 560 , 80 , check_if_can_buy(earn_cost))
        show_cost(simple_money(int(auto_cost)), 560 , 140, check_if_can_buy(auto_cost))
        show_cost(simple_money(xp_cost) , 560 , 200 ,check_if_can_buy(xp_cost))
        show_cost(simple_money(luck_cost) , 560 , 260 , check_if_can_buy(luck_cost))
        show_cost(simple_money(shop_cost) , 560 , 320 , check_if_can_buy(shop_cost))
        show_cost(simple_money(lubricant_cost), 560 , 380, check_if_can_buy(lubricant_cost))
        show_cost(simple_money(fast_fingers_cost), 560 , 440, check_if_can_buy(fast_fingers_cost))
        if multiply.draw_button():
            if check_if_can_buy(multiply_cost) == red:
                pass
            else:
                multiplier += 1 * better_upgrade_level
                money -= multiply_cost
                multiply_cost = multiply_cost * multiply_cost
                multiply_level += better_upgrade_level
        if earn.draw_button():
            if check_if_can_buy(earn_cost) == blue:
                income += better_upgrade_level
                money -= earn_cost
                earn_cost = earn_cost * 2
                earn_level += better_upgrade_level
        if auto.draw_button():
            if check_if_can_buy(auto_cost)==blue:
                autoclick += better_upgrade_level * 0.2
                money -= auto_cost
                auto_cost = auto_cost * 2.5
                autoclick_level += better_upgrade_level
        if extra_xp.draw_button():
            if check_if_can_buy(xp_cost) == blue:
                xp_gain += better_upgrade_level
                money -= xp_cost
                xp_cost = int(xp_cost * 2.5)
                xp_level += better_upgrade_level
        if lucky.draw_button() and level >= 3 and luck_level < 100:
            if check_if_can_buy(luck_cost) == blue:
                money -= luck_cost
                luck_level += better_upgrade_level
                luck_cost = luck_cost * 3
        elif luck_level >= 100:
            luck_level = 'MAX'
        if shop.draw_button() and level >= 7:
            if check_if_can_buy(shop_cost) == blue:
                money -= shop_cost
                shop_level += better_upgrade_level
                shop_cost = shop_cost * 2
        if lubricant.draw_button() and level >= 10:
            if check_if_can_buy(lubricant_cost) == blue:
                money -= lubricant_cost
                lubricant_level += better_upgrade_level
                lubricant_cost = lubricant_cost * 3
                income += 2
        if faster_fingers.draw_button() and level >= 15:
            if check_if_can_buy(fast_fingers_cost) == blue:
                money -= fast_fingers_cost
                fast_fingers_level += better_upgrade_level
                fast_fingers_cost = fast_fingers_cost * 2
                xp_gain = xp_gain * 2
                
                
        pygame.draw.line(screen , (0, 0, 0), (400, 0), (400, height), width = 5)
        pygame.draw.line(screen, (0, 0, 0), (400, 2), (width , 2), width = 5)
        pygame.draw.line(screen, (0, 0, 0), (400, height - 3), (width , height - 3), width = 5)
    if shop_level >= 1:
        if open_shop.draw_button():
            shop_open = not shop_open
            show_menu = False
    if stats.draw_button():
        show_stats = not show_stats
        show_menu = False
        shop_open = False
        
            
                
        
        
                    
                
        
    pygame.draw.rect(screen , (255,25,255) , pygame.Rect(0, 0, 225 , 40))
    pygame.draw.line(screen , (0,0,0) , (0 , 0) , (225,0), width = 5)
    pygame.draw.line(screen, (0, 0, 0), (0,0), (0,40), width=5)
    pygame.draw.line(screen, (0, 0, 0), (0,40), (225,40), width=5)
    pygame.draw.line(screen, (0, 0, 0), (225,0), (225,40), width=5)
    screen.blit(displayed_money, (10, 10))
    pygame.display.update()



pygame.display.set_caption('gaem!')
while True:
    if tutorial == True:
        do_tutorial(page)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    page += 1
        if page == 6:
            tutorial = False
        continue
    player = pygame.Rect((width / 2) - 16, (height / 2) - 16, 32, 32)
    if rainbow_level != 1:
        player_colour = (255,255,255)
    displayed_xp = button_font.render("{0}/{1}XP".format(xp , max_xp), True, (200,120,193))
    displayed_xp_rect = displayed_xp.get_rect(center=(width / 2, 60))
    displayed_money = font.render("Money: " + simple_money(math.floor(money)), True, (0, 0, 0))
    clock.tick(60)  # sets fixed fps
    screen.fill((50, 50, 50))
    screen.blit(font.render("Click space to earn money" , True, (255,255,255)) , (0 , height - 30))
    if shop_level >= 3:
        screen.blit(font.render("Press M to merge assistants", True, (255,255,255)), (0, height - 60))
    pygame.draw.rect(screen, (255,255,255), xp_bar_bg)
    xp_bar = pygame.Rect(250 , 5 , 300 * (xp / max_xp) , 30)
    pygame.draw.line(screen, (0,0,0) , (245 , 1) , (555, 1), width  = 3)
    pygame.draw.line(screen, (0,0,0) , (245 , 0) , (245 , 40) , width = 3)
    pygame.draw.line(screen, (0,0,0) , (555 , 0) , (555, 40), width  = 3)
    pygame.draw.line(screen, (0,0,0) , (245 , 40) , (555 , 40) , width = 3)
    pygame.draw.rect(screen , (0,100,255) , xp_bar)
    screen.blit(displayed_xp , displayed_xp_rect)
    displayed_level = button_font.render("Level {0}".format(level), True, (0,0,0))
    displayed_level_rect = displayed_level.get_rect(center=(width / 2, 25))
    screen.blit(displayed_level , displayed_level_rect)
    screen.blit(button_font.render('Press B to upgrade' , True , (255,0,0)) , (580,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                money += income * multiplier
                xp += xp_gain
                player = pygame.Rect((width / 2) - 20, (height / 2) - 20, 40, 40)
                if rainbow_level == 1:
                    if rainbow_index == 7:
                        rainbow_index = 0
                    player_colour = rainbow_list[rainbow_index]
                    rainbow_index += 1
                else:
                    player_colour = (255,0,0)
                clicks += 1
                if random.randint(0, 100 - luck_level) == 0:
                    money += income * 100
            if event.key == pygame.K_b:
                show_menu = not show_menu
                shop_open = False
                show_merge_menu = False
            if event.key == pygame.K_m and shop_level >= 3:
                show_merge_menu = not show_merge_menu
                show_menu = False
                shop_open = False
            if show_merge_menu == True:
                if event.key == pygame.K_UP:
                    if merge_find < max(assistant_list):
                        merge_find += 1
                if event.key == pygame.K_DOWN:
                    if merge_find > 0:
                        merge_find -= 1
                    
                
                
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if xp >= max_xp:
        level += 1
        xp = 0
        max_xp = max_xp * 3
    autoclik()
    
    draw_everything()
