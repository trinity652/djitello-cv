from djitellopy import Tello

tello = Tello()

tello.connect() # Connect to tello
tello.takeoff() 

tello.move_left(100)
tello.rotate_counter_clockwise(180) 
tello.move_forward(100)

tello.land()