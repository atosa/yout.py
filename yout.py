#!/usr/bin/env python3
import pafy
print("""


 ____  ____   __| _/___________  \_ |__ ___.__. _____ _/  |_  ____  ___________    
_/ ___\/  _ \ / __ |/ __ \_  __ \  | __ <   |  | \__  \\   __\/  _ \/  ___/\__  \   
\  \__(  <_> ) /_/ \  ___/|  | \/  | \_\ \___  |  / __ \|  | (  <_> )___ \  / __ \_ 
 \___  >____/\____ |\___  >__|     |___  / ____| (____  /__|  \____/____  >(____  / 
     \/           \/    \/             \/\/           \/                \/      \/  


""")
url=input("enter your url : ")
v = pafy.new(url)
s = v.getbest()
print("Size is %s" % s.get_filesize())
print(v.title)
print(v.duration)
print(v.rating)
print(v.author)
print(v.length)
print(v.thumb)
print(v.videoid)
print(v.viewcount)
down=v.videostreams
filename = s.download()
