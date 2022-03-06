# Mailbluster Leads Python API  

An Python wrapper for the [Mailbluster API](https://app.mailbluster.com/api-doc/products).  
(currently for leads only - products and orders not implemented - PRs welcome)  

## Minimal Example  

from mailbluster import Mailbluster  
mailblusterclient = Mailbluster(mailbluster_api_key)  
response = mailblusterclient.create_lead(email="me@example.com",firstName="Andy",lastName="Pi")  

## Lead creation form  
This repo also contains a [Flask-Zappa](https://github.com/zappa/Zappa) app for lead collection  
which runs on AWS lambda (newlead.py; /static, /templates).  
To use, you'll need an AWS account and credentials.  