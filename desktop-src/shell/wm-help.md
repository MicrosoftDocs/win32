---
Description: Indicates that the user pressed the F1 key.
ms.assetid: 6a090125-67dd-4267-9973-10e32c6e4f1f
title: WM\_HELP message
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WM\_HELP message

Indicates that the user pressed the F1 key. If a menu is active when F1 is pressed, **WM\_HELP** is sent to the window associated with the menu; otherwise, **WM\_HELP** is sent to the window that has the keyboard focus. If no window has the keyboard focus, **WM\_HELP** is sent to the currently active window.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lphi* 
</dt> <dd>

The address of a [**HELPINFO**](/windows/desktop/api/Winuser/ns-winuser-taghelpinfo) structure that contains information about the menu item, control, dialog box, or window for which Help is requested.

</dd> </dl>

## Return value

Returns **TRUE**.

## Remarks

The [**DefWindowProc**](https://msdn.microsoft.com/windows/desktop/fcc6b242-e152-4364-a977-b0441bec425f) function passes **WM\_HELP** to the parent window of a child window or to the owner of a top-level window.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Winuser.h</dt> </dl> |



 

 




