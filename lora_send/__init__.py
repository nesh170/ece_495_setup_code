from network import LoRa
import socket

counter = 0;
lora = LoRa(mode = LoRa.LORA, power_mode = LoRa.ALWAYS_ON)

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW);
print(s)
s.setblocking(False);

while(True):
    if(counter %30000 == 0):
        s.send(bytes([0x01, 0x02, 0x03]))
        print(s.recv(64))
        print(str(counter) + "lol\n");
    counter = counter + 1;
   
