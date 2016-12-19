DJAPNS (Push Notifications for Django)
======================================

A minimal Django app can be used to send [apns] push notification that implements Device models that can send messages through [APNS].


[APNS]: https://developer.apple.com/go/?id=push-notifications

## Setup

Download and copy the `djapns` folder to your project or any of your PYTHON_PATH.

Edit your settings.py file:

```
INSTALLED_APPS = (
        ...
        "djapns",
)
```

### Settings list

## Sending messages

TODO

## Sending bulk messages

TODO

## Administration

APNS devices which are not receiving push notifications can be set to inactive by two methods. The web admin interface for APNS devices has a "prune devices" option. Any selected devices which are not receiving notifications will be set to inactive [1]. There is also a management command to prune all devices failing to receive notifications:

    $ python manage.py prune_devices
