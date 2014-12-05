

from kivy.uix.floatlayout import FloatLayout


class Orgboat(FloatLayout):
     def __init__(self, **kwargs):
         super(Orgboat, self).__init__(**kwargs)
         
         
         
if __name__ == '__main__':
    from kivy.base import runTouchApp
    
    runTouchApp(Orgboat())
