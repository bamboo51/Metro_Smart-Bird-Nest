import threading
import time
from motion_sensor import motion_detection
from web_server import run_flask
from light_sensor import monitor_light_sensor

try:
    motion_thread = threading.Thread(target=motion_detection)
    motion_thread.daemon = True # ensure thread exits when main program does
    motion_thread.start()

    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    light_sensor_thread = threading.Thread(target=monitor_light_sensor)
    light_sensor_thread.daemon = True
    light_sensor_thread.start()

    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting program.")
finally:
    from motion_sensor import stop_all
    stop_all()
    print("Program exited.")