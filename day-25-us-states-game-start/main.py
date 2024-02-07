import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
correct_ans = []
data = pandas.read_csv("50_states.csv")
state_colm = data["state"].to_list()

while len(correct_ans) < 50:
    ans_state = screen.textinput(title=f"{len(correct_ans)}/50", prompt="what's another state's name?").title()

    if ans_state == "Exit":
        remaining_states = [states for states in state_colm if states not in correct_ans]
        # remaining_states = []
        # for states in state_colm:
        #     if states not in correct_ans:
        #         remaining_states.append(states)
        r_s_states = pandas.DataFrame(remaining_states)
        data.to_csv("remaining_data.csv")
        break
    if ans_state in state_colm:
        bt = turtle.Turtle()
        get_state = data[data.state == f"{ans_state}"]
        x_cod = int(get_state.x)
        y_cod = int(get_state.y)
        bt.hideturtle()
        bt.penup()
        bt.goto(x_cod, y_cod)
        bt.write(f"{ans_state}")
        correct_ans.append(ans_state)

# staes_to_learn.csv





# xcord = data[data.state == "Alaska"]
# xcord_x = xcord.x
# print(xcord_x)

















screen.exitonclick()

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)













turtle.mainloop()
