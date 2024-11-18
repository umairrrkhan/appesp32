from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
import random

class DiceGame(BoxLayout):
    def __init__(self, **kwargs):
        super(DiceGame, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.label = Label(text="Roll the Dice!", font_size='24sp')
        self.add_widget(self.label)

        self.roll_button = Button(text="Roll Dice", font_size='18sp')
        self.roll_button.bind(on_press=self.roll_dice)
        self.add_widget(self.roll_button)

        self.result_label = Label(text="", font_size='48sp')
        self.add_widget(self.result_label)

        self.dice_image1 = Image()
        self.add_widget(self.dice_image1)

        self.dice_image2 = Image()
        self.add_widget(self.dice_image2)

    def roll_dice(self, instance):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

        self.result_label.text = f"{die1} + {die2} = {die1 + die2}"
        self.update_dice_image(die1, die2)

    def update_dice_image(self, die1, die2):
        self.dice_image1.source = f'dice_{die1}.png'
        self.dice_image2.source = f'dice_{die2}.png'
        self.dice_image1.reload()
        self.dice_image2.reload()

class DiceApp(App):
    def build(self):
        return DiceGame()

if __name__ == '__main__':
    DiceApp().run()