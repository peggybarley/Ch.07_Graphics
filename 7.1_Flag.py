'''
FLAG PROJECT
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red:#BF0A30 and blue:#002868
Title the window, "The Stars and Stripes"
I used a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
'''
import arcade
ya = 260

arcade.open_window(494, 266, "The Stars and Stripes")
arcade.set_background_color((255, 255, 255))
arcade.start_render()

for red_stripes in range(7):
    arcade.draw_rectangle_filled()
    #arcade.draw_line(0, ya, 494, ya, (191,10,48), 20)
    #ya -= 20


arcade.finish_render()
arcade.run()