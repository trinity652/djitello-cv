from djitellopy import Tello
import time,av


# Create a class to control the tello drone
class TelloControlUtil:

    # Initialize the drone and controls
    def __init__(self):
        self.prev_flight_data = None
        self.record = False
        self.tracking = False
        self.keydown = False
        self.date_fmt = '%Y-%m-%d_%H%M%S'
        self.speed = 50
        self.drone = Tello()
        self.init_drone()
        self.init_controls()

        # container for processing the packets into frames
        self.container = av.open(self.drone.get_video_stream())
        self.vid_stream = self.container.streams.video[0]
        self.out_file = None
        self.out_stream = None
        self.out_name = None
        self.start_time = time.time()

        
    # Initialize the drone
    def init_drone(self):
        self.drone.connect()
        self.drone.streamon()

    def init_controls(self):
        self.drone.takeoff()
        self.drone.move_up(50)
        self.drone.move_down(50)
        self.drone.land()
