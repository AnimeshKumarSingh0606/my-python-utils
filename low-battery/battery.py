import psutil                             #install this first

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

if percent >= 30:
 
    # pip install py-notifier
    # pip install win10toast              install these two modules
    from pynotifier import Notification

    Notification(
        title="Battery Low",
        description=str(percent) + "% Battery remain!!",
        duration=5,  # Duration in seconds
        urgency=Notification.URGENCY_CRITICAL,
    ).send()