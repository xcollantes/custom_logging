"""Demonstrate IANA timezone validation and helper functions."""

from src.enhanced_logger import get_logger, get_available_timezones, is_valid_timezone

print("=" * 80)
print("IANA Timezone Support Demonstration")
print("=" * 80)

# Show total available timezones.
timezones = get_available_timezones()
print(f"\nTotal IANA timezones available: {len(timezones)}")

# Show sample timezones by region.
print("\nSample timezones by region:")
print("-" * 80)

regions = ["America", "Europe", "Asia", "Africa", "Pacific", "Australia"]
for region in regions:
    region_tzs = sorted([tz for tz in timezones if tz.startswith(region)])[:5]
    print(f"\n{region}:")
    for tz in region_tzs:
        print(f"  - {tz}")

# Validate timezone strings.
print("\n" + "=" * 80)
print("Testing timezone validation:")
print("=" * 80)

test_cases = [
    ("America/New_York", True),
    ("US/Pacific", True),
    ("UTC", True),
    ("Invalid/Timezone", False),
    ("America/FakeCity", False),
    (
        "PST",
        False,
    ),  # PST is not a valid IANA identifier (use America/Los_Angeles or US/Pacific)
]

for tz_str, expected in test_cases:
    is_valid = is_valid_timezone(tz_str)
    status = "✓" if is_valid == expected else "✗"
    result = "VALID" if is_valid else "INVALID"
    print(f"{status} {tz_str:30s} - {result}")

# Test with valid timezones.
print("\n" + "=" * 80)
print("Testing logger with various IANA timezones:")
print("=" * 80)

valid_timezones = [
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "UTC",
]

for tz in valid_timezones:
    logger = get_logger(timezone=tz, fileout_path=None)
    logger.info(f"Using IANA timezone: {tz}")

# Test with invalid timezone (should show warning and fall back).
print("\n" + "=" * 80)
print("Testing with invalid timezone (should show warning):")
print("=" * 80)

try:
    logger = get_logger(timezone="Invalid/Timezone", fileout_path=None)
    logger.info("This should work but use local time after warning")
except Exception as e:
    print(f"Error: {e}")

print("\n" + "=" * 80)
print("Demonstration complete!")
print("=" * 80)
print("\nKey Points:")
print("- The logger uses Python's zoneinfo module with IANA timezone database")
print("- All standard IANA timezone identifiers are supported")
print("- Format: Region/City (e.g., 'America/New_York', 'Europe/London')")
print("- Use get_available_timezones() to see all available timezones")
print("- Use is_valid_timezone() to validate timezone strings before using them")
