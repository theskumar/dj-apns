from django.conf import settings

DJAPNS_SETTINGS = getattr(settings, "DJAPNS", {})

# Common
DJAPNS_SETTINGS.setdefault("ENABLED", True)
DJAPNS_SETTINGS.setdefault("ENABLE_ADMIN", True)

# APNS
DJAPNS_SETTINGS.setdefault("USE_SANDBOX", True)
DJAPNS_SETTINGS.setdefault("CERT_SANDBOX_FILE", None)
DJAPNS_SETTINGS.setdefault("CERT_PRODUCTION_FILE", None)
