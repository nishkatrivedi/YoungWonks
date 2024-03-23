import pygame, time
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Health Account')

light_blue = (97, 182, 255)
dark_blue = (68, 131, 255)
offwhite = (252, 249, 215)


def show_text(msg, X, Y, col, fontsize):
    fontobj = pygame.font.SysFont('newyork', fontsize)
    msgobj = fontobj.render(msg, False, col)
    screen.blit(msgobj, (X, Y))


# screen1: initial menu
# screen2: create account page
# screen3: login page
# screen4: home page after login
# screen5: quiz
# screen6: workouts
# screen7: meals
# screen8: music
# screen9: yoga


class User():
    def __init__(self):
        self.screens = 1
        self.goals = ''
        self.intensity = ''
        self.type = ''
        self.score = 0


user = User()


class Button():
    def __init__(self, x, y, width, height, color, border):
        global screens
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.border = border

    def draw_button(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), self.border)

    def draw_button_text(self, text, color, fontsize):
        show_text(text, self.x + 1, self.y, color, fontsize)

    def button_sensor(self, screennumber):
        mx, my = pygame.mouse.get_pos()
        if self.x < mx < self.x + self.width and self.y < my < self.y + self.height:
            user.screens = screennumber
            return True
        return False


create_account = Button(250, 450, 500, 100, light_blue, 0)
login = Button(250, 600, 500, 100, dark_blue, 0)


class Screen1():

    def __init__(self):
        pass

    def create_account_button(self):
        create_account.draw_button()
        create_account.draw_button_text('Create Account', dark_blue, 68)

    def login_button(self):
        login.draw_button()
        login.draw_button_text('Login', light_blue, 68)

    def screen1_button_sensor(self):
        create_account.button_sensor(2)
        login.button_sensor(3)


done = Button(250, 850, 500, 75, light_blue, 0)


class Screen2():

    def __init__(self):
        self.name = input('Enter your name')
        self.age = input('Enter your age')
        self.weight = input('Enter your weight')
        self.height = input('Enter your height in inches')

    def display_info(self):
        show_text('Name: ' + str(self.name), 100, 100, dark_blue, 50)
        show_text('Age: ' + str(self.age), 100, 300, dark_blue, 50)
        show_text('Weight: ' + str(self.weight), 100, 500, dark_blue, 50)
        show_text('Height (in): ' + str(self.height), 100, 700, dark_blue, 50)

    def done_button(self):
        done.draw_button()
        done.draw_button_text('Done', offwhite, 50)

    def done_button_sensor(self):
        done.button_sensor(4)


test = Button(350, 400, 300, 50, light_blue, 0)
workouts = Button(350, 500, 300, 50, light_blue, 0)
meals = Button(350, 600, 300, 50, light_blue, 0)
music = Button(350, 700, 300, 50, light_blue, 0)
yoga = Button(350, 800, 300, 50, light_blue, 0)


class Screen4():
    def __init__(self):
        pass

    def welcome(self):
        show_text('Welcome ' + str(screen2.name) + '!', 200, 250, dark_blue, 75)

    def test_button(self):
        test.draw_button()
        test.draw_button_text('Take the Quizzes', offwhite, 30)

    def find_workouts(self):
        workouts.draw_button()
        workouts.draw_button_text('Find Workouts', offwhite, 30)

    def find_meal_ideas(self):
        meals.draw_button()
        meals.draw_button_text('Find Meal Ideas', offwhite, 30)

    def find_music(self):
        music.draw_button()
        music.draw_button_text('Find Music', offwhite, 30)

    def find_yoga_exercises(self):
        yoga.draw_button()
        yoga.draw_button_text('Yoga Exercises', offwhite, 30)

    def screen4_button_sensor(self):
        test.button_sensor(5)
        workouts.button_sensor(6)
        meals.button_sensor(7)
        music.button_sensor(8)
        yoga.button_sensor(9)


preference = Button(300, 250, 400, 100, dark_blue, 0)
activity = Button(300, 500, 400, 100, dark_blue, 0)
diet = Button(300, 750, 400, 100, dark_blue, 0)


class Screen5():
    def __init__(self):
        pass

    def preferences(self):
        preference.draw_button()
        preference.draw_button_text('Preferences', offwhite, 50)

    def activity_questions(self):
        activity.draw_button()
        activity.draw_button_text('Lifestyle', offwhite, 50)

    def diet_questions(self):
        diet.draw_button()
        diet.draw_button_text('Diet', offwhite, 50)

    def screen5_button_sensor(self):
        preference.button_sensor(10)
        activity.button_sensor(20)
        diet.button_sensor(30)


# shift down by 50


s101 = Button(25, 240, 20, 20, dark_blue, 2)
s102 = Button(25, 405, 20, 20, dark_blue, 2)
s103 = Button(25, 570, 20, 20, dark_blue, 2)
s104 = Button(25, 735, 20, 20, dark_blue, 2)

s10 = [s101, s102, s103, s104]

s111 = Button(25, 240, 20, 20, dark_blue, 2)
s112 = Button(25, 405, 20, 20, dark_blue, 2)
s113 = Button(25, 570, 20, 20, dark_blue, 2)
s114 = Button(25, 735, 20, 20, dark_blue, 2)

s11 = [s111, s112, s113]

s121 = Button(25, 240, 20, 20, dark_blue, 2)
s122 = Button(25, 405, 20, 20, dark_blue, 2)
s123 = Button(25, 570, 20, 20, dark_blue, 2)
s124 = Button(25, 735, 20, 20, dark_blue, 2)

s12 = [s121, s122, s123, 124]


class Goals():

    def __init__(self):
        pass

    def fitness_goals(self):
        show_text('What are your fitness goals?', 50, 100, dark_blue, 82)
        for s in s10:
            s.draw_button()

        show_text('Weight Loss', 75, 220, light_blue, 50)
        show_text('Muscle Toning', 75, 385, light_blue, 50)
        show_text('Improved Appearance', 75, 550, light_blue, 50)
        show_text('More Strength', 75, 715, light_blue, 50)

    def fitness_button_sensor(self, my):

        for s in s10:
            print(s, s101, s102, s103, s104)

            if s == s101:
                user.goals = 'Weight Loss'
                user.score += 4
            elif s == s102:
                user.goals = 'Muscle Toning'
                user.score += 1
            elif s == s103:
                user.goals = 'Improved Appearance'
                user.score += 2
            elif s == s104:
                user.goals = 'More Strength'
                user.score += 3
            print('s11')
        s.button_sensor(11)


class Intensity():
    def __init__(self):
        pass

    def intensity(self):
        show_text('How intense would you like your workouts to be?', 50, 100, dark_blue, 82)
        for s in s11:
            s.draw_button()

        show_text('Mild Intensity', 75, 220, light_blue, 50)
        show_text('Moderate Intensity', 75, 385, light_blue, 50)
        show_text('High Intensity', 75, 550, light_blue, 50)
        show_text('Doesnt Matter', 75, 715, light_blue, 50)

    def intensity_button_sensor(self):
        for i in s11:
            clicked = i.button_sensor(12)
            if clicked == True:
                buttonclicked = i
                break

        if clicked == True:
            user.screens = 12
            if buttonclicked == s111:
                user.intensity = 'Mild Intensity'
                user.score += 3
            elif buttonclicked == s112:
                user.intensity = 'Moderate Intensity'
                user.score += 2
            elif buttonclicked == s113:
                user.intensity = 'High Intensity'
                user.score += 1
            elif buttonclicked == s114:
                user.intensity = 'N/A'
                user.score += 2


class Type():
    def __init__(self):
        pass

    def exercise_type(self):
        show_text('What kind of workouts would you like?', 50, 100, dark_blue, 82)
        for s in s12:
            s.draw_button()

        show_text('Cardio', 75, 220, light_blue, 50)
        show_text('Pilates', 75, 385, light_blue, 50)
        show_text('Strength Training', 75, 550, light_blue, 50)
        show_text('Doesnt Matter', 75, 715, light_blue, 50)

    def exercise_type_button_sensor(self):
        for s in s12:

            if s == s121:
                user.type = 'Cardio'
                user.score += 3
            elif s == s122:
                user.type = 'Pilates'
                user.score += 2
            elif s == s123:
                user.type = 'Strength Training'
                user.score += 1
            elif s == s124:
                user.type = 'N/A'
                user.score += 2

            s.button_sensor(13)


# ,fitness_goals,exercise_type,intensity
# ,lifestyle,current exercise
# ,diet_preferences,allergies


screen1 = Screen1()
screen2 = Screen2()
screen4 = Screen4()
screen5 = Screen5()
goal = Goals()
inten = Intensity()
extype = Type()

while True:

    print(user.screens)
    print(user.goals)
    print(user.type)
    print(user.intensity)

    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        if event.type == MOUSEBUTTONDOWN:
            if user.screens == 1:
                screen1.screen1_button_sensor()
            if user.screens == 2:
                screen2.done_button_sensor()

            if user.screens == 4:
                screen4.screen4_button_sensor()
            if user.screens == 5:
                screen5.screen5_button_sensor()

            if user.screens == 10:
                mx, my = pygame.mouse.get_pos()
                goal.fitness_button_sensor(my)

            if user.screens == 11:
                inten.intensity_button_sensor()
            if user.screens == 12:
                extype.exercise_type_button_sensor()

    if user.screens == 1:
        screen.fill(offwhite)
        screen1.create_account_button()
        screen1.login_button()

    if user.screens == 2:
        screen.fill(offwhite)
        screen2.display_info()
        screen2.done_button()

    if user.screens == 3:
        pass

    if user.screens == 4:
        screen.fill(offwhite)
        screen4.welcome()
        screen4.test_button()
        screen4.find_workouts()
        screen4.find_meal_ideas()
        screen4.find_music()
        screen4.find_yoga_exercises()

    if user.screens == 5:
        screen.fill(offwhite)
        screen5.preferences()
        screen5.activity_questions()
        screen5.diet_questions()

    if user.screens == 10:
        screen.fill(offwhite)
        goal.fitness_goals()

    if user.screens == 11:
        screen.fill(offwhite)
        inten.intensity()

    if user.screens == 12:
        screen.fill(offwhite)
        extype.exercise_type()

    if user.screens == 13:
        screen.fill(light_blue)

    pygame.display.update()
