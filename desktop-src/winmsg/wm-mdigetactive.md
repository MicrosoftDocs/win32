---
description: An application sends the WM\_MDIGETACTIVE message to a multiple-document interface (MDI) client window to retrieve the handle to the active MDI child window.
ms.assetid: 3ee445be-dd55-4825-8508-fa18a346ffcd
title: WM_MDIGETACTIVE message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_MDIGETACTIVE message

An application sends the **WM\_MDIGETACTIVE** message to a multiple-document interface (MDI) client window to retrieve the handle to the active MDI child window.


```C++
#define WM_MDIGETACTIVE                  0x0229
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

The maximized state. If this parameter is not **NULL**, it is a pointer to a value that indicates the maximized state of the MDI child window. If the value is **TRUE**, the window is maximized; a value of **FALSE** indicates that it is not. If this parameter is **NULL**, the parameter is ignored.

</dd> </dl>

## Return value

Type: **HWND**

The return value is the handle to the active MDI child window.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Multiple Document Interface Overview](multiple-document-interface.md)
</dt> </dl>

 

 




