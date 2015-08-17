# pybullet
Simple python interface to PushBullet. The following functions are implemented:

```python
def push_note(title = "Untitled", body = "Sample body", token = ""):
def push_link(title = "Untitled", body = "Sample: body", url = "http://www.google.co.uk", token = ""):
def get_pushes(modified_after = 0, active = True, token = ""):
```

Simply do:
```python
import pybullet
pybullet.push_note("title", "body", "TOKEN")
```

to use the functions listed above. Requires python packages ```urllib2``` and ```json```. All functions return the response. If the request fails, ```None``` is returned, otherwise a string representation of the json response is returned.
