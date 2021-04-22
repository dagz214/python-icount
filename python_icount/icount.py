"""
File: icount.py
--------------
Home to the main icount service object.

"""

import os
import requests
import yaml
import json

class Icount:
    """
    Icount    

    """
    BASE_URL='https://api.icount.co.il/api/v3.php/'

    yaml_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__),
        "../",
        "authentication.yaml"))
    with open(yaml_path, 'r') as f:
        stream=f.read()

    credentials = yaml.load(stream, yaml.SafeLoader)


    def __init__(
        self,
        cid: str = credentials['cid'],
        user: str = credentials['user'],
        password: str = credentials['password'],
        **kwargs
    ) -> None:
        """
        Icount object.

        Args:
            user (str, optional): icount username. Defaults to settings['user'].
            password (str, optional): icount password. Defaults to settings['password'].
            cid (str, optional): icount company id. Defaults to settings['cid'].
        """    

        for key, value in kwargs.items():
            print ("%s == %s" %(key, value))

        
        # merge kwargs with param dictionary, and get sid from response
        self.sid=requests.post(
            f'{Icount.BASE_URL}auth/login',
            {
                'cid':cid,
                'user':user,
                'pass':password,
                **kwargs,
            }).json()['sid']

    @classmethod
    def send_request(cls, method,endpoint, params):
        pass





    


