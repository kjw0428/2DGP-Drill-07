from pico2d import *
import random


# Game object class here
#1. 객체를 도출 - 추상화
#2. 속성을 도출 - 추상화
#3. 행위를 도출
#4. 클래스를 제작

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.frame = random.randint(0, 7)
        if random.choice([True, False]):
            self.image = load_image('ball21x21.png')
            self.size = 21
        else:
            self.image = load_image('ball41x41.png')
            self.size = 41

    def update(self):  # 객체의 상호 작용. 행위
        self.frame = (self.frame + 1) % 8
        self.y -= 5

    def draw(self): #객체의 상호 작용. 행위
        self.image.clip_draw(0, 0, self.size, self.size, self.x, self.y)
        pass

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):  # 객체의 상호 작용. 행위
        pass

    def draw(self): #객체의 상호 작용. 행위
        self.image.draw(400, 30)
        pass





def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False






def reset_world():
    global running
    global grass
    global boy
    global world

    global team
    world = []
    team = [Boy() for i in range(20)]
    world += team

    running = True

    grass = Grass()
    world.append(grass)
    boy = Boy()


def update_world():
    for o in world:
        o.update()

    pass


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()
    pass

open_canvas()

reset_world()

while True:
    handle_events()
    update_world() # 객체들의 상호 작용을 시뮬레이션, 계산
    render_world() # 객체들의 모습을 그린다.
    delay(0.05)

close_canvas()
