'''
PICASSO PROJECT
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''

import arcade
arcade.open_window(500, 500, "Picasso Project")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

arcade.draw_arc_filled(250, 100, 180, 195, (255, 211, 0), 0, 180)
arcade.draw_rectangle_filled(400, 185, 20, 230, (255, 211, 0), 200)
arcade.draw_ellipse_filled(390, 300, 30, 75, (255, 211, 0), 120)
arcade.draw_ellipse_filled(100, 300, 30, 75, (255, 211, 0), 225)


arcade.finish_render()
arcade.run()


