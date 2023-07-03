import sys
import pyautogui
import pyperclip

pyautogui.hotkey("win", "r")
pyautogui.write("mspaint")
pyautogui.press("enter")

# 그림판 나타날 떄까지 2초 대기
pyautogui.sleep(2)

window = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0] # 그림판 1개만 띄어져 있다고 가정
if window.isMaximized == False:
    window.maximize()
    
# 글자 버튼 클릭
btn_text = pyautogui.locateOnScreen("btn_text.png")
if btn_text:
    pyautogui.click(btn_text, duration=0.5)
else:
    print("찾기 실패")
    sys.exit()
    
# 흰 영역 클릭
#pyautogui.click(300,300, duration=0.5)

btn_brush = pyautogui.locateOnScreen("btn_brush.png")
pyautogui.click(btn_brush.left - 300, btn_brush.top + 300)

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")
    
my_write("참 잘했어요")

# 5초 대기
pyautogui.sleep(5)

# 프로그램 종료
window.close()
pyautogui.sleep(0.5)
pyautogui.moveTo(1270, 755, duration=0.5)
pyautogui.click()