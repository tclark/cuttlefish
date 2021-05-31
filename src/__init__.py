from server import Server

s = Server()
s.bind_to('127.0.0.1', 65432)
s.run()
