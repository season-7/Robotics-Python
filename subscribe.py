import paho.mqtt.client as mqtt


def on_connect(client, userdata, rc):
    print "Connected with result code " + str(rc)
    client.subscribe([('left/left', 1), ('right/right', 1)])


def on_message(client, userdata, msg):
    print "Topic: ", msg.topic + "\nMessage: " + str(msg.payload)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect('iot.eclipse.org', 1883, 60)

client.loop_forever()
