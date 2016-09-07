#!/usr/bin/python
import os
import json
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2
import urllib
import mimetypes

def push_note(title = "Untitled", body = "Sample body", token = ""):
    """
    Push note using pushbullet
    """
    json_object = dict()
    json_object["type"] = "note"
    json_object["title"] = title
    json_object["body"] = body

    try:
        request = urllib2.Request("https://api.pushbullet.com/v2/pushes", data = json.dumps(json_object) )
        request.add_header('Content-Type', 'application/json')
        request.add_header('Access-Token', token)
        response = urllib2.urlopen(request)
        return response.read()
    except:
        return None

def push_link(title = "Untitled", body = "Sample body", url = "http://www.google.co.uk", token = ""):
    """
    Push link using pushbullet
    """
    json_object = dict()
    json_object["type"] = "link"
    json_object["title"] = title
    json_object["body"] = body
    json_object["url"] = url

    try:
        request = urllib2.Request("https://api.pushbullet.com/v2/pushes", data = json.dumps(json_object) )
        request.add_header('Content-Type', 'application/json')
        request.add_header('Access-Token', token)
        response = urllib2.urlopen(request)
        return response.read()
    except:
        return None

def push_file(file_path = "", file_name = "", file_desc="", token = ""):
    """
    Push file using pushbullet
    """
    json_object = dict()
    json_object["file_name"] = file_name
  
    url = urllib.pathname2url(file_path)

    mime_type = mimetypes.guess_type(url)[0]

    json_object["mime_type"] = mime_type

    try:    
        request = urllib2.Request("https://api.pushbullet.com/v2/upload-request", data = json.dumps(json_object) )
        request.add_header('Content-Type', 'application/json')
        request.add_header('Access-Token', token)
        response = urllib2.urlopen(request)
        upload_response = response.read()
    except:
        return None

    upload_data = json.loads(upload_response)

    register_openers()
    
    try:
        datagen, headers = multipart_encode({"file": open(file_path)})    
        upload_request = urllib2.Request(upload_data["upload_url"], datagen, headers)
        urllib2.urlopen(upload_request).read()
    except:
        return None

    file_object = dict()
    file_object["type"] = "file" 
    file_object["body"] = file_desc
    file_object["file_name"] = file_name
    file_object["file_type"] = mime_type
    file_object["file_url"] = upload_data["file_url"]

    try:
        push_request = urllib2.Request("https://api.pushbullet.com/v2/pushes", data = json.dumps(file_object) )
        push_request.add_header('Content-Type', 'application/json')
        push_request.add_header('Access-Token', token)
        push_response = urllib2.urlopen(push_request)
        return push_response.read()
    except:
        return None
    
def get_pushes(modified_after = 0, active = True, token = ""):
    """
    List pushbullet 'pushes'
    """
    url = "https://api.pushbullet.com/v2/pushes?" + "modified_after=" + str(modified_after) + "&active=" + str(active)
    try:
        request = urllib2.Request(url)
        request.add_header('Authorization', 'Bearer ' + token)
        response = urllib2.urlopen(request)
        return response.read()
    except:
        return None
