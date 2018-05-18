---
title: Capturing Joystick Input
description: Capturing Joystick Input
ms.assetid: '1214fe5a-5a6a-4c6c-9b77-94eeb73f60da'
keywords: ["joysticks,capturing input", "capturing joystick input"]
---

# Capturing Joystick Input

Most of the code controlling the joystick is in the main window function. In the following portion of the message handler, the application calls [**joySetCapture**](joysetcapture.md) to capture input from the joystick JOYSTICKID1.


```C++
case WM_CREATE: 
    if(joySetCapture(hWnd, JOYSTICKID1, NULL, FALSE)) 
    { 
        MessageBeep(MB_ICONEXCLAMATION); 
        MessageBox(hWnd, "Couldn't capture the joystick.", NULL, 
            MB_OK | MB_ICONEXCLAMATION); 
        PostMessage(hWnd,WM_CLOSE,0,0L); 
    } 
    break; 
 
```



 

 




