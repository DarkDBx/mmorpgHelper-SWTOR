from logging import debug, info, error
from random import uniform
from time import sleep
from pydirectinput import keyDown, keyUp, press

from helper import image_helper, timer_helper, config_helper
from helper.timer_helper import TIMER_STOPPED


SKILLPATH = ".\\assets\\skills\\"


cfg = config_helper.read_config()
class_var = cfg['class']
comboKey = cfg['comboKey']
skill1 = cfg['skill01']
skill2 = cfg['skill02']
skill3 = cfg['skill03']
skill4 = cfg['skill04']
skill5 = cfg['skill05']
skill6 = cfg['skill06']
skill7 = cfg['skill07']
skill8 = cfg['skill08']
skill9 = cfg['skill09']
skill10 = cfg['skill10']
skill11 = cfg['skill11']
skill12 = cfg['skill12']

timer1 = timer_helper.TimerHelper('timer1')


def press_combo(key):
    keyDown(comboKey)
    press(key)
    keyUp(comboKey)


def rotation():
    """set up the skill rotation for a specific class, by the config value"""
    if class_var == 'Commando':
        combat_rotation('comm')
    elif class_var == 'Assasin':
        combat_rotation('assa')
    elif class_var == 'Juggernaut':
        combat_rotation('jugg')
    else:
        error('No vaible class')


def combat_rotation(value):
    # target check
    if image_helper.pixel_matches_color(1298,907, 225,73,72): # or image_helper.line_detection('mob') != False:
        # class check
        if value == 'comm':
            debug('Use commando skillset')
            pass
        elif value == 'assa':
            debug('Use assasin skillset')
            pass
        elif value == 'jugg':
            debug('Use juggernaut skillset')
            # heal skill check
            if image_helper.locate_needle(SKILLPATH+value+'\\s10.png', conf=0.99) and not image_helper.pixel_matches_color(770,908, 170,0,0): # below 50% health
                press_combo(skill10)
                info('Execute ability shift+10')
            # class skill checks
            elif image_helper.locate_needle(SKILLPATH+value+'\\s05.png', conf=0.99):
                press_combo(skill5)
                info('Execute ability shift+5')
            elif image_helper.locate_needle(SKILLPATH+value+'\\s04.png', conf=0.99):
                press_combo(skill4)
                info('Execute ability shift+4')
            elif image_helper.locate_needle(SKILLPATH+value+'\\s02.png', conf=0.99):
                press_combo(skill2)
                info('Execute ability shift+2')
            elif image_helper.locate_needle(SKILLPATH+value+'\\12.png', conf=0.99):
                press(skill12)
                info('Execute ability 12')
            elif image_helper.locate_needle(SKILLPATH+value+'\\11.png', conf=0.99) and timer1.GetTimerState() == TIMER_STOPPED and image_helper.pixel_matches_color(678,923, 172,110,38): # 3 rage
                timer1.StartTimer(6)
                press(skill11)
                info('Execute ability 11')
            elif image_helper.locate_needle(SKILLPATH+value+'\\10.png', conf=0.99) and image_helper.pixel_matches_color(655,923, 172,110,38): # 4 rage
                press(skill10)
                info('Execute ability 10')
            elif image_helper.locate_needle(SKILLPATH+value+'\\09.png', conf=0.99):
                press(skill9)
                info('Execute ability 9')
            elif image_helper.locate_needle(SKILLPATH+value+'\\08.png', conf=0.99) and image_helper.pixel_matches_color(678,923, 172,110,38): # 3 rage
                press(skill8)
                info('Execute ability 8')
            elif image_helper.locate_needle(SKILLPATH+value+'\\07.png', conf=0.99) and image_helper.pixel_matches_color(703,924, 210,153,34): # 2 rage
                press(skill7)
                info('Execute ability 7')
            elif image_helper.locate_needle(SKILLPATH+value+'\\06.png', conf=0.99) and image_helper.pixel_matches_color(678,923, 172,110,38): # 3 rage
                press(skill6)
                info('Execute ability 6')
            elif image_helper.locate_needle(SKILLPATH+value+'\\05.png', conf=0.99):
                press(skill5)
                info('Execute ability 5')
            elif image_helper.locate_needle(SKILLPATH+value+'\\04.png', conf=0.99) and image_helper.pixel_matches_color(703,924, 210,153,34): # 2 rage
                press(skill4)
                info('Execute ability 4')
            elif image_helper.locate_needle(SKILLPATH+value+'\\03.png', conf=0.99):
                press(skill3)
                info('Execute ability 3')
            elif image_helper.locate_needle(SKILLPATH+value+'\\02.png', conf=0.99) and image_helper.pixel_matches_color(678,923, 172,110,38): # 3 rage
                press(skill2)
                info('Execute ability 2')
            elif image_helper.locate_needle(SKILLPATH+value+'\\01.png', conf=0.99):
                press(skill1)
                info('Execute ability 1')
            
            sleep(uniform(1.06, 1.11))

