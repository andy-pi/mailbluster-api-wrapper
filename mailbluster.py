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

    def __get_lead_md5_hash(lead_email):
        '''
        Returns md5 hash of supplied email address
        '''
        lead_email = lead_email.encode('utf-8')
        return (hashlib.md5(lead_email)).hexdigest()

    def create_lead(self,**kwargs):
        '''
        Creates a new lead 
        required parameters: email
        optional parameters: firstName, lastName, timezone, ipAddress, tags, meta,
        '''
        payload = locals()["kwargs"]
        if "email" not in payload:
            raise TypeError("Missing 'email' argument") 
        payload["subscribed"] = 'true'
        payload["overrideExisting"] = 'true'
        return self.__perform_request(self.base_url + 'leads', typeofr="post", payload=payload)

    def read_lead(self,lead_email):
        '''
        Reads a lead
        required parameters: email
        '''
        lead_md5_hash = self.__get_lead_md5_hash(lead_email)
        return self.__perform_request(self.base_url + 'leads/' + lead_md5_hash, typeofr="get")

    def update_lead(self,**kwargs):
        '''
        Updates a lead
        required parameters: email
        optional parameters: firstName, lastName, timezone, ipAddress, meta, addTags, removeTags
        '''
        payload = locals()["kwargs"]
        if "email" not in payload:
            raise TypeError("Missing 'email' argument") 
        lead_md5_hash = self.__get_lead_md5_hash(payload["email"])
        return self.__perform_request(self.base_url + 'leads/' + lead_md5_hash, typeofr="put", payload=payload)

    def delete_lead(self,lead_email):
        '''
        Deletes a lead
        required parameters: email
        '''
        lead_md5_hash = self.__get_lead_md5_hash(lead_email)
        return self.__perform_request(self.base_url + 'leads/' + lead_md5_hash, typeofr="delete")
