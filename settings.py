"""
Searcharr
Sonarr & Radarr Telegram Bot
By Todd Roberts
https://github.com/toddrob99/searcharr
"""

# Searcharr Bot
searcharr_password = "abc123"  # Used to authenticate as a regular user to add series/movies
searcharr_admin_password = "pls100182881"  # Used to authenticate as admin to manage users
searcharr_language = "en-us"  # yml file in the lang folder
searcharr_start_command_aliases = ["start"]  # Override /start command
searcharr_help_command_aliases = ["help"]  # Override /help command
searcharr_users_command_aliases = ["users"]  # Override /users command

# Telegram
tgram_token = "2001554503:AAH1mz3sDU-4oO8lDbm4K4H-wBQIFZN9Tu0"

# Sonarr
sonarr_enabled = True
sonarr_url = "http://192.168.1.100:8989"  # http://192.168.0.100:8989
sonarr_api_key = "623e7f7776804e72bb79ab74cc84b064"
sonarr_quality_profile_id = ["1080p/720p/480p"]  # can be name or id value - include multiple to allow the user to choose
sonarr_add_monitored = True
sonarr_search_on_add = True
sonarr_tag_with_username = True
sonarr_forced_tags = []  # e.g. ["searcharr", "friends-and-family"] - leave empty for none
sonarr_allow_user_to_select_tags = True
sonarr_user_selectable_tags = []  # e.g. ["custom-tag-1", "custom-tag-2"] - leave empty to let user choose from all tags in Sonarr
sonarr_series_command_aliases = ["series"]  # e.g. ["series", "tv", "t"]
sonarr_series_paths = []  # e.g. ["/tv", "/anime"] - can be full path or id value - leave empty to enable all
sonarr_season_monitor_prompt = False  # False - always monitor all seasons; True - prompt user to select from All, First, or Latest season(s)

# Radarr
radarr_enabled = True
radarr_url = "http://192.168.1.100:7878"  # http://192.168.0.100:7878
radarr_api_key = "7fc6ddc9cc244075a85cfcdf8866303d"
radarr_quality_profile_id = ["720p/1080p/4k"]  # can be name or id value - include multiple to allow the user to choose
radarr_add_monitored = True
radarr_search_on_add = True
radarr_tag_with_username = True
radarr_forced_tags = []  # e.g. ["searcharr", "friends-and-family"] - leave empty for none
radarr_allow_user_to_select_tags = True
radarr_user_selectable_tags = []  # e.g. ["custom-tag-1", "custom-tag-2"] - leave empty to let user choose from all tags in Radarr
radarr_min_availability = "released"  # options: "announced", "inCinemas", "released"
radarr_movie_command_aliases = ["movie"]  # e.g. ["movie", "mv", "m"]
radarr_movie_paths = []  # e.g. ["/movies", "/other-movies"] - can be full path or id value - leave empty to enable all
