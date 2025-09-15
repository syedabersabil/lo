from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):
    def build(self):
        # Main layout - vertical box layout
        main_layout = BoxLayout(orientation="vertical")
        
        # Display for results
        self.solution = TextInput(
            multiline=False, readonly=True, font_size=55, halign="right"
        )
        main_layout.add_widget(self.solution)
        
        # Buttons layout
        buttons = [
            ["C", "DEL", "√", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "(", ")"],
            ["="]
        ]
        
        # Create grid layout for buttons
        buttons_layout = GridLayout(cols=4, spacing=5)
        
        for row in buttons:
            for label in row:
                if label == "=":
                    # Span "=" button across all columns
                    btn = Button(text=label, font_size=40)
                    btn.bind(on_press=self.on_solution)
                    buttons_layout.add_widget(btn)
                elif label == "C":
                    # Clear button
                    btn = Button(text=label, font_size=40)
                    btn.bind(on_press=self.on_clear)
                    buttons_layout.add_widget(btn)
                elif label == "DEL":
                    # Delete button
                    btn = Button(text=label, font_size=40)
                    btn.bind(on_press=self.on_delete)
                    buttons_layout.add_widget(btn)
                elif label == "√":
                    # Square root button
                    btn = Button(text=label, font_size=40)
                    btn.bind(on_press=self.on_square_root)
                    buttons_layout.add_widget(btn)
                else:
                    # Number/operator buttons
                    btn = Button(text=label, font_size=40)
                    btn.bind(on_press=self.on_button_press)
                    buttons_layout.add_widget(btn)
        
        main_layout.add_widget(buttons_layout)
        return main_layout
    
    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        
        if current == "Error":
            self.solution.text = button_text
        else:
            self.solution.text = current + button_text
    
    def on_solution(self, instance):
        try:
            # Evaluate the expression
            result = str(eval(self.solution.text))
            self.solution.text = result
        except:
            self.solution.text = "Error"
    
    def on_clear(self, instance):
        self.solution.text = ""
    
    def on_delete(self, instance):
        current = self.solution.text
        if current:
            self.solution.text = current[:-1]
    
    def on_square_root(self, instance):
        try:
            # Calculate square root
            current = self.solution.text
            result = str(eval(f"({current})**0.5"))
            self.solution.text = result
        except:
            self.solution.text = "Error"


if __name__ == "__main__":
    app = CalculatorApp()
    app.run()