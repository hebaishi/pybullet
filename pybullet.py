#!/usr/bin/python
import json
import urllib2

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
        request.add_header('Authorization', 'Bearer ' + token)
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
        request.add_header('Authorization', 'Bearer ' + token)
        response = urllib2.urlopen(request)
        return response.read()
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
