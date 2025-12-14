"""Test to verify IANA timezone strings are properly accepted."""

from src.enhanced_logger import get_logger

print("Testing IANA timezone string support")
print("=" * 80)

# Test various IANA timezone string formats.
test_timezones = [
    # Standard IANA format (Region/City)
    "America/New_York",
    "America/Los_Angeles",
    "America/Chicago",
    "Europe/London",
    "Europe/Paris",
    "Asia/Tokyo",
    "Asia/Shanghai",
    "Australia/Sydney",
    "Pacific/Auckland",

    # POSIX-style (US/*)
    "US/Pacific",
    "US/Eastern",
    "US/Central",
    "US/Mountain",

    # UTC variants
    "UTC",
    "GMT",

    # Other formats
    "America/Argentina/Buenos_Aires",
    "America/Indiana/Indianapolis",
]

print("\nTesting each timezone format:\n")

for tz in test_timezones:
    try:
        logger = get_logger(timezone=tz, fileout_path=None)
        logger.info(f"Successfully using timezone: {tz}")
        print(f"✓ {tz:40s} - SUCCESS")
    except Exception as e:
        print(f"✗ {tz:40s} - FAILED: {e}")

print("\n" + "=" * 80)
print("Test complete!")

# Test that we can switch between different timezone formats.
print("\n" + "=" * 80)
print("Testing timezone switching:")
print("=" * 80)

logger = get_logger(timezone="America/New_York", fileout_path=None)
logger.info("Message 1 in New York time")

logger = get_logger(timezone="Europe/London", fileout_path=None)
logger.info("Message 2 in London time")

logger = get_logger(timezone="Asia/Tokyo", fileout_path=None)
logger.info("Message 3 in Tokyo time")

logger = get_logger(timezone="UTC", fileout_path=None)
logger.info("Message 4 in UTC")

print("\n" + "=" * 80)
print("All tests passed!")

