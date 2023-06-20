---
title: Capturing Joystick Input
description: Capturing Joystick Input
ms.assetid: 1214fe5a-5a6a-4c6c-9b77-94eeb73f60da
keywords:
- joysticks,capturing input
- capturing joystick input
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Capturing Joystick Input

\[The feature associated with this page, [Joysticks](/windows/win32/multimedia/joysticks), is a legacy feature. It has been superseded by [Windows.Gaming.Input Namespace](/uwp/api/windows.gaming.input). **Windows.Gaming.Input Namespace** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Windows.Gaming.Input Namespace** instead of **Joysticks**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Most of the code controlling the joystick is in the main window function. In the following portion of the message handler, the application calls [**joySetCapture**](/windows/win32/api/joystickapi/nf-joystickapi-joysetcapture) to capture input from the joystick JOYSTICKID1.


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



 

 