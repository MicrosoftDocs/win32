---
title: Up-Down Control
description: This section contains information about the programming elements used with up-down controls.
ms.assetid: 48c6b4bd-65b4-4388-959e-efffa7658274
ms.topic: article
ms.date: 05/31/2018
---

# Up-Down Control

This section contains information about the programming elements used with up-down controls.

### Overviews



| Topic                                    | Contents                                                                                                                                                                                                            |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Up-Down Controls](up-down-controls.md) | An up-down control is a pair of arrow buttons that the user can click to increment or decrement a value, such as a scroll position or a number displayed in a companion control (called a buddy window).<br/> |



 

### Functions



| Topic                                              | Contents                                                                                                                                                |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateUpDownControl**](/windows/desktop/api/Commctrl/nf-commctrl-createupdowncontrol) | Creates an up-down control. Note: This function is obsolete. It is a 16 bit function and cannot handle 32 bit values for range and position.<br/> |



 

### Messages



| Topic                                                 | Contents                                                                                                                                                                                                                               |
|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UDM\_GETACCEL**](udm-getaccel.md)                 | Retrieves acceleration information for an up-down control. <br/>                                                                                                                                                                 |
| [**UDM\_GETBASE**](udm-getbase.md)                   | Retrieves the current radix base (that is, either base 10 or 16) for an up-down control. <br/>                                                                                                                                   |
| [**UDM\_GETBUDDY**](udm-getbuddy.md)                 | Retrieves the handle to the current buddy window. <br/>                                                                                                                                                                          |
| [**UDM\_GETPOS**](udm-getpos.md)                     | Retrieves the current position of an up-down control with 16-bit precision. <br/>                                                                                                                                                |
| [**UDM\_GETPOS32**](udm-getpos32.md)                 | Returns the 32-bit position of an up-down control.<br/>                                                                                                                                                                          |
| [**UDM\_GETRANGE**](udm-getrange.md)                 | Retrieves the minimum and maximum positions (range) for an up-down control. <br/>                                                                                                                                                |
| [**UDM\_GETRANGE32**](udm-getrange32.md)             | Retrieves the 32-bit range of an up-down control. <br/>                                                                                                                                                                          |
| [**UDM\_GETUNICODEFORMAT**](udm-getunicodeformat.md) | Retrieves the Unicode character format flag for the control. <br/>                                                                                                                                                               |
| [**UDM\_SETACCEL**](udm-setaccel.md)                 | Sets the acceleration for an up-down control. <br/>                                                                                                                                                                              |
| [**UDM\_SETBASE**](udm-setbase.md)                   | Sets the radix base for an up-down control. The base value determines whether the buddy window displays numbers in decimal or hexadecimal digits. Hexadecimal numbers are always unsigned, and decimal numbers are signed. <br/> |
| [**UDM\_SETBUDDY**](udm-setbuddy.md)                 | Sets the buddy window for an up-down control. <br/>                                                                                                                                                                              |
| [**UDM\_SETPOS**](udm-setpos.md)                     | Sets the current position for an up-down control with 16-bit precision. <br/>                                                                                                                                                    |
| [**UDM\_SETPOS32**](udm-setpos32.md)                 | Sets the position of an up-down control with 32-bit precision.<br/>                                                                                                                                                              |
| [**UDM\_SETRANGE**](udm-setrange.md)                 | Sets the minimum and maximum positions (range) for an up-down control.<br/>                                                                                                                                                      |
| [**UDM\_SETRANGE32**](udm-setrange32.md)             | Sets the 32-bit range of an up-down control. <br/>                                                                                                                                                                               |
| [**UDM\_SETUNICODEFORMAT**](udm-setunicodeformat.md) | Sets the Unicode character format flag for the control. This message allows you to change the character set used by the control at run time rather than having to re-create the control. <br/>                                   |



 

### Notifications



| Topic                                                            | Contents                                                                                                                                                                                                                                                                                                                                                       |
|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [NM\_RELEASEDCAPTURE (up-down)](nm-releasedcapture-up-down-.md) | Notifies an up-down control's parent window that the control is releasing mouse capture. This notification is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                                                                                                                       |
| [UDN\_DELTAPOS](udn-deltapos.md)                                | Sent by the operating system to the parent window of an up-down control when the position of the control is about to change. This happens when the user requests a change in the value by pressing the control's up or down arrow. The [UDN\_DELTAPOS](udn-deltapos.md) message is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/> |



 

### Structures



| Topic                        | Contents                                                                                                                                          |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NMUPDOWN**](/windows/win32/api/commctrl/ns-commctrl-nmupdown) | Contains information specific to up-down control notification messages. It is identical to and replaces the **NM\_UPDOWN** structure. <br/> |
| [**UDACCEL**](/windows/desktop/api/Commctrl/ns-commctrl-udaccel)   | Contains acceleration information for an up-down control. <br/>                                                                             |



 

### Constants



| Topic                                                | Contents                                                                      |
|------------------------------------------------------|-------------------------------------------------------------------------------|
| [Up-Down Control Styles](up-down-control-styles.md) | This section lists the styles used when creating up-down controls.<br/> |



 

 

 





