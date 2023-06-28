---
title: Processing Joystick Messages
description: Processing Joystick Messages
ms.assetid: d21a9d49-1fc0-4899-9083-87c3cf4e0e62
keywords:
- joysticks,messages
- MM_JOY1MOVE message
- MM_JOY1BUTTONDOWN message
- MM_JOY1BUTTONUP message
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Processing Joystick Messages

\[The feature associated with this page, [Joysticks](/windows/win32/multimedia/joysticks), is a legacy feature. It has been superseded by [Windows.Gaming.Input Namespace](/uwp/api/windows.gaming.input). **Windows.Gaming.Input Namespace** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Windows.Gaming.Input Namespace** instead of **Joysticks**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following example illustrates how an application could respond to joystick movements and changes in the button states. When the joystick changes position, the application moves the cursor and, if either button is pressed, draws a bullet hole on the desktop. When a joystick button is pressed, the application draws a hole on the desktop and plays a sound continuously until a button is released. The messages to watch are [**MM\_JOY1MOVE**](mm-joy1move.md), [**MM\_JOY1BUTTONDOWN**](mm-joy1buttondown.md), and [**MM\_JOY1BUTTONUP**](mm-joy1buttonup.md).


```C++
case MM_JOY1MOVE :                     // changed position 
    if((UINT) wParam & (JOY_BUTTON1 | JOY_BUTTON2)) 
        DrawFire(hWnd); 
    DrawSight(lParam);                 // calculates new cursor position 
    break; 
case MM_JOY1BUTTONDOWN :               // button is down 
    if((UINT) wParam & JOY_BUTTON1) 
    { 
        PlaySound(lpButton1, SND_LOOP | SND_ASYNC | SND_MEMORY); 
        DrawFire(hWnd); 
    } 
    else if((UINT) wParam & JOY_BUTTON2) 
    { 
        PlaySound(lpButton2, SND_ASYNC | SND_MEMORY |  SND_LOOP); 
        DrawFire(hWnd); 
    } 
    break; 
case MM_JOY1BUTTONUP :                 // button is up 
    sndPlaySound(NULL, 0);             // stops the sound 
    break; 

```



 

 




