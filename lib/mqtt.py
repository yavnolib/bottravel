import time
import paho.mqtt.client as mqtt
def on_connect(client,userdata,flags,rc):
	print('Connected with code'+str(rc))
	    #Sub
	client.subscribe("Test/#")
def on_message(client,userdata,msg):
	print( str(msg.payload) )
	print('ok')
class Sendler:
	def __init__(self,fromInput,fromOutput,date):
		self.fromOutput=str(fromOutput)
		print('Вывожу fromOutput')
		print(fromOutput)
		self.fromInput=str(fromInput)
		print('Вывожу fromInput')
		print(fromInput)
		self.date=str(date)
		print('Вывожу time')
		print(date)
	def send(self):
		run=1
		time.sleep(0.1)
		client=mqtt.Client()
		client.on_connect=on_connect
		client.on_message=on_message
		client.connect("<mqtt-data>")
		client.username_pw_set("<mqtt-data>")
		time.sleep(0.4)
		client.loop_start()
		while run<3:
			client.publish("Inform",self.fromInput+":"+self.fromOutput+":"+self.date)
			time.sleep(1.2)
			run+=1
			print(run)
		client.loop_stop()
		client.disconnect()
