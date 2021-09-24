#!/usr/bin/env python

import os
import json

def get_profiles(browser, path):
  profiles = []
  if os.path.isdir(path) == False:
    return profiles
  folders = [ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ]
  for folder in folders:
    file = "{}/{}/Preferences".format(path, folder)
    if folder != 'System Profile' and folder != 'Guest Profile' and (os.path.isfile(file)):
      with open(file) as f:
        data = json.load(f)
        name = data['profile']['name']
        hd = name
#        name = data['account_info'][0]['full_name'];
#        hd = data['account_info'][0]['hd']
        profiles.append({
          "icon": {
#           "path": "icons/{}".format(browser['icon'])
            "path": "{}/{}/Google Profile Picture.png".format(path,folder)
          },
          "arg": "{} {}".format(browser['name'], folder),
          "subtitle": "Open Chrome using {} profile.".format(name.encode('utf-8')),
          "title": hd,
        })
  return profiles


home = os.path.expanduser("~")

browsers = [
  { 'name': 'CHROME', 'path': '/Library/Application Support/Google/Chrome', 'icon': 'chrome.icns' },
#  { 'name': 'CHROME_CANARY', 'path': '/Library/Application Support/Google/Chrome Canary', 'icon': 'canary.icns' },
  # { 'name': 'CHROMIUM', 'path': '/Library/Application Support/Chromium', 'icon': 'chromium.icns' },
]

profiles = []

for browser in browsers:
  path = "{}{}".format(home, browser['path'])
  prof = get_profiles(browser, path)
  profiles += prof

print json.dumps({"items": profiles}, indent=2)
