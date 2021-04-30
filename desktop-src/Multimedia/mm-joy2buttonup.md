---
title: MM_JOY2BUTTONUP message (Mmsystem.h)
description: The MM\_JOY2BUTTONUP message notifies the window that has captured joystick JOYSTICKID2 that a button has been released.
ms.assetid: da024466-7cd3-42ec-90a7-1468eb42841e
keywords:
- MM_JOY2BUTTONUP message Windows Multimedia
topic_type:
- apiref
api_name:
- MM_JOY2BUTTONUP
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MM\_JOY2BUTTONUP message

The **MM\_JOY2BUTTONUP** message notifies the window that has captured joystick JOYSTICKID2 that a button has been released.


```C++
MM_JOY2BUTTONUP 
fwButton = wParam; 
xPos = LOWORD(lParam); 
yPos = HIWORD(lParam); 
```



## Parameters

<dl> <dt>

**fwButtons** 
</dt> <dd>

Identifies the button that has changed state and the buttons that are pressed. It can be one of the following:



| Value                                                                                                                                                            | Meaning                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| <span id="JOY_BUTTON1CHG"></span><span id="joy_button1chg"></span><dl> <dt>**JOY\_BUTTON1CHG**</dt> </dl> | First joystick button has changed state.<br/>  |
| <span id="JOY_BUTTON2CHG"></span><span id="joy_button2chg"></span><dl> <dt>**JOY\_BUTTON2CHG**</dt> </dl> | Second joystick button has changed state.<br/> |
| <span id="JOY_BUTTON3CHG"></span><span id="joy_button3chg"></span><dl> <dt>**JOY\_BUTTON3CHG**</dt> </dl> | Third joystick button has changed state.<br/>  |
| <span id="JOY_BUTTON4CHG"></span><span id="joy_button4chg"></span><dl> <dt>**JOY\_BUTTON4CHG**</dt> </dl> | Fourth joystick button has changed state.<br/> |



 

and one or more of the following:



| Value                                                                                                                                                   | Meaning                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| <span id="JOY_BUTTON1"></span><span id="joy_button1"></span><dl> <dt>**JOY\_BUTTON1**</dt> </dl> | First joystick button is pressed.<br/>  |
| <span id="JOY_BUTTON2"></span><span id="joy_button2"></span><dl> <dt>**JOY\_BUTTON2**</dt> </dl> | Second joystick button is pressed.<br/> |
| <span id="JOY_BUTTON3"></span><span id="joy_button3"></span><dl> <dt>**JOY\_BUTTON3**</dt> </dl> | Third joystick button is pressed.<br/>  |
| <span id="JOY_BUTTON4"></span><span id="joy_button4"></span><dl> <dt>**JOY\_BUTTON4**</dt> </dl> | Fourth joystick button is pressed.<br/> |



 

</dd> <dt>

**xPos** 
</dt> <dd>

The x-coordinates of the joystick relative to the upper left corner of the client area.

</dd> <dt>

**yPos** 
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

 

 





