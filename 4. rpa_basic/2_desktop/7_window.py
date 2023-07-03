import pyautogui

# fw = pyautogui.getActiveWindow() # 현재 활성화된 창 (Vscode)
# print(fw.title) # 창의 제목 정보
# print(fw.size) # 창의 크기 정보
# print(fw.left, fw.top, fw.right, fw.bottom)
# pyautogui.click(fw.left + 25, fw.top + 20)

# for w in pyautogui.getAllWindows():
#     print(w) # 모든 윈도우 가져오기
    
w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)
if w.isActive == False: # 현재 활성화가 되지 않았다면
    w.activate() # 활성화 (맨 앞으로 가져오기)
    
if w.isMaximized == False:
    w.maximize() # 최대화

pyautogui.sleep(1)

# if w.isMinimized == False:
#     w.minimize() # 최소화

w.restore() # 화면 원복

w.close() # 윈도우 닫기