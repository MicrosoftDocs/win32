---
title: Up-Down Control Styles (CommCtrl.h)
description: This section lists the styles used when creating up-down controls.
ms.assetid: d35198cb-6a5b-485e-a914-1b2ede53462f
topic_type:
- apiref
api_name:
- UDS_ALIGNLEFT
- UDS_ALIGNRIGHT
- UDS_ARROWKEYS
- UDS_AUTOBUDDY
- UDS_HORZ
- UDS_HOTTRACK
- UDS_NOTHOUSANDS
- UDS_SETBUDDYINT
- UDS_WRAP
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Up-Down Control Styles

This section lists the styles used when creating up-down controls.



| Constant                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                               |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="UDS_ALIGNLEFT"></span><span id="uds_alignleft"></span><dl> <dt>**UDS\_ALIGNLEFT**</dt> </dl>       | Positions the up-down control next to the left edge of the buddy window. The buddy window is moved to the right, and its width is decreased to accommodate the width of the up-down control.<br/>                                                                                                                                                                                                   |
| <span id="UDS_ALIGNRIGHT"></span><span id="uds_alignright"></span><dl> <dt>**UDS\_ALIGNRIGHT**</dt> </dl>    | Positions the up-down control next to the right edge of the buddy window. The width of the buddy window is decreased to accommodate the width of the up-down control.<br/>                                                                                                                                                                                                                          |
| <span id="UDS_ARROWKEYS"></span><span id="uds_arrowkeys"></span><dl> <dt>**UDS\_ARROWKEYS**</dt> </dl>       | Causes the up-down control to increment and decrement the position when the UP ARROW and DOWN ARROW keys are pressed.<br/>                                                                                                                                                                                                                                                                          |
| <span id="UDS_AUTOBUDDY"></span><span id="uds_autobuddy"></span><dl> <dt>**UDS\_AUTOBUDDY**</dt> </dl>       | Automatically selects the previous window in the z-order as the up-down control's buddy window.<br/>                                                                                                                                                                                                                                                                                                |
| <span id="UDS_HORZ"></span><span id="uds_horz"></span><dl> <dt>**UDS\_HORZ**</dt> </dl>                      | Causes the up-down control's arrows to point left and right instead of up and down.<br/>                                                                                                                                                                                                                                                                                                            |
| <span id="UDS_HOTTRACK"></span><span id="uds_hottrack"></span><dl> <dt>**UDS\_HOTTRACK**</dt> </dl>          | Causes the control to exhibit "hot tracking" behavior. That is, it highlights the UP ARROW and DOWN ARROW on the control as the pointer passes over them. This style requires Windows 98 or Windows 2000. If the system is running Windows 95 or Windows NT 4.0, the flag is ignored. To check whether hot tracking is enabled, call [**SystemParametersInfo**](/windows/desktop/api/winuser/nf-winuser-systemparametersinfoa). <br/> |
| <span id="UDS_NOTHOUSANDS"></span><span id="uds_nothousands"></span><dl> <dt>**UDS\_NOTHOUSANDS**</dt> </dl> | Does not insert a thousands separator between every three decimal digits. <br/>                                                                                                                                                                                                                                                                                                                     |
| <span id="UDS_SETBUDDYINT"></span><span id="uds_setbuddyint"></span><dl> <dt>**UDS\_SETBUDDYINT**</dt> </dl> | Causes the up-down control to set the text of the buddy window (using the [**WM\_SETTEXT**](/windows/desktop/winmsg/wm-settext) message) when the position changes. The text consists of the position formatted as a decimal or hexadecimal string.<br/>                                                                                                                                                             |
| <span id="UDS_WRAP"></span><span id="uds_wrap"></span><dl> <dt>**UDS\_WRAP**</dt> </dl>                      | Causes the position to "wrap" if it is incremented or decremented beyond the ending or beginning of the range.<br/>                                                                                                                                                                                                                                                                                 |



## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>CommCtrl.h</dt> </dl> |



 

