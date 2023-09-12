import arcade


LEFT_MARGIN = 100
BOTTOM_MARGIN = 100
COLUMN_SPACING = 20
ROW_SPACING = 20


arcade.open_window(400, 400, "complex loops")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

for r in range(10):
    for c in range(10):
        a = c * COLUMN_SPACING + LEFT_MARGIN
        b = r * ROW_SPACING + BOTTOM_MARGIN
        if (r + c)%2 != 0:
            arcade.draw_rectangle_filled(a, b, 10,10, arcade.color.BLUE,45)
        else:
            arcade.draw_rectangle_filled(a, b, 10,10, arcade.color.RED,45)

arcade.finish_render()

arcade.run()