import subprocess
from termux.common import utils


"""
    implementation of all the termux-api commands
    via subprocesses,
"""
def battery_status():
    out, rc, err = utils.execute('termux-battery-status')
    if rc:
        raise Exception(err)
    return out


def camera_info():
    out, rc, err = utils.execute('termux-camera-info')
    if rc:
        raise Exception(err)
    return out


def camera_photo():
    out, rc, err = utils.execute('termux-camera-photo')
    if rc:
        raise Exception(err)
    return out


def clipboard_get():
    out, rc, err = utils.execute('termux-clipboard-get')
    if rc:
        raise Exception(err)
    return out


def clipboard_set():
    out, rc, err = utils.execute('termux-clipboard-set')
    if rc:
        raise Exception(err)
    return out


def contact_list():
    out, rc, err = utils.execute('termux-contact-list')
    if rc:
        raise Exception(err)
    return out


def dialog():
    out, rc, err = utils.execute('termux-dialog')
    if rc:
        raise Exception(err)
    return out


def download():
    out, rc, err = utils.execute('termux-download')
    if rc:
        raise Exception(err)
    return out


def fix_shebang():
    out, rc, err = utils.execute('termux-fix-shebang')
    if rc:
        raise Exception(err)
    return out


def info():
    out, rc, err = utils.execute('termux-info')
    if rc:
        raise Exception(err)
    return out


def infrared_frequencies():
    out, rc, err = utils.execute('termux-infrared-frequencies')
    if rc:
        raise Exception(err)
    return out


def infrared_transmit():
    out, rc, err = utils.execute('termux-infrared-transmit')
    if rc:
        raise Exception(err)
    return out


def location():
    out, rc, err = utils.execute('termux-location')
    if rc:
        raise Exception(err)
    return out


def notification():
    out, rc, err = utils.execute('termux-notification')
    if rc:
        raise Exception(err)
    return out


def notification_remove():
    out, rc, err = utils.execute('termux-notification-remove')
    if rc:
        raise Exception(err)
    return out


def open():
    out, rc, err = utils.execute('termux-open')
    if rc:
        raise Exception(err)
    return out


def open_url():
    out, rc, err = utils.execute('termux-open-url')
    if rc:
        raise Exception(err)
    return out


def reload_settings():
    out, rc, err = utils.execute('termux-reload-settings')
    if rc:
        raise Exception(err)
    return out


def setup_storage():
    out, rc, err = utils.execute('termux-setup-storage')
    if rc:
        raise Exception(err)
    return out


def share():
    out, rc, err = utils.execute('termux-share')
    if rc:
        raise Exception(err)
    return out


def sms_inbox():
    out, rc, err = utils.execute('termux-sms-inbox')
    if rc:
        raise Exception(err)
    return out


def sms_send():
    out, rc, err = utils.execute('termux-sms-send')
    if rc:
        raise Exception(err)
    return out


def storage_get():
    out, rc, err = utils.execute('termux-storage-get')
    if rc:
        raise Exception(err)
    return out


def telephony_call():
    out, rc, err = utils.execute('termux-telephony-call')
    if rc:
        raise Exception(err)
    return out


def telephony_cellinfo():
    out, rc, err = utils.execute('termux-telephony-cellinfo')
    if rc:
        raise Exception(err)
    return out


def telephony_deviceinfo():
    out, rc, err = utils.execute('termux-telephony-deviceinfo')
    if rc:
        raise Exception(err)
    return out


def toast():
    out, rc, err = utils.execute('termux-toast')
    if rc:
        raise Exception(err)
    return out


def tts_engines():
    out, rc, err = utils.execute('termux-tts-engines')
    if rc:
        raise Exception(err)
    return out


def tts_speak():
    out, rc, err = utils.execute('termux-tts-speak')
    if rc:
        raise Exception(err)
    return out


def vibrate():
    out, rc, err = utils.execute('termux-vibrate')
    if rc:
        raise Exception(err)
    return out


def wake_lock():
    out, rc, err = utils.execute('termux-wake-lock')
    if rc:
        raise Exception(err)
    return out


def wake_unlock():
    out, rc, err = utils.execute('termux-wake-unlock')
    if rc:
        raise Exception(err)
    return out


def wifi_connectioninfo():
    out, rc, err = utils.execute('termux-wifi-connectioninfo')
    if rc:
        raise Exception(err)
    return out


def wifi_scaninfo():
    out, rc, err = utils.execute('termux-wifi-scaninfo')
    if rc:
        raise Exception(err)
    return out
