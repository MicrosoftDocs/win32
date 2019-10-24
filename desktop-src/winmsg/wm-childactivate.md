---
Description: Sent to a child window when the user clicks the window's title bar or when the window is activated, moved, or sized.
ms.assetid: 6e60725d-aa01-48bb-86a5-f17f56b97d35
title: WM_CHILDACTIVATE message
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CHILDACTIVATE message

Sent to a child window when the user clicks the window's title bar or when the window is activated, moved, or sized.

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/en-us/library/ms633573(v=VS.85).aspx) function.


```C++
#define WM_CHILDACTIVATE                0x0022
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

[**MoveWindow**](https://msdn.microsoft.com/en-us/library/ms633534(v=VS.85).aspx)
</dt> <dt>

[**SetWindowPos**](https://msdn.microsoft.com/en-us/library/ms633545(v=VS.85).aspx)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> </dl>

 

 




