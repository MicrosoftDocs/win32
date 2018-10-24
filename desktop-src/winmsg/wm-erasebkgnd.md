---
Description: Sent when the window background must be erased (for example, when a window is resized). The message is sent to prepare an invalidated portion of a window for painting.
ms.assetid: 3bdc37da-227c-4be1-bf0b-99704b8acbe1
title: WM_ERASEBKGND message
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WM\_ERASEBKGND message

Sent when the window background must be erased (for example, when a window is resized). The message is sent to prepare an invalidated portion of a window for painting.


```C++
#define WM_ERASEBKGND                   0x0014
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the device context.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

Type: **LRESULT**

An application should return nonzero if it erases the background; otherwise, it should return zero.

## Remarks

The [**DefWindowProc**](https://msdn.microsoft.com/en-us/library/ms633572(v=VS.85).aspx) function erases the background by using the class background brush specified by the **hbrBackground** member of the [**WNDCLASS**](https://msdn.microsoft.com/en-us/library/ms633576(v=VS.85).aspx) structure. If **hbrBackground** is **NULL**, the application should process the **WM\_ERASEBKGND** message and erase the background.

An application should return nonzero in response to **WM\_ERASEBKGND** if it processes the message and erases the background; this indicates that no further erasing is required. If the application returns zero, the window will remain marked for erasing. (Typically, this indicates that the **fErase** member of the [**PAINTSTRUCT**](https://msdn.microsoft.com/en-us/library/Dd162768(v=VS.85).aspx) structure will be **TRUE**.)

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

[**DefWindowProc**](https://msdn.microsoft.com/en-us/library/ms633572(v=VS.85).aspx)
</dt> <dt>

[**WNDCLASS**](https://msdn.microsoft.com/en-us/library/ms633576(v=VS.85).aspx)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Icons](https://msdn.microsoft.com/en-us/library/ms646973(v=VS.85).aspx)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**BeginPaint**](https://msdn.microsoft.com/en-us/library/Dd183362(v=VS.85).aspx)
</dt> <dt>

[**PAINTSTRUCT**](https://msdn.microsoft.com/en-us/library/Dd162768(v=VS.85).aspx)
</dt> </dl>

 

 




