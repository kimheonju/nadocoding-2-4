import pyautogui
w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 메모장 1개 띄운 상태에서 가져옴
w.activate()

# pyautogui.write("12345")
# pyautogui.write("Nadocoding", interval= 1)
# pyautogui.write("나도 코딩")

#pyautogui.write(["t","e","s","t", "left", "left","right", "l","a","enter"], interval=0.25)


# 특수 문자
# shift 4 -> $
# pyautogui.keyDown("shift") # 키를 누른 상태에서
# pyautogui.press("4") # 숫자 4를 입력하고
# pyautogui.keyUp("shift") # 키를 뗀다

# 조합키 (Hot key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl")

# 간편한 조합키
#pyautogui.hotkey("ctrl", "alt", "shift", "a") # 순서대로 누르고 순서대로 뗸다
# pyautogui.hotkey("ctrl", "a")

import pyperclip

pyperclip.copy("나도코딩") # 나도코딩 슬자를 클립보드에 저장
pyautogui.hotkey("ctrl","v") # 클립보드에 있는 내용을 붙여넣기

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")
    
my_write("나도코딩")