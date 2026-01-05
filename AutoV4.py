#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# RaisoTool v7.0 - ULTIMATE SPEED (Multi-Threading)
# Fixed & Tested - Works on Servers & Groups

import os
import requests
import threading
import itertools
from colorama import init, Fore

init(autoreset=True)

# الألوان (Colors)
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
C = Fore.CYAN
W = Fore.WHITE
LG = Fore.LIGHTGREEN_EX
LY = Fore.LIGHTYELLOW_EX
LC = Fore.LIGHTCYAN_EX
RESET = Fore.RESET

def banner():
    os.system('clear')
    print(f"""{R}
┌──────────────────────────────────────┐
│  RAISOTOOL v7.0 - ULTIMATE SPEED     │
│    (SERVERS + GROUPS + MENTION)      │
└──────────────────────────────────────┘{RESET}""")

def send_request(url, headers, payload, count):
    try:
        # إرسال بدون انتظار طويل لزيادة السرعة
        r = requests.post(url, headers=headers, json=payload, timeout=5)
        if r.status_code == 200:
            print(f"{W}[{count:04d}] {LG}SENT ➤ {LY}{payload['content'][:30]}{RESET}")
        elif r.status_code == 429:
            print(f"{R}!!! RATE LIMITED (Too Fast) !!!{RESET}")
        elif r.status_code == 403:
            print(f"{R}FAILED (403): No Permission{RESET}")
    except:
        pass

def spam_loop(token, channel_id, mention, messages):
    url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
    headers = {"Authorization": token, "Content-Type": "application/json"}
    count = 0
    
    # تكرار الرسائل بشكل لا نهائي
    message_cycle = itertools.cycle(messages)
    
    while True:
        count += 1
        msg = next(message_cycle)
        payload = {"content": f"{mention}{msg}"}
        
        # تشغيل نظام الـ Threading لإرسال مئات الطلبات في وقت واحد
        t = threading.Thread(target=send_request, args=(url, headers, payload, count))
        t.start()
        
        # لا يوجد delay هنا لضمان أقصى سرعة (Turbo Mode)

def main():
    banner()
    token = input(f"{W} ┌─ Token ➜ {G}").strip()
    channel_id = input(f"{W} ┌─ Channel/Group ID ➜ {C}").strip()
    m_id = input(f"{W} ┌─ User ID to Mention ➜ {LY}").strip()
    
    print(f"\n{LC}Enter messages (type 'done' to finish):")
    messages = []
    while True:
        m = input(f"   {W}➤ {RESET}").strip()
        if m.lower() == 'done':
            if not messages: continue
            break
        if m: messages.append(m)
    
    mention = f"<@{m_id}> " if m_id else ""
    
    print(f"\n{R}!!! ATTACK STARTED AT MAX SPEED !!!{RESET}\n")
    spam_loop(token, channel_id, mention, messages)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}Stopped.{RESET}")

