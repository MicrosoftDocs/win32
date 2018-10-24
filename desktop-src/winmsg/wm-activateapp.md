---
Description: Sent when a window belonging to a different application than the active window is about to be activated. The message is sent to the application whose window is being activated and to the application whose window is being deactivated.
ms.assetid: fc3626ac-8f19-4aa6-8fe9-5020d00c09db
title: WM_ACTIVATEAPP message
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WM\_ACTIVATEAPP message

Sent when a window belonging to a different application than the active window is about to be activated. The message is sent to the application whose window is being activated and to the application whose window is being deactivated.

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/en-us/library/ms633573(v=VS.85).aspx) function.


```C++
#define WM_ACTIVATEAPP                  0x001C
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Indicates whether the window is being activated or deactivated. This parameter is **TRUE** if the window is being activated; it is **FALSE** if the window is being deactivated.

</dd> <dt>

*lParam* 
</dt> <dd>

The thread identifier. If the *wParam* parameter is **TRUE**, *lParam* is the identifier of the thread that owns the window being deactivated. If *wParam* is **FALSE**, *lParam* is the identifier of the thread that owns the window being activated.

</dd> </dl>

## Return value

Type: **LRESULT**

If an application processes this message, it should return zero.

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

[**WM\_ACTIVATE**](https://msdn.microsoft.com/en-us/library/ms646274(v=VS.85).aspx)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> </dl>

 

 




