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
ms.date: 05/31/2018
---

# Processing Joystick Messages

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



 

 




