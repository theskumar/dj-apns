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
All settings are contained in a `DJAPNS` dict.

- `ENABLE_ADMIN` (default=True) - Whether to enable Admin interface of not.
- `ENABLED` (default=True) - Do not send push notifications, but only logs the messages to console useful for testing purposes.

- `USE_SANDBOX` (default=True)
- `CERT_SANDBOX_FILE` (default=None)
- `CERT_PRODUCTION_FILE` (default=None)


## Sending messages

TODO

## Sending bulk messages

TODO

## Administration

APNS devices which are not receiving push notifications can be set to inactive by two methods. The web admin interface for APNS devices has a "prune devices" option. Any selected devices which are not receiving notifications will be set to inactive [1]. There is also a management command to prune all devices failing to receive notifications:

    $ python manage.py prune_devices
