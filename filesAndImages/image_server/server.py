import socket
from PIL import Image
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((socket.gethostname(),4571))
    s.listen(5)
    print('Server is up. Listening for connections..\n')

    client,address= s.accept()
    print('Connection to ',address,' established\n')
    print('Client object: ',client,'\n')
    
    with open('./OddFutureSansOcean.jpg','rb') as image_file:
        image_batch=image_file.read(40960)
        while(image_batch):
            client.send(image_batch)
            image_batch=image_file.read(40960)
            print('Batch sent')
        print('Image sent succesfully')