
from tasks import main
import logging
import time



# This script attempts to execute the 'main' function from the 'tasks' module up to five times,
# with increasing delays in case of exceptions. Any exceptions raised during execution are logged as critical errors.
if __name__ == '__main__':
    for trynum in range(1, 6):
        try:
            main()
        except Exception as e:
            
            logging.critical(e)
            time.sleep(10 * trynum)
            continue
        else:
            break



