from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

Config.set("graphics", "resizable", 1)
Config.set("graphics", "width", 700)
Config.set("graphics", "height", 750)


class MainApp(App):

    def click(self, instance):
        self.label.text = 'Спасибо что нажал!'

    def grio(self, instance):
        self.label.text = 'Зачем нажал?'

    def build(self):
        but_together = BoxLayout()
        grid = GridLayout(cols=1)

        my_but = Button(text='Нажми меня СРОЧНО!', font_size=35, background_color='orange', on_press=self.click)
        names = Button(text='НЕ НАЖИМАЙ МЕНЯ', font_size=30, background_color='blue', on_press=self.grio)
        self.label = Label(text='Текст...', font_size=50)

        but_together.add_widget(my_but)
        but_together.add_widget(names)
        grid.add_widget(but_together)
        grid.add_widget(self.label)

        return grid


if __name__ == '__main__':
    MainApp().run()
