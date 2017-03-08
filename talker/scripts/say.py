#!/usr/bin/env python

import roslib
roslib.load_manifest('talker')
import rospy
import actionlib
import talker.msg

def say(words):
    client = actionlib.SimpleActionClient('say', talker.msg.SayAction)
    client.wait_for_server(timeout=rospy.Duration(5))
    goal = talker.msg.SayGoal(text=words)
    client.send_goal(goal)
    client.wait_for_result()
    return client.get_result()



if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('words', help="words to say")
    args = parser.parse_args()
    rospy.init_node('say_cmd', anonymous=True)
    print say(args.words)


