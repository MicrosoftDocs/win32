---
title: Pager
description: This section contains information about the programming elements used with pager controls.
ms.assetid: 0da466c6-129e-4092-9d26-579b98f38795
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Pager

This section contains information about the programming elements used with pager controls.

### Overviews



| Topic                                | Contents                                                                                                                                         |
|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| [Pager Controls](pager-controls.md) | A *pager control* is a window container that is used with a window that does not have enough display area to show all of its content.<br/> |



 

### Macros



| Topic                                                 | Contents                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Pager\_ForwardMouse**](/windows/win32/Commctrl/nf-commctrl-pager_forwardmouse?branch=master)     | Enables or disables mouse forwarding for the pager control. When mouse forwarding is enabled, the pager control forwards [**WM\_MOUSEMOVE**](https://msdn.microsoft.com/library/windows/desktop/ms645616) messages to the contained window. You can use this macro or send the [**PGM\_FORWARDMOUSE**](pgm-forwardmouse.md) message explicitly. <br/>                                                                                                                     |
| [**Pager\_GetBkColor**](/windows/win32/Commctrl/nf-commctrl-pager_getbkcolor?branch=master)         | Retrieves the current background color for the pager control. You can use this macro or send the [**PGM\_GETBKCOLOR**](pgm-getbkcolor.md) message explicitly. <br/>                                                                                                                                                                                                                                                                 |
| [**Pager\_GetBorder**](/windows/win32/Commctrl/nf-commctrl-pager_getborder?branch=master)           | Retrieves the current border size for the pager control. You can use this macro or send the [**PGM\_GETBORDER**](pgm-getborder.md) message explicitly. <br/>                                                                                                                                                                                                                                                                        |
| [**Pager\_GetButtonSize**](/windows/win32/Commctrl/nf-commctrl-pager_getbuttonsize?branch=master)   | Retrieves the current button size for the pager control. You can use this macro or send the [**PGM\_GETBUTTONSIZE**](pgm-getbuttonsize.md) message explicitly. <br/>                                                                                                                                                                                                                                                                |
| [**Pager\_GetButtonState**](/windows/win32/Commctrl/nf-commctrl-pager_getbuttonstate?branch=master) | Retrieves the state of the specified button in a pager control. You can use this macro or send the [**PGM\_GETBUTTONSTATE**](pgm-getbuttonstate.md) message explicitly. <br/>                                                                                                                                                                                                                                                       |
| [**Pager\_GetDropTarget**](/windows/win32/Commctrl/nf-commctrl-pager_getdroptarget?branch=master)   | Retrieves a pager control's [**IDropTarget**](https://msdn.microsoft.com/library/windows/desktop/ms679679) interface pointer. You can use this macro or send the [**PGM\_GETDROPTARGET**](pgm-getdroptarget.md) message explicitly. <br/>                                                                                                                                                                                                                                       |
| [**Pager\_GetPos**](/windows/win32/Commctrl/nf-commctrl-pager_getpos?branch=master)                 | Retrieves the current scroll position of the pager control. You can use this macro or send the [**PGM\_GETPOS**](pgm-getpos.md) message explicitly. <br/>                                                                                                                                                                                                                                                                           |
| [**Pager\_RecalcSize**](/windows/win32/Commctrl/nf-commctrl-pager_recalcsize?branch=master)         | Forces the pager control to recalculate the size of the contained window. Using this macro will result in a [PGN\_CALCSIZE](pgn-calcsize.md) notification being sent. You can use this macro or send the [**PGM\_RECALCSIZE**](pgm-recalcsize.md) message explicitly. <br/>                                                                                                                                                        |
| [**Pager\_SetBkColor**](/windows/win32/Commctrl/nf-commctrl-pager_setbkcolor?branch=master)         | Sets the current background color for the pager control. You can use this macro or send the [**PGM\_SETBKCOLOR**](pgm-setbkcolor.md) message explicitly. <br/>                                                                                                                                                                                                                                                                      |
| [**Pager\_SetBorder**](/windows/win32/Commctrl/nf-commctrl-pager_setborder?branch=master)           | Sets the current border size for the pager control. You can use this macro or send the [**PGM\_SETBORDER**](pgm-setborder.md) message explicitly. <br/>                                                                                                                                                                                                                                                                             |
| [**Pager\_SetButtonSize**](/windows/win32/Commctrl/nf-commctrl-pager_setbuttonsize?branch=master)   | Sets the current button size for the pager control. You can use this macro or send the [**PGM\_SETBUTTONSIZE**](pgm-setbuttonsize.md) message explicitly. <br/>                                                                                                                                                                                                                                                                     |
| [**Pager\_SetChild**](/windows/win32/Commctrl/nf-commctrl-pager_setchild?branch=master)             | Sets the contained window for the pager control. This macro will not change the parent of the contained window; it only assigns a window handle to the pager control for scrolling. In most cases, the contained window will be a child window. If this is the case, the contained window should be a child of the pager control. You can use this macro or send the [**PGM\_SETCHILD**](pgm-setchild.md) message explicitly. <br/> |
| [**Pager\_SetPos**](/windows/win32/Commctrl/nf-commctrl-pager_setpos?branch=master)                 | Sets the scroll position for the pager control. You can use this macro or send the [**PGM\_SETPOS**](pgm-setpos.md) message explicitly. <br/>                                                                                                                                                                                                                                                                                       |
| [**Pager\_SetScrollInfo**](/windows/win32/Commctrl/nf-commctrl-pager_setscrollinfo?branch=master)   | **Intended for internal use; not recommended for use in applications.**<br/> Sets the scrolling parameters of the pager control, including the timeout value, the lines per timeout, and the pixels per line. You can use this macro or send the [**PGM\_SETSETSCROLLINFO**](pgm-setscrollinfo.md) message explicitly. <br/>                                                                                                  |



 

### Messages



| Topic                                              | Contents                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PGM\_FORWARDMOUSE**](pgm-forwardmouse.md)      | Enables or disables mouse forwarding for the pager control. When mouse forwarding is enabled, the pager control forwards [**WM\_MOUSEMOVE**](https://msdn.microsoft.com/library/windows/desktop/ms645616) messages to the contained window. You can send this message explicitly or use the [**Pager\_ForwardMouse**](/windows/win32/Commctrl/nf-commctrl-pager_forwardmouse?branch=master) macro. <br/>                                                                                                                       |
| [**PGM\_GETBKCOLOR**](pgm-getbkcolor.md)          | Retrieves the current background color for the pager control. You can send this message explicitly or use the [**Pager\_GetBkColor**](/windows/win32/Commctrl/nf-commctrl-pager_getbkcolor?branch=master) macro. <br/>                                                                                                                                                                                                                                                                   |
| [**PGM\_GETBORDER**](pgm-getborder.md)            | Retrieves the current border size for the pager control. You can send this message explicitly or use the [**Pager\_GetBorder**](/windows/win32/Commctrl/nf-commctrl-pager_getborder?branch=master) macro. <br/>                                                                                                                                                                                                                                                                          |
| [**PGM\_GETBUTTONSIZE**](pgm-getbuttonsize.md)    | Retrieves the current button size for the pager control. You can send this message explicitly or use the [**Pager\_GetButtonSize**](/windows/win32/Commctrl/nf-commctrl-pager_getbuttonsize?branch=master) macro. <br/>                                                                                                                                                                                                                                                                  |
| [**PGM\_GETBUTTONSTATE**](pgm-getbuttonstate.md)  | Retrieves the state of the specified button in a pager control. You can send this message explicitly or use the [**Pager\_GetButtonState**](/windows/win32/Commctrl/nf-commctrl-pager_getbuttonstate?branch=master) macro. <br/>                                                                                                                                                                                                                                                         |
| [**PGM\_GETDROPTARGET**](pgm-getdroptarget.md)    | Retrieves a pager control's [**IDropTarget**](https://msdn.microsoft.com/library/windows/desktop/ms679679) interface pointer. You can send this message explicitly or use the [**Pager\_GetDropTarget**](/windows/win32/Commctrl/nf-commctrl-pager_getdroptarget?branch=master) macro. <br/>                                                                                                                                                                                                                                         |
| [**PGM\_GETPOS**](pgm-getpos.md)                  | Retrieves the current scroll position of the pager control. You can send this message explicitly or use the [**Pager\_GetPos**](/windows/win32/Commctrl/nf-commctrl-pager_getpos?branch=master) macro. <br/>                                                                                                                                                                                                                                                                             |
| [**PGM\_RECALCSIZE**](pgm-recalcsize.md)          | Forces the pager control to recalculate the size of the contained window. Sending this message will result in a [PGN\_CALCSIZE](pgn-calcsize.md) notification being sent. You can send this message explicitly or use the [**Pager\_RecalcSize**](/windows/win32/Commctrl/nf-commctrl-pager_recalcsize?branch=master) macro. <br/>                                                                                                                                                      |
| [**PGM\_SETBKCOLOR**](pgm-setbkcolor.md)          | Sets the current background color for the pager control. You can send this message explicitly or use the [**Pager\_SetBkColor**](/windows/win32/Commctrl/nf-commctrl-pager_setbkcolor?branch=master) macro. <br/>                                                                                                                                                                                                                                                                        |
| [**PGM\_SETBORDER**](pgm-setborder.md)            | Sets the current border size for the pager control. You can send this message explicitly or use the [**Pager\_SetBorder**](/windows/win32/Commctrl/nf-commctrl-pager_setborder?branch=master) macro. <br/>                                                                                                                                                                                                                                                                               |
| [**PGM\_SETBUTTONSIZE**](pgm-setbuttonsize.md)    | Sets the current button size for the pager control. You can send this message explicitly or use the [**Pager\_SetButtonSize**](/windows/win32/Commctrl/nf-commctrl-pager_setbuttonsize?branch=master) macro. <br/>                                                                                                                                                                                                                                                                       |
| [**PGM\_SETCHILD**](pgm-setchild.md)              | Sets the contained window for the pager control. This message will not change the parent of the contained window; it only assigns a window handle to the pager control for scrolling. In most cases, the contained window will be a child window. If this is the case, the contained window should be a child of the pager control. You can send this message explicitly or use the [**Pager\_SetChild**](/windows/win32/Commctrl/nf-commctrl-pager_setchild?branch=master) macro. <br/> |
| [**PGM\_SETPOS**](pgm-setpos.md)                  | Sets the current scroll position for the pager control. You can send this message explicitly or use the [**Pager\_SetPos**](/windows/win32/Commctrl/nf-commctrl-pager_setpos?branch=master) macro. <br/>                                                                                                                                                                                                                                                                                 |
| [**PGM\_SETSETSCROLLINFO**](pgm-setscrollinfo.md) | **Intended for internal use; not recommended for use in applications.**<br/> Sets the scrolling parameters of the pager control, including the timeout value, the lines per timeout, and the pixels per line. You can send this message explicitly or by using the [**Pager\_SetScrollInfo**](/windows/win32/Commctrl/nf-commctrl-pager_setscrollinfo?branch=master) macro. <br/>                                                                                                  |



 

### Notifications



| Topic                                                        | Contents                                                                                                                                                                                                                                                                                                   |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [NM\_RELEASEDCAPTURE (pager)](nm-releasedcapture-pager-.md) | Notifies a pager control's parent window that the control has released the mouse capture. NM\_RELEASEDCAPTURE is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                                                                |
| [PGN\_CALCSIZE](pgn-calcsize.md)                            | Notification sent by a pager control to obtain the scrollable dimensions of the contained window. These dimensions are used by the pager control to determine the scrollable size of the contained window. This notification is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/> |
| [PGN\_HOTITEMCHANGE](pgn-hotitemchange.md)                  | Sent by a pager control when the hot (highlighted) item changes. <br/>                                                                                                                                                                                                                               |
| [PGN\_SCROLL](pgn-scroll.md)                                | Notification sent by a pager control prior to the contained window being scrolled. This notification is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                                                                         |



 

### Structures



| Topic                                | Contents                                                                                                                                                                                                |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NMPGCALCSIZE**](/windows/win32/Commctrl/ns-commctrl-nmpgcalcsize?branch=master) | Contains and receives information that the pager control uses to calculate the scrollable area of the contained window. It is used with the [PGN\_CALCSIZE](pgn-calcsize.md) notification. <br/> |
| [**NMPGHOTITEM**](/windows/win32/Commctrl/ns-commctrl-tagnmpghotitem?branch=master)   | Contains information used with the [PGN\_HOTITEMCHANGE](pgn-hotitemchange.md) notification. <br/>                                                                                                |
| [**NMPGSCROLL**](/windows/win32/Commctrl/ns-commctrl-nmpgscroll?branch=master)     | Contains and receives information that the pager control uses when scrolling the contained window. It is used with the [PGN\_SCROLL](pgn-scroll.md) notification. <br/>                          |



 

### Constants



| Topic                                            | Contents                                                                            |
|--------------------------------------------------|-------------------------------------------------------------------------------------|
| [Pager Control Styles](pager-control-styles.md) | This section lists the window styles used when creating pager controls. <br/> |



 

 

 





