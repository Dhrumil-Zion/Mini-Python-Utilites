import pywhatkit as kt
import getpass as gp

p_num=gp.getpass(prompt="PhoneNumber with +91xxxxxxxxxx :",stream=None)
msg ="Hello bro"
kt.sendwhatmsg(p_num,msg,11,48)   ## 2nd and 3rd argument is hr and min you want to share msg at.

