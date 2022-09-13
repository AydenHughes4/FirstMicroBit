def on_button_pressed_a():
    global x
    x = (a * x + b) % c
    basic.show_number(x)
input.on_button_pressed(Button.A, on_button_pressed_a)

x = 12
a = 14
b = 16
c = 19