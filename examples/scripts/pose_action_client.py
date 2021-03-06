#!/usr/bin/env python
import rospy
import time
import actionlib
from geometry_msgs.msg import Pose
from examples.msg import PoseAction, PoseGoal, PoseResult, PoseFeedback

def feedback_cb(feedback):
    print('[Feedback] Current Pose:')
    print(feedback.current_pose)
    print('[Feedback] Time elapsed: %f' %(feedback.time_elapsed.to_sec()))

rospy.init_node('pose_action_client')
client = actionlib.SimpleActionClient('pose',PoseAction)
client.wait_for_server()
goal = PoseGoal
goal_pose = Pose()
goal_pose.position.x = 5
goal.goal_pose = goal_pose
client.send_goal(goal, feedback_cb=feedback_cb)
client.wait_for_result()
print('[Result] Status: %s' %(client.get_goal_status_text()))
print('[Result] Time elapsed: %f' %(client.get_result().time_elapsed.to_sec()))
