#had to generate this as i didn't learn this in class, but is pretty eeasy
import datetime

current_datetime = datetime.datetime.now()

formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

print(f"Current Date and Time: {formatted_datetime}")
