---
Description: Sent prior to the WM\_CREATE message when a window is first created.
ms.assetid: 5dd0eda3-83a6-4077-a7a3-e371c9413b0f
title: WM_NCCREATE message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_NCCREATE message

Sent prior to the [**WM\_CREATE**](wm-create.md) message when a window is first created.

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/en-us/library/ms633573(v=VS.85).aspx) function.


```C++
#define WM_NCCREATE                     0x0081
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to the [**CREATESTRUCT**](https://msdn.microsoft.com/en-us/library/ms632603(v=VS.85).aspx) structure that contains information about the window being created. The members of **CREATESTRUCT** are identical to the parameters of the [**CreateWindowEx**](https://msdn.microsoft.com/en-us/library/ms632680(v=VS.85).aspx) function.

</dd> </dl>

## Return value

Type: **LRESULT**

If an application processes this message, it should return **TRUE** to continue creation of the window. If the application returns **FALSE**, the [**CreateWindow**](https://msdn.microsoft.com/en-us/library/ms632679(v=VS.85).aspx) or [**CreateWindowEx**](https://msdn.microsoft.com/en-us/library/ms632680(v=VS.85).aspx) function will return a **NULL** handle.

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

[**CreateWindow**](https://msdn.microsoft.com/en-us/library/ms632679(v=VS.85).aspx)
</dt> <dt>

[**CreateWindowEx**](https://msdn.microsoft.com/en-us/library/ms632680(v=VS.85).aspx)
</dt> <dt>

[**DefWindowProc**](https://msdn.microsoft.com/en-us/library/ms633572(v=VS.85).aspx)
</dt> <dt>

[**CREATESTRUCT**](https://msdn.microsoft.com/en-us/library/ms632603(v=VS.85).aspx)
</dt> <dt>

[**WM\_CREATE**](wm-create.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> </dl>

 

 




