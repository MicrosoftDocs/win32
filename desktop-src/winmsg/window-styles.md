---
description: The following are the window styles. After the window has been created, these styles cannot be modified, except as noted.
ms.assetid: 'vs|winui|~\winui\windowsuserinterface\windowing\windows\windowreference\windowstyles.htm'
title: Window Styles (Winuser.h)
ms.topic: article
ms.date: 10/26/2021
---

# Window Styles

The following are the window styles. After the window has been created, these styles cannot be modified, except as noted.

| Constant name            | Constant value | Description                       |
|:------------------------:|:--------------:|-----------------------------------|
| **WS\_BORDER**           | 0x00800000L    | The window has a thin-line border |
| **WS\_CAPTION**          | 0x00C00000L    | The window has a title bar (includes the **WS\_BORDER** style). |
| **WS\_CHILD**            | 0x40000000L    | The window is a child window. A window with this style cannot have a menu bar. This style cannot be used with the **WS\_POPUP** style. |
| **WS\_CHILDWINDOW**      | 0x40000000L    | Same as the **WS\_CHILD** style. |
| **WS\_CLIPCHILDREN**     | 0x02000000L    | Excludes the area occupied by child windows when drawing occurs within the parent window. This style is used when creating the parent window. |
| **WS\_CLIPSIBLINGS**     | 0x04000000L    | Clips child windows relative to each other; that is, when a particular child window receives a [**WM\_PAINT**](../gdi/wm-paint.md) message, the **WS\_CLIPSIBLINGS** style clips all other overlapping child windows out of the region of the child window to be updated. If **WS\_CLIPSIBLINGS** is not specified and child windows overlap, it is possible, when drawing within the client area of a child window, to draw within the client area of a neighboring child window. |
| **WS\_DISABLED**         | 0x08000000L    | The window is initially disabled. A disabled window cannot receive input from the user. To change this after a window has been created, use the [**EnableWindow**](/windows/win32/api/winuser/nf-winuser-enablewindow) function. |
| **WS\_DLGFRAME**         | 0x00400000L    | The window has a border of a style typically used with dialog boxes. A window with this style cannot have a title bar. |
| **WS\_GROUP**            | 0x00020000L    | The window is the first control of a group of controls. The group consists of this first control and all controls defined after it, up to the next control with the **WS\_GROUP** style. The first control in each group usually has the **WS\_TABSTOP** style so that the user can move from group to group. The user can subsequently change the keyboard focus from one control in the group to the next control in the group by using the direction keys.<br/> You can turn this style on and off to change dialog box navigation. To change this style after a window has been created, use the [**SetWindowLong**](/windows/win32/api/winuser/nf-winuser-setwindowlonga) function. |
| **WS\_HSCROLL**          | 0x00100000L    | The window has a horizontal scroll bar. |
| **WS\_ICONIC**           | 0x20000000L    | The window is initially minimized. Same as the **WS\_MINIMIZE** style. |
| **WS\_MAXIMIZE**         | 0x01000000L    | The window is initially maximized. |
| **WS\_MAXIMIZEBOX**      | 0x00010000L    | The window has a maximize button. Cannot be combined with the **WS\_EX\_CONTEXTHELP** style. The **WS\_SYSMENU** style must also be specified. |
| **WS\_MINIMIZE**         | 0x20000000L    | The window is initially minimized. Same as the **WS\_ICONIC** style. |
| **WS\_MINIMIZEBOX**      | 0x00020000L    | The window has a minimize button. Cannot be combined with the **WS\_EX\_CONTEXTHELP** style. The **WS\_SYSMENU** style must also be specified. |
| **WS\_OVERLAPPED**       | 0x00000000L    | The window is an overlapped window. An overlapped window has a title bar and a border. Same as the **WS\_TILED** style. |
| **WS\_OVERLAPPEDWINDOW** | (WS\_OVERLAPPED \| WS\_CAPTION \| WS\_SYSMENU \| WS\_THICKFRAME \| WS\_MINIMIZEBOX \| WS\_MAXIMIZEBOX) | The window is an overlapped window. Same as the **WS\_TILEDWINDOW** style. |
| **WS\_POPUP**            | 0x80000000L    | The window is a pop-up window. This style cannot be used with the **WS\_CHILD** style. |
| **WS\_POPUPWINDOW**      | (WS\_POPUP \| WS\_BORDER \| WS\_SYSMENU) | The window is a pop-up window. The **WS\_CAPTION** and **WS\_POPUPWINDOW** styles must be combined to make the window menu visible. |
| **WS\_SIZEBOX**          | 0x00040000L    | The window has a sizing border. Same as the **WS\_THICKFRAME** style. |
| **WS\_SYSMENU**          | 0x00080000L    | The window has a window menu on its title bar. The **WS\_CAPTION** style must also be specified. |
| **WS\_TABSTOP**          | 0x00010000L    | The window is a control that can receive the keyboard focus when the user presses the TAB key. Pressing the TAB key changes the keyboard focus to the next control with the **WS\_TABSTOP** style.<br/> You can turn this style on and off to change dialog box navigation. To change this style after a window has been created, use the [**SetWindowLong**](/windows/win32/api/winuser/nf-winuser-setwindowlonga) function. For user-created windows and modeless dialogs to work with tab stops, alter the message loop to call the [**IsDialogMessage**](/windows/win32/api/winuser/nf-winuser-isdialogmessagea) function.<br/>           |
| **WS\_THICKFRAME**       | 0x00040000L    | The window has a sizing border. Same as the **WS\_SIZEBOX** style. |
| **WS\_TILED**            | 0x00000000L    | The window is an overlapped window. An overlapped window has a title bar and a border. Same as the **WS\_OVERLAPPED** style. |
| **WS\_TILEDWINDOW**      | (WS\_OVERLAPPED \| WS\_CAPTION \| WS\_SYSMENU \| WS\_THICKFRAME \| WS\_MINIMIZEBOX \| WS\_MAXIMIZEBOX)                | The window is an overlapped window. Same as the **WS\_OVERLAPPEDWINDOW** style. |
| **WS\_VISIBLE**          | 0x10000000L    | The window is initially visible.<br/> This style can be turned on and off by using the [**ShowWindow**](/windows/win32/api/winuser/nf-winuser-showwindow) or [**SetWindowPos**](/windows/win32/api/winuser/nf-winuser-setwindowpos) function. |
| **WS\_VSCROLL**          | 0x00200000L    | The window has a vertical scroll bar. |

## Requirements

| Requirement              | Value                                           |
|--------------------------|-------------------------------------------------|
| Minimum supported client | Windows 2000 Professional \[desktop apps only\] |
| Minimum supported server | Windows 2000 Server \[desktop apps only\]       |
| Header                   | Winuser.h (include Windows.h)                   |
