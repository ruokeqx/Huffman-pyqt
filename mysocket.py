import socket


class MySocket:

    def __init__(self):
        self.ip = '192.168.136.18'
        # self.ip = '127.0.0.1'
        self.port = 11111

    def sendfile(self, path):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.ip, self.port))
        encodeddata = open(path+"_encoded.bin", 'rb').read()
        client.send(encodeddata)
        reverse_mapping = open(path+'_reverse_mapping', 'r').read()
        serverstatus = client.recv(1)
        client.send(reverse_mapping.encode('utf-8')) if serverstatus else print("send encodeddata error")
        serverstatus = client.recv(1)
        client.send(b'1') if serverstatus else print("send reverse_mapping error")
        client.close()

    def recvfile(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.ip, self.port))
        server.listen(5)
        while True:
            connobj, addr = server.accept()
            while True:
                # encoded file
                self.data = connobj.recv(1024)
                if self.data != '':
                    # print(data)
                    self.saveasfile()
                    connobj.send(b'1')
                # reverse_mapping
                self.data = connobj.recv(1024)
                if self.data != '':
                    connobj.send(b'1')
                    break
            clientstatus = connobj.recv(1)
            if clientstatus == b'1':
                connobj.close()
                return self.data

    def saveasfile(self):
        filename = "huffman_test.bin"
        f = open(filename, 'wb')
        f.write(self.data)
        f.close()


if __name__ == '__main__':
    conn = MySocket()
    conn.recvfile()
