---
Description: Sent to a minimized (iconic) window.
ms.assetid: e4f0e638-f606-4745-888b-14a846c7fd37
title: WM_QUERYDRAGICON message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_QUERYDRAGICON message

Sent to a minimized (iconic) window. The window is about to be dragged by the user but does not have an icon defined for its class. An application can return a handle to an icon or cursor. The system displays this cursor or icon while the user drags the icon.

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/library/ms633573(v=VS.85).aspx) function.


```C++
#define WM_QUERYDRAGICON                0x0037
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

Type: **LRESULT**

An application should return a handle to a cursor or icon that the system is to display while the user drags the icon. The cursor or icon must be compatible with the display driver's resolution. If the application returns **NULL**, the system displays the default cursor.

## Remarks

When the user drags the icon of a window without a class icon, the system replaces the icon with a default cursor. If the application requires a different cursor to be displayed during dragging, it must return a handle to the cursor or icon compatible with the display driver's resolution. If an application returns a handle to a color cursor or icon, the system converts the cursor or icon to black and white. The application can call the [**LoadCursor**](https://msdn.microsoft.com/library/ms648391(v=VS.85).aspx) or [**LoadIcon**](https://msdn.microsoft.com/library/ms648072(v=VS.85).aspx) function to load a cursor or icon from the resources in its executable (.exe) file and to retrieve this handle.

If a dialog box procedure handles this message, it should cast the desired return value to a **BOOL** and return the value directly. The **DWL\_MSGRESULT** value set by the [**SetWindowLong**](https://msdn.microsoft.com/library/ms633591(v=VS.85).aspx) function is ignored.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**LoadCursor**](https://msdn.microsoft.com/library/ms648391(v=VS.85).aspx)
</dt> <dt>

[**LoadIcon**](https://msdn.microsoft.com/library/ms648072(v=VS.85).aspx)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> </dl>

 

 




