import time
import os
social_media_sites = [
    "facebook.com",
    "twitter.com",
    "instagram.com"
]
start_time = 9
end_time = 18
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"


def block_social_media():
    current_hour = time.localtime().tm_hour
    if start_time <= current_hour < end_time:
        with open(hosts_path, "a") as hosts_file:
            for site in social_media_sites:
                hosts_file.write(f"127.0.0.1 {site}\n")
        print("Social media sites blocked.")
    else:
        print("Not within the specified time window. No action taken.")


if __name__ == "__main__":
    block_social_media()