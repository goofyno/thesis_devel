#!/usr/bin/env python
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import shape_msgs.msg 
from geometry_msgs.msg import Pose, Quaternion
from tf.transformations import quaternion_from_euler

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_test', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander("arm")

waypoints = []
# start with the current pose
waypoints.append(group.get_current_pose().pose)

pose_target = Pose()
robot.get_current_state
rospy.sleep(1)

pose_target.orientation = Quaternion(*quaternion_from_euler(3.1416, 0.0, -1.5708))
pose_target.position.x = -0.4
pose_target.position.y = -0.5
pose_target.position.z = 1.3
waypoints.append(copy.deepcopy(pose_target))

pose_target.orientation = Quaternion(*quaternion_from_euler(0.0, 0.0, -1.5708))
pose_target.position.x = 0.4
pose_target.position.y = -0.5
pose_target.position.z = 1.15
waypoints.append(copy.deepcopy(pose_target))

(plan3, fraction) = group.compute_cartesian_path(
                             waypoints,   # waypoints to follow
                             0.01,        # eef_step
                             0.0)         # jump_threshold



moveit_commander.roscpp_shutdown()

