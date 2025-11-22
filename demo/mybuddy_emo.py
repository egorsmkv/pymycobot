from pymycobot import MyBuddyEmoticon
import time

file_path = [["/home/er/emo/look_happy.mp4", 10]]

em = MyBuddyEmoticon(file_path, loop=True)

em.start()
time.sleep(5)

# Pause
em.pause()

time.sleep(2)

# Resume playback
em.run()

# Wait for playback to finish
em.join()
