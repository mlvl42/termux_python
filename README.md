# termux_python

`termux_python` provides python bindings for https://wiki.termux.com/wiki/Termux:API
and other termux scripts.

## Install

This package is available via pip:
```
pip install termux_python
```

For development purposes, use [poetry](https://python-poetry.org/):
```bash
git clone https://github.com/mlvl42/termux_python
cd termux_python
poetry install
```

## Example

The following example shows how some bindings could be used in a python script. Check [the list of supported
APIs](https://github.com/mlvl42/termux_python/blob/master/termux/termux.py) as well
as the content of [the original termux-api scripts](https://github.com/termux/termux-api-package/tree/master/scripts)
to understand how to use the bindings.

```python
import termux
import textwrap

# retrieve various device infos
print(termux.wifi_connectioninfo())
print(termux.camera_info())
print(termux.telephony_deviceinfo())

# pretty print last 100 sms
messages = termux.sms_list(limit=100)

for m in messages:
    if 'sender' in m:
        print(f"{m['sender']}:")
    else:
        print(f"{m['number']}:")
    wrap = textwrap.TextWrapper(initial_indent='\t', subsequent_indent='\t')
    body = wrap.fill(m["body"])
    print(body)

# send a message
termux.sms_send("sending an sms from python", "+01020304050")

# perform an action if the fingerprint matches
ret = termux.fingerprint(title="Restricted action", desc="Analyze your fingerprint")
if ret['auth_result'] == 'AUTH_RESULT_SUCCESS':
    print("Access granted")
else:
    print("Access denied")

# text to speech
termux.tts_speak("job's done !")
```
