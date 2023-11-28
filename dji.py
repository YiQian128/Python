from robomaster import *
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="ap")

ep_chassis = chassis.Chassis(ep_robot)
ep_chassis.move(z=360,z_speed=360).wait_for_completed()

ep_robot.close()