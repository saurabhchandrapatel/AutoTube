""" Version 5.2
# Status: Stable
# Documentation: https://github.com/Ankit404butfound/PyWhatKit/wiki
# Report Bugs and Feature Requests here: https://github.com/Ankit404butfound/PyWhatKit/issues
# For further Information, Join our Discord: https://discord.gg/62Yf5mushu
"""
__VERSION__ = "Version 5.3 (Stable)"

from platform import system

from .ascii_art import image_to_ascii_art
from .handwriting import text_to_handwriting
from .mail import send_hmail, send_mail
from .misc import info, playonyt, search, show_history
from .sc import cancel_shutdown, shutdown
from .whats import (
    open_web,
    sendwhatmsg,
    sendwhatmsg_instantly,
    sendwhatmsg_to_group,
    sendwhatmsg_to_group_instantly,
    sendwhats_image,
    sendwhatdoc_immediately,
    sendimg_or_video_immediately
)

_system = system().lower()
if _system in ("darwin", "windows"):
    from .misc import take_screenshot

if _system == "windows":
    from .remotekit import start_server
