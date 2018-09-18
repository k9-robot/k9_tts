#!/usr/bin/env python

# Import speech engine
import pyttsx3

# Import ROS
import rospy
from std_msgs.msg import String
from k9_tts.msg import tts
from k9_tts.srv import Say

class k9_tts:
    def __init__(self):
        self.engine = pyttsx3.init()
        rospy.init_node("k9_tts")
        service = rospy.Service('k9_say', Say, self.k9_tts_service)
        
    def k9_tts_service(self, req):
        self.engine.say(req.speech.text)
        rospy.loginfo("K9 Says: %s" % (req.speech.text))
        self.engine.runAndWait()
        return True


if __name__ == "__main__":
    try:
        k9_tts()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass