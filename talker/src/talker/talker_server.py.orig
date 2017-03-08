#! /usr/bin/env python

import roslib
roslib.load_manifest('talker')
import rospy
import actionlib
import subprocess

from talker.msg import SayAction, SayResult

class SayServer(object):
    def __init__(self):
        self.say_server = actionlib.SimpleActionServer('say', SayAction, self.say, False)
        self.say_server.start()

    def say(self, goal):
        rospy.loginfo('saying "{0}"'.format(goal.text))
        r = rospy.Rate(1)
        try:
            proc = subprocess.Popen(['aoss', 'swift', '"{0}"'.format(goal.text)])

            while proc.poll() == None:
                if self.say_server.is_preempt_requested():
                    proc.terminate()
                    rospy.loginfo('canceling say request...')
                    self.say_server.set_preempted(SayResult(False))
                    break
                r.sleep()

            if proc.returncode == 0:
                self.say_server.set_succeeded(SayResult(True))

        except OSError:
            rospy.logerr('Unable to speak. Make sure "swift" and "alsa-oss" are installed.')
            self.say_server.set_aborted(SayResult(False))


if __name__ == '__main__':
    rospy.init_node('talker')
    say_server = SayServer()
    rospy.spin()
