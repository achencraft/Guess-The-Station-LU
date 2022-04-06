import os, time, zipfile
from oscpy.client import OSCClient

class UpdateService():

    Client = OSCClient('localhost', 3000)

    def run(self):


        if not os.path.isdir('include/music'):

            ####Extraction des musiques
            time.sleep(0.5)
            self.Client.send_message(b'/step',["Extraction des musiques".encode('utf8'),],)
            with zipfile.ZipFile('include/luxtram-musiques.zip', 'r') as zip_ref:
                zip_ref.extractall('include/music')


        self.Client.send_message(b'/ok',[],)



if __name__ == '__main__':
    UpdateService().run()
    
    