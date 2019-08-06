from kivy.app import App
from logic.paint import PaintWidget


class PaintApp(App):

    def build(self):
        return PaintWidget()


if __name__ == '__main__':
    PaintApp().run()
