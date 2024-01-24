---
title: MM_JOY1MOVE message (Mmsystem.h)
description: The MM\_JOY1MOVE message notifies the window that has captured joystick JOYSTICKID1 that the joystick position has changed.
ms.assetid: 317ac0b2-f873-413d-b071-47d840229643
keywords:
- MM_JOY1MOVE message Windows Multimedia
topic_type:
- apiref
api_name:
- MM_JOY1MOVE
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MM\_JOY1MOVE message

The **MM\_JOY1MOVE** message notifies the window that has captured joystick JOYSTICKID1 that the joystick position has changed.


```C++
MM_JOY1MOVE 
fwButtons = wParam; 
xPos = LOWORD(lParam); 
yPos = HIWORD(lParam); 
```



## Parameters

<dl> <dt>

<span id="fwButtons"></span><span id="fwbuttons"></span><span id="FWBUTTONS"></span>*fwButtons*
</dt> <dd>

Identifies the buttons that are pressed. It can be one or more of the following values:



| Requirement | Value |
|--------------|------------------------------------|
| JOY\_BUTTON1 | First joystick button is pressed.  |
| JOY\_BUTTON2 | Second joystick button is pressed. |
| JOY\_BUTTON3 | Third joystick button is pressed.  |
| JOY\_BUTTON4 | Fourth joystick button is pressed. |



 

</dd> <dt>

<span id="xPos"></span><span id="xpos"></span><span id="XPOS"></span>*xPos*
</dt> <dd>

The x-coordinates of the joystick relative to the upper left corner of the client area.

</dd> <dt>

<span id="yPos"></span><span id="ypos"></span><span id="YPOS"></span>*yPos*
</dt> <dd>

The y-coordinate of the joystick relative to the upper left corner of the client area.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Mmsystem.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Joysticks](joysticks.md)
</dt> <dt>

[Multimedia Joystick Messages](multimedia-joystick-messages.md)
</dt> </dl>

 

 





