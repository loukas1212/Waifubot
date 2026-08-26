#!/usr/bin/env python3
import requests

def waifuapi():
    api_url = "https://api.waifu.im/images"
    response = requests.get(api_url)
    data = response.json()

    item = data["items"][0]
    return item["id"], item["url"]


def waifuapi_sfw_tag(tag):
    api_url = f"https://api.waifu.im/images?included_tags={tag}"
    response = requests.get(api_url)
    data = response.json()

    item = data["items"][0]
    return item["id"], item["url"]

def waifuapi_nsfw(tag):
    api_url = f"https://api.waifu.im/images?included_tags={tag}&is_nsfw=true"
    response = requests.get(api_url)
    data = response.json()

    item = data["items"][0]
    return item["id"], item["url"]