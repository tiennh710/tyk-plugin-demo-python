from tyk.decorators import *
from gateway import TykGateway as tyk
from google.protobuf.json_format import MessageToDict, MessageToJson
import json

@Hook
def PostKeyAuth(request, session, metadata, spec):
    tyk.log("-----PostKeyAuth is called-----", "info")

    addConfigDataToRequestBody(request, spec['config_data'])

    tyk.log("request info: {0}".format(MessageToJson(request.object)), "info")  
    return request, session, metadata

@Hook
def ResponseHook(request, response, session, metadata, spec):
    tyk.log("ResponseHook is called", "info")

    addConfigDataToResponseBody(response, spec['config_data'])

    tyk.log("response info: {0}".format(MessageToJson(response)), "info")  
    return response

@Hook
def PreHook(request, session, spec):
    tyk.log("PreHook is called", "info")
    return request, session

@Hook
def PostHook(request, session, spec):
    tyk.log("PostHook is called", "info")
    return request, session

@Hook
def AuthCheck(request, session, metadata, spec):
    tyk.log("AuthCheck is called", "info")
    return request, session, metadata

# ------------------------------------------------

def addConfigDataToRequestBody(request, config_data):
    tyk.log("Add config data to request body", "info")

    req_body = getRequestBody(request)
    json_config_data = json.loads(config_data)

    for key in json_config_data['data']['field_for_request']:
        req_body[key] = json_config_data['data']['field_for_request'][key]
        

    new_req_body = json.dumps(req_body) 
    request.object.body = new_req_body
    request.object.raw_body = bytes(new_req_body, 'utf-8')

def getRequestBody(request):
    tyk_request = MessageToDict(request.object)
    req_body = json.loads(tyk_request["body"])
    return req_body

def addConfigDataToResponseBody(response, config_data):
    tyk.log("Add config data to response body", "info")

    res_body = getResponseBody(response)
    json_config_data = json.loads(config_data)

    for key in json_config_data['data']['field_for_response']:
        res_body[key] = json_config_data['data']['field_for_response'][key]

    new_res_body = json.dumps(res_body) 
    response.body = new_res_body
    response.raw_body = bytes(new_res_body, 'utf-8')

def getResponseBody(response):
    tyk_response = MessageToDict(response)
    res_body = json.loads(tyk_response["body"])
    return res_body

