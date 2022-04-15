import subprocess
import time

starttime=time.time()
while True:
    subprocess.run(['logger','Hello OS! I am a little service. Nice to meet you.'])
    time.sleep(10.0)
 

