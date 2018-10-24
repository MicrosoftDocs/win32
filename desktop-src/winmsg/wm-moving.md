---
Description: Sent to a window that the user is moving. By processing this message, an application can monitor the position of the drag rectangle and, if needed, change its position.
ms.assetid: f56a36c1-dbaa-438a-9e52-d12697a9dac9
title: WM_MOVING message
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WM\_MOVING message

Sent to a window that the user is moving. By processing this message, an application can monitor the position of the drag rectangle and, if needed, change its position.

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/en-us/library/ms633573(v=VS.85).aspx) function.


```C++
#define WM_MOVING                       0x0216
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**RECT**](https://msdn.microsoft.com/en-us/library/Dd162897(v=VS.85).aspx) structure with the current position of the window, in screen coordinates. To change the position of the drag rectangle, an application must change the members of this structure.

</dd> </dl>

## Return value

Type: **LRESULT**

An application should return **TRUE** if it processes this message.

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

[**WM\_MOVE**](wm-move.md)
</dt> <dt>

[**WM\_SIZING**](wm-sizing.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**RECT**](https://msdn.microsoft.com/en-us/library/Dd162897(v=VS.85).aspx)
</dt> </dl>

 

 




