import kivy
from kivy.app import App
from kivy.uix.label import Label

# Specify the Kivy version (optional)
kivy.require('2.0.0')

class HelloWorldApp(App):
    def build(self):
        # Create a label with "Hello, World!" text
        return Label(text='Hello, World!')

# Run the app
if __name__ == '__main__':
    HelloWorldApp().run()