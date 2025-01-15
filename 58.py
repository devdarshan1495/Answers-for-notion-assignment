#had to chatGPT this because i haven't learnt this yet, sorry sir
import logging


logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


logging.info("This is an informational message.")
logging.error("This is an error message.")
logging.warning("This is a warning message.")

print("Logs have been written to app.log.")
