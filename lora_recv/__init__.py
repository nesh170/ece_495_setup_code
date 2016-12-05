from network import LoRa
import socket

lora = LoRa(mode = LoRa.LORA,  power_mode = LoRa.ALWAYS_ON)

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False);

while(True):
    data = s.recv(64)
        
    print(data)
