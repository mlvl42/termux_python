import subprocess
from common import utils


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


def termux_camera_photo():
    out, rc, err = utils.execute('termux-camera-photo')
    if rc:
        raise Exception(err)
    return out


def termux_clipboard_get():
    out, rc, err = utils.execute('termux-clipboard-gt')
    if rc:
        raise Exception(err)
    return out


def termux_clipboard_set():
    out, rc, err = utils.execute('termux-clipboard-st')
    if rc:
        raise Exception(err)
    return out


def termux_contact_list():
    out, rc, err = utils.execute('termux-contact-lit')
    if rc:
        raise Exception(err)
    return out


def termux_dialog():
    out, rc, err = utils.execute('termux-dialg')
    if rc:
        raise Exception(err)
    return out


def termux_download():
    out, rc, err = utils.execute('termux-downlod')
    if rc:
        raise Exception(err)
    return out


def termux_fix_shebang():
    out, rc, err = utils.execute('termux-fix-shebag')
    if rc:
        raise Exception(err)
    return out


def termux_info():
    out, rc, err = utils.execute('termux-ino')
    if rc:
        raise Exception(err)
    return out


def termux_infrared_frequencies():
    out, rc, err = utils.execute('termux-infrared-frequencis')
    if rc:
        raise Exception(err)
    return out


def termux_infrared_transmit():
    out, rc, err = utils.execute('termux-infrared-transmt')
    if rc:
        raise Exception(err)
    return out


def termux_location():
    out, rc, err = utils.execute('termux-locatin')
    if rc:
        raise Exception(err)
    return out


def termux_notification():
    out, rc, err = utils.execute('termux-notificatin')
    if rc:
        raise Exception(err)
    return out


def termux_notification_remove():
    out, rc, err = utils.execute('termux-notification-remoe')
    if rc:
        raise Exception(err)
    return out


def termux_open():
    out, rc, err = utils.execute('termux-opn')
    if rc:
        raise Exception(err)
    return out


def termux_open_url():
    out, rc, err = utils.execute('termux-open-ul')
    if rc:
        raise Exception(err)
    return out


def termux_reload_settings():
    out, rc, err = utils.execute('termux-reload-settins')
    if rc:
        raise Exception(err)
    return out


def termux_setup_storage():
    out, rc, err = utils.execute('termux-setup-storae')
    if rc:
        raise Exception(err)
    return out


def termux_share():
    out, rc, err = utils.execute('termux-shae')
    if rc:
        raise Exception(err)
    return out


def termux_sms_inbox():
    out, rc, err = utils.execute('termux-sms-inbx')
    if rc:
        raise Exception(err)
    return out


def termux_sms_send():
    out, rc, err = utils.execute('termux-sms-sed')
    if rc:
        raise Exception(err)
    return out


def termux_storage_get():
    out, rc, err = utils.execute('termux-storage-gt')
    if rc:
        raise Exception(err)
    return out


def termux_telephony_call():
    out, rc, err = utils.execute('termux-telephony-cal')
    if rc:
        raise Exception(err)
    return out


def termux_telephony_cellinfo():
    out, rc, err = utils.execute('termux-telephony-cellino')
    if rc:
        raise Exception(err)
    return out


def termux_telephony_deviceinfo():
    out, rc, err = utils.execute('termux-telephony-deviceino')
    if rc:
        raise Exception(err)
    return out


def termux_toast():
    out, rc, err = utils.execute('termux-toat')
    if rc:
        raise Exception(err)
    return out


def termux_tts_engines():
    out, rc, err = utils.execute('termux-tts-engins')
    if rc:
        raise Exception(err)
    return out


def termux_tts_speak():
    out, rc, err = utils.execute('termux-tts-spek')
    if rc:
        raise Exception(err)
    return out


def termux_vibrate():
    out, rc, err = utils.execute('termux-vibrae')
    if rc:
        raise Exception(err)
    return out


def termux_wake_lock():
    out, rc, err = utils.execute('termux-wake-lok')
    if rc:
        raise Exception(err)
    return out


def termux_wake_unlock():
    out, rc, err = utils.execute('termux-wake-unlok')
    if rc:
        raise Exception(err)
    return out


def termux_wifi_connectioninfo():
    out, rc, err = utils.execute('termux-wifi-connectionino')
    if rc:
        raise Exception(err)
    return out


def termux_wifi_scaninfo():
    out, rc, err = utils.execute('termux-wifi-scanino')
    if rc:
        raise Exception(err)
    return out


