import serial ,time


class pulse:
    # ser=0
    reset=False
    
    def connect (port, label10 ):
        try:
            pulse.ser=serial.Serial(port, 115200, timeout=.1)
            label10.setText ("*** Connected ***")
            return (True)
        except:
            label10.setText ("!!! Not Connected !!!")
            return (True)



    def getAvaPorts():
        ports = serial.tools.list_ports.comports(include_links=False)
        res=list()
        for port in ports :
            res.append(port.device)
        return (res)

    def startRec(timer, timelabel):
        pulse.finish=False
        try:
            timer=int(timer)
        except:
            print("!!! Error : No time set")
            exit()
        data=list()
        reftime=int(time.time())
        pulse.dectime=0
        while( (pulse.dectime < timer) ):
            pulse.dectime=int(time.time())-reftime 
            l=pulse.ser.readline()
            if l:
                print(str(l)[3:-6])
                data.append((str(l)[3:-6]+"\n"))
            time.sleep(0.040)
        timelabel.setText("finished")
        pulse.finish=False
        return (data)


    def save(data,path):
        with open(path, 'w+') as wfile:
	        wfile.writelines( data )
        print ("....Saved")


