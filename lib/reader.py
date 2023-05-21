import time
import paho.mqtt.client as mqtt

def on_connect(client,userdata,flags,rc):
	print('Connected with code'+str(rc))
	    #Sub
	client.subscribe("toglobal/#")
	client.subscribe("toglobal2/#")
def on_message(client,userdata,msg):
	print( str(msg.payload.decode("UTF-8")) )
	print(msg.topic)
	if msg.topic=="toglobal2":
		s7=open("s7.txt",mode='w')
		s7.write(msg.payload.decode("UTF-8"))
	elif msg.topic=="toglobal":
		rzd=open("rzd.txt",mode="w")
		rzd.write(msg.payload.decode("UTF-8"))
def read():
	wr=open("rzd.txt",mode='w')
	wr.close()
	ws=open('s7.txt',mode='w')
	ws.close()
	runnnn=1
	rzds=0
	s7s=0
	client=mqtt.Client()
	client.on_connect=on_connect
	client.on_message=on_message
	client.connect("<mqtt-data>")
	client.username_pw_set("<mqtt-data>")
	time.sleep(1)
	client.loop_start()		
	while runnnn==1:
		link_rzd=''
		rzd_r=open('rzd.txt',mode='r')
		for line in rzd_r:
			link_rzd+=line
			print("link_rzd"+link_rzd)
			if link_rzd!="":
				rzds=1
		time.sleep(1)
		link_s7=""
		s7_r=open('s7.txt',mode='r')
		for linee in s7_r:
			link_s7+=linee
			print("link_s7"+link_s7)
			if link_s7!="":
				s7s=1
		if (s7s==1) and (rzds==1):
			runnnn=0
			return(link_rzd+'\n'+'Авиамаршруты на данный день'+link_s7)
	

	return(link_rzd)
	print('конец')
	client.loop_stop()
	
	client.disconnect()
