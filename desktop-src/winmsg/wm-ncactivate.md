---
Description: Sent to a window when its nonclient area needs to be changed to indicate an active or inactive state.
ms.assetid: d25732b9-b9ab-4754-a4cf-002d32e3945e
title: WM_NCACTIVATE message
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_NCACTIVATE message

Sent to a window when its nonclient area needs to be changed to indicate an active or inactive state.

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/en-us/library/ms633573(v=VS.85).aspx) function.


```C++
#define WM_NCACTIVATE                   0x0086
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Indicates when a title bar or icon needs to be changed to indicate an active or inactive state. If an active title bar or icon is to be drawn, the *wParam* parameter is **TRUE**. If an inactive title bar or icon is to be drawn, *wParam* is **FALSE**.

</dd> <dt>

*lParam* 
</dt> <dd>

When a [visual style](https://msdn.microsoft.com/library/Bb773187(v=VS.85).aspx) is active for this window, this parameter is not used.

When a visual style is not active for this window, this parameter is a handle to an optional update region for the nonclient area of the window. If this parameter is set to -1, [**DefWindowProc**](https://msdn.microsoft.com/en-us/library/ms633572(v=VS.85).aspx) does not repaint the nonclient area to reflect the state change.

</dd> </dl>

## Return value

Type: **LRESULT**

When the *wParam* parameter is **FALSE**, an application should return **TRUE** to indicate that the system should proceed with the default processing, or it should return **FALSE** to prevent the change. When *wParam* is **TRUE**, the return value is ignored.

## Remarks

Processing messages related to the nonclient area of a standard window is not recommended, because the application must be able to draw all the required parts of the nonclient area for the window. If an application does process this message, it must return **TRUE** to direct the system to complete the change of active window. If the window is minimized when this message is received, the application should pass the message to the [**DefWindowProc**](https://msdn.microsoft.com/en-us/library/ms633572(v=VS.85).aspx) function.

The [**DefWindowProc**](https://msdn.microsoft.com/en-us/library/ms633572(v=VS.85).aspx) function draws the title bar or icon title in its active colors when the *wParam* parameter is **TRUE** and in its inactive colors when *wParam* is **FALSE**.

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

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> </dl>

 

 




