"""Demo showing timezone support in enhanced_logger."""

from src.enhanced_logger import get_logger

# Example 1: Default logger (uses local timezone).
print("=" * 80)
print("Example 1: Default logger (local timezone)")
print("=" * 80)
logger = get_logger(name="demo", fileout_path=None)
logger.info("This log uses the local timezone")
print()

# Example 2: UTC timezone.
print("=" * 80)
print("Example 2: UTC timezone")
print("=" * 80)
logger_utc = get_logger(timezone="UTC")
logger_utc.info("This log uses UTC timezone")
print()

# Example 3: US Pacific timezone.
print("=" * 80)
print("Example 3: US/Pacific timezone")
print("=" * 80)
logger_pacific = get_logger(timezone="US/Pacific")
logger_pacific.info("This log uses US/Pacific timezone")
print()

# Example 4: Europe/London timezone.
print("=" * 80)
print("Example 4: Europe/London timezone")
print("=" * 80)
logger_london = get_logger(timezone="Europe/London")
logger_london.info("This log uses Europe/London timezone")
print()

# Example 5: Asia/Tokyo timezone.
print("=" * 80)
print("Example 5: Asia/Tokyo timezone")
print("=" * 80)
logger_tokyo = get_logger(timezone="Asia/Tokyo")
logger_tokyo.info("This log uses Asia/Tokyo timezone")
print()

# Example 6: Multiple log levels with timezone.
print("=" * 80)
print("Example 6: Multiple log levels with US/Eastern timezone")
print("=" * 80)
logger_eastern = get_logger(timezone="US/Eastern", level="DEBUG")
logger_eastern.debug("Debug message with timezone")
logger_eastern.info("Info message with timezone")
logger_eastern.warning("Warning message with timezone")
logger_eastern.error("Error message with timezone")
print()

# Example 7: Change timezone on the fly.
print("=" * 80)
print("Example 7: Switching timezones")
print("=" * 80)
logger_switch = get_logger(timezone="Australia/Sydney")
logger_switch.info("First log with Australia/Sydney timezone")
logger_switch = get_logger(timezone="America/New_York")
logger_switch.info("Second log with America/New_York timezone")

