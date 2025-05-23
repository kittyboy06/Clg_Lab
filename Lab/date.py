import datetime as dt
import pytz

# Local time (system time without timezone awareness)
local_time = dt.datetime.now()
print("Local time:", local_time)

# UTC time (naive)
utc_time = dt.datetime.now(dt.UTC)
print("UTC time:", utc_time)

# ISO format of local time
iso_time = local_time.isoformat()
print("ISO time:", iso_time)

# Desired timezone conversion
desired_timezone = "Asia/Calcutta"
timezone_object = pytz.timezone(desired_timezone)

# Make local time timezone-aware, or get current time directly in desired zone
current_time_in_zone = dt.datetime.now(timezone_object)
print(f"Current time in {desired_timezone}:", current_time_in_zone)
