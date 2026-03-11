from AutoI.Actions.Scroll import Scroll
import time

time_1 = time.time()
scroll = Scroll("..\\Images\\Preamble_start_scroll.png", "..\\Images\\end_conditions.png")
scroll.scroll_to_point(-300)
time_2 = time.time()
diff_time = time_2 - time_1
print(diff_time)
