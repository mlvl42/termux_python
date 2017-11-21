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


# termux-camera-photo
# termux-clipboard-get
# termux-clipboard-set
# termux-contact-list
# termux-dialog
# termux-download
# termux-fix-shebang
# termux-info
# termux-infrared-frequencies
# termux-infrared-transmit
# termux-location
# termux-notification
# termux-notification-remove
# termux-open
# termux-open-url
# termux-reload-settings
# termux-setup-storage
# termux-share
# termux-sms-inbox
# termux-sms-send
# termux-storage-get
# termux-telephony-call
# termux-telephony-cellinfo
# termux-telephony-deviceinfo
# termux-toast
# termux-tts-engines
# termux-tts-speak
# termux-vibrate
# termux-wake-lock
# termux-wake-unlock
# termux-wifi-connectioninfo
# termux-wifi-scaninfo
