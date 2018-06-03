---
Description: Sent when the window background must be erased (for example, when a window is resized). The message is sent to prepare an invalidated portion of a window for painting.
ms.assetid: 3bdc37da-227c-4be1-bf0b-99704b8acbe1
title: WM\_ERASEBKGND message
ms.technology: desktop
ms.prod: windows
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

The [**DefWindowProc**](/windows/desktop/api/Winuser/nf-winuser-defwindowproca) function erases the background by using the class background brush specified by the **hbrBackground** member of the [**WNDCLASS**](/windows/desktop/api/Winuser/ns-winuser-tagwndclassa) structure. If **hbrBackground** is **NULL**, the application should process the **WM\_ERASEBKGND** message and erase the background.

An application should return nonzero in response to **WM\_ERASEBKGND** if it processes the message and erases the background; this indicates that no further erasing is required. If the application returns zero, the window will remain marked for erasing. (Typically, this indicates that the **fErase** member of the [**PAINTSTRUCT**](https://msdn.microsoft.com/windows/desktop/1f8c6dd2-e511-48f2-8ab0-d2fadb1ce433) structure will be **TRUE**.)

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

[**DefWindowProc**](/windows/desktop/api/Winuser/nf-winuser-defwindowproca)
</dt> <dt>

[**WNDCLASS**](/windows/desktop/api/Winuser/ns-winuser-tagwndclassa)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Icons](https://msdn.microsoft.com/windows/desktop/1dc588f4-b032-40a8-82ef-5b9fc04abb0b)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**BeginPaint**](https://msdn.microsoft.com/windows/desktop/513341d7-bed8-469c-a067-ee71dc8860f9)
</dt> <dt>

[**PAINTSTRUCT**](https://msdn.microsoft.com/windows/desktop/1f8c6dd2-e511-48f2-8ab0-d2fadb1ce433)
</dt> </dl>

 

 




