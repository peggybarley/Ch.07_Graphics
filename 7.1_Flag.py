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

arcade.open_window(494, 266, "The Stars and Stripes")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

for y in range(10, 251, 40):
    arcade.draw_rectangle_filled(247, y, 494, 20, (191, 10, 48))
arcade.draw_rectangle_filled(99, 190, 197.6, 140, (0, 40, 104))
y=245
for star_rows in range(9):
    if star_rows % 2 == 8:
        arcade.draw_text("* * * * * *", 15, y, arcade.color.WHITE, 20)
    y-=13
arcade.finish_render()
arcade.run()