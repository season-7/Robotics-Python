import paho.mqtt.client as mqtt

# mqttc = mqtt.Client('python_pub')
# mqttc.connect('test.mosquitto.org', 1883)


def left():
    mqttc = mqtt.Client('python_pub')
    mqttc.connect('iot.eclipse.org', 1883)
    mqttc.publish('left/left', 'Left!')
    mqttc.loop(2)


def right():
    mqttc = mqtt.Client('python_pub')
    mqttc.connect('iot.eclipse.org', 1883)
    mqttc.publish('right/right', 'Right!')
    mqttc.loop(2)

def foward():
    mqttc = mqtt.Client('python_pub')
    mqttc.connect('iot.eclipse.org',1883)
    mqttc.publish('foward/foward','Foward!')
    mqttc.loop(2)

def reverse():
    mqttc = mqtt.Client('python_pub')
    mqttc.connect('iot.eclipse.org',1883)
    mqttc.publish('reverse/reverse','Reverse!')
    mqttc.loop(2)