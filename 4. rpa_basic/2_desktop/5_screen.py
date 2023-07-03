import pyautogui
#스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png") # 파일로 저장

# pyautogui.mouseInfo()
# 606,617 207, 210, 217 #CED1D8

pixel = pyautogui.pixel(606, 617)
print(pixel)


# print(pyautogui.pixelMatchesColor(606, 617, (207, 210, 217)))
print(pyautogui.pixelMatchesColor(606, 617, pixel))