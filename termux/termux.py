import json
from typing import Dict, List, Optional, Union

from termux.common import utils


class PermissionError(Exception):
    pass


class ApiError(Exception):
    pass


def api_wrapper(cmd: Union[str, List]) -> str:

    # ensure all params are str before passing to subprocess
    if isinstance(cmd, list):
        cmd = list(map(str, cmd))

    out, rc, err = utils.execute(cmd)

    if rc:
        print(cmd)
        print(out, rc, err)
        raise ApiError(err)
    elif "API_ERROR" in out:
        error = json.loads(out)["API_ERROR"]
        raise ApiError(error)

    if "Please grant the following permission to use this command" in out:
        error = json.loads(out)["error"]
        raise PermissionError(error)

    return out


def api_start():
    api_wrapper("termux-api-start")


def api_stop():
    api_wrapper("termux-api-stop")


def api_restart():
    api_wrapper("termux-api-stop")
    api_wrapper("termux-api-start")


def audio_info() -> Dict:
    return json.loads(api_wrapper("termux-audio-info"))


def battery_status() -> Dict:
    return json.loads(api_wrapper("termux-battery-status"))


# TODO
# def brightness(level: int):
#     pass


def call_log(limit: Optional[int] = None, offset: Optional[int] = None) -> List[Dict]:
    cmd = ["termux-call-log"]

    if limit:
        cmd += ["-l", limit]
    if offset:
        cmd += ["-o", offset]

    return json.loads(api_wrapper(cmd))


def camera_info() -> List[Dict]:
    return json.loads(api_wrapper("termux-camera-info"))


def camera_photo(output_file: str, camera_id: Optional[str] = None):
    cmd = ["termux-camera-photo"]

    if camera_id:
        cmd += ["-c", camera_id]

    cmd.append(output_file)

    return api_wrapper(cmd)


def clipboard_get() -> str:
    return api_wrapper("termux-clipboard-get")


def clipboard_set(text: str):
    api_wrapper(["termux-clipboard-set", text])


def contact_list() -> List[Dict]:
    return json.loads(api_wrapper("termux-contact-list"))


# TODO
# def dialog():
#     pass


def download(
    url: str,
    desc: Optional[str] = None,
    title: Optional[str] = None,
    path: Optional[str] = None,
):
    cmd = ["termux-download"]

    if desc:
        cmd += ["-d", desc]

    if title:
        cmd += ["-t", title]

    if path:
        cmd += ["-p", path]

    cmd.append(url)

    return api_wrapper(cmd)


def fingerprint(
    title: Optional[str] = None,
    desc: Optional[str] = None,
    subtitle: Optional[str] = None,
    cancel: Optional[str] = None,
) -> Dict:
    cmd = ["termux-fingerprint"]

    if title:
        cmd += ["-t", title]

    if desc:
        cmd += ["-d", desc]

    if subtitle:
        cmd += ["-s", subtitle]

    if cancel:
        cmd += ["-c", cancel]

    return json.loads(api_wrapper(cmd))


def infrared_frequencies():
    return json.loads(api_wrapper("termux-infrared-frequencies"))


def infrared_transmit(frequency: int, pattern: str):
    return api_wrapper(["termux-infrared-transmit", "-f", frequency, pattern])


# TODO
# def job_scheduler():
#     pass


# TODO
# def keystore():
#     pass


def location(provider: Optional[str] = None, request: Optional[str] = None) -> Dict:
    cmd = ["termux-location"]

    if provider:
        cmd += ["-p", provider]

    if request:
        cmd += ["-r", request]

    return json.loads(api_wrapper(cmd))


def media_player(command: str, args: Optional[List[str]] = None) -> str:
    cmd = ["termux-media-player", command]

    if args:
        cmd += args

    return api_wrapper(cmd)


# TODO
# def media_scan():
#     pass


# TODO
# def microphone_record():
# pass


def nfc_read(short: bool = True):
    cmd = ["termux-nfc", "-r", "short" if short else "full"]
    return api_wrapper(cmd)


def nfc_write(text: str):
    cmd = ["termux-nfc", "-w", text]
    return api_wrapper(cmd)


def notification_list() -> List[Dict]:
    return json.loads(api_wrapper("termux-notification-list"))


def notification_remove(id: int) -> str:
    return api_wrapper(["termux-notification-remove", id])


# TODO
# def notification():
#     pass


# TODO
# def saf_*():
# pass


def open(
    path: str,
    send: bool = False,
    chooser: bool = False,
    content_type: Optional[str] = None,
):
    cmd = ["termux-open"]

    if send:
        cmd.append("--send")
    else:
        cmd.append("--view")

    if chooser:
        cmd.append("--chooser")

    if content_type:
        cmd += ["--content-type", content_type]

    cmd.append(path)
    api_wrapper(cmd)


def sensor_list() -> Dict:
    return json.loads(api_wrapper(["termux-sensor", "-l"]))


# TODO: stream command output
# def sensor_listen(sensors: Union[str,List[str]], delay: Optional[int] = None) -> Dict:
#     cmd = ['termux-sensor']

#     if sensors == "all":
#         cmd.append('-a')
#     elif isinstance(sensors, list):
#         cmd += ['-s', ','.join(sensors)]
#     else:
#         raise ValueError('Unexpected value for sensors param')

#     if delay:
#         cmd += ['-d', delay]

#     return json.loads(api_wrapper(['termux-sensor', '-l']))


def sms_list(
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    type: Optional[str] = None,
    conversation_list: bool = False,
    number: Optional[str] = None,
) -> List[Dict]:
    cmd = ["termux-sms-list"]

    if limit:
        cmd += ["-l", limit]
    if offset:
        cmd += ["-o", offset]
    if type:
        cmd += ["-t", type]
    if conversation_list:
        cmd.append("-c")

    if number:
        cmd += ["-f", number]

    return json.loads(api_wrapper(cmd))


def sms_send(text: str, number: Union[str, List[str]], slot: int = 0):
    cmd = ["termux-sms-send", "-s", slot]

    if isinstance(number, str):
        cmd += ["-n", number]
    else:
        cmd += ["-n", ",".join(number)]

    cmd.append(text)

    api_wrapper(cmd)


def speech_to_text() -> str:
    return api_wrapper("termux-speech-to-text")


def storage_get(output_file: str):
    api_wrapper(["termux-storage-get", output_file])


def telephony_call(number: str):
    api_wrapper(["termux-telephony-call", number])


def telephony_cellinfo() -> List[Dict]:
    return json.loads(api_wrapper(["termux-telephony-cellinfo"]))


def telephony_deviceinfo() -> Dict:
    return json.loads(api_wrapper(["termux-telephony-deviceinfo"]))


def toast(
    text: str,
    bgcolor: Optional[str] = None,
    color: Optional[str] = None,
    gravity: Optional[str] = None,
    short: bool = False,
):
    cmd = ["termux-toast"]

    if bgcolor:
        cmd += ["-b", bgcolor]
    if color:
        cmd += ["-c", color]
    if gravity:
        cmd += ["-g", gravity]
    if short:
        cmd.append("-s")

    cmd.append(text)

    api_wrapper(cmd)


def torch(enabled: bool):
    api_wrapper(["termux-torch", "on" if enabled else "off"])


def tts_engines() -> List[Dict]:
    return json.loads(api_wrapper("termux-tts-engines"))


def tts_speak(
    text: str,
    engine: Optional[str] = None,
    lang: Optional[str] = None,
    region: Optional[str] = None,
    variant: Optional[str] = None,
    pitch: Optional[float] = None,
    rate: Optional[float] = None,
    stream: Optional[str] = None,
):

    cmd = ["termux-tts-speak"]

    if engine:
        cmd += ["-e", engine]
    if lang:
        cmd += ["-l", lang]
    if region:
        cmd += ["-n", region]
    if variant:
        cmd += ["-v", variant]
    if pitch:
        cmd += ["-p", pitch]
    if rate:
        cmd += ["-r", rate]
    if stream:
        cmd += ["-s", stream]

    cmd.append(text)

    api_wrapper(cmd)


def vibrate(duration: Optional[int] = None, force: bool = False):
    cmd = ["termux-vibrate"]

    if duration:
        cmd += ["-d", duration]

    if force:
        cmd.append("-f")

    api_wrapper(cmd)


def volume(stream: str, value: int):
    api_wrapper(["termux-volume", stream, value])


def wifi_connectioninfo():
    return json.loads(api_wrapper("termux-wifi-connectioninfo"))


def wifi_enable(enabled: bool):
    api_wrapper(["termux-wifi-enable", "true" if enabled else "false"])


def wifi_scaninfo():
    return json.loads(api_wrapper("termux-wifi-scaninfo"))
