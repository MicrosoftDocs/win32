---
Description: Sent when an application changes the enabled state of a window.
ms.assetid: df2cf953-121f-43bb-a06c-d10e445bfb5e
title: WM_ENABLE message
ms.topic: article
ms.date: 05/31/2018
---

# WM\_ENABLE message

Sent when an application changes the enabled state of a window. It is sent to the window whose enabled state is changing. This message is sent before the [**EnableWindow**](https://msdn.microsoft.com/en-us/library/ms646291(v=VS.85).aspx) function returns, but after the enabled state ([**WS\_DISABLED**](window-styles.md) style bit) of the window has changed.

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/en-us/library/ms633573(v=VS.85).aspx) function.


```C++
#define WM_ENABLE                       0x000A
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Indicates whether the window has been enabled or disabled. This parameter is **TRUE** if the window has been enabled or **FALSE** if the window has been disabled.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

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

[**EnableWindow**](https://msdn.microsoft.com/en-us/library/ms646291(v=VS.85).aspx)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> </dl>

 

 




