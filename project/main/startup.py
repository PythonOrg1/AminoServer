# from project.main.server import httpServer
from  server import httpServer

def startService():
    httpServer.run()


if __name__ == '__main__':
    startService()