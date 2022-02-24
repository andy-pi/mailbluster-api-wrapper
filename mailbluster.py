import requests
import hashlib

class Mailbluster():

    def __init__(self, api_key):
        '''
        Sets the API key for the class instance
        '''
        self.api_key = api_key
        self.base_url = 'https://api.mailbluster.com/api/'

    def __perform_request(self, endpoint_url, typeofr, payload=None):
        '''
        Performs a generic API request and returns the JSON response
        '''
        headers = {"Authorization": self.api_key}
        if typeofr == "get": r = requests.get(endpoint_url, headers=headers)
        if typeofr == "post": r = requests.post(endpoint_url, data=payload, headers=headers)
        if typeofr == "put": r = requests.put(endpoint_url, data=payload, headers=headers)
        if typeofr == "delete": r = requests.delete(endpoint_url, data=payload, headers=headers)
        return r.json()

    def create_lead(self,email,first_name='',last_name=''):
        '''
        Creates a new lead 
        *args and kwargs can we use here? unpack and add
        '''
        raise NotImplementedError
        payload = {}
        payload["firstName"] = first_name
        payload["lastName"] = last_name
        payload["email"] = email
        payload["timezone"] = timezone
        payload["ipAddress"] = ipAddress
        payload["tags"] = tags
        payload["meta"] = meta
        payload["subscribed"] = 'true'
        payload["overrideExisting"] = 'true'
        return self.__perform_request(self.base_url + 'leads', typeofr="post", payload=payload)

    def read_lead(self,lead_email):
        '''
        Reads a lead
        '''
        lead_md5_hash = (hashlib.md5(lead_email)).hexdigest()
        return self.__perform_request(self.base_url + 'leads/' + lead_md5_hash, typeofr="get")

    def update_lead(self,lead_email):
        '''
        Updates a lead ()
        '''
        raise NotImplementedError
        lead_md5_hash = (hashlib.md5(lead_email)).hexdigest()
        return self.__perform_request(self.base_url + 'leads/' + lead_md5_hash, typeofr="put")

    def delete_lead(self,lead_email):
        '''
        Deletes a lead
        '''
        lead_md5_hash = (hashlib.md5(lead_email)).hexdigest()
        return self.__perform_request(self.base_url + 'leads/' + lead_md5_hash, typeofr="delete")

