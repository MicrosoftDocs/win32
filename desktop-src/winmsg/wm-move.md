---
Description: Sent after a window has been moved.
ms.assetid: 552ddc26-fe63-449b-8c82-bb927a2c1c41
title: WM_MOVE message
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WM\_MOVE message

Sent after a window has been moved.

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/en-us/library/ms633573(v=VS.85).aspx) function.


```C++
#define WM_MOVE                         0x0003
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

The x and y coordinates of the upper-left corner of the client area of the window. The low-order word contains the x-coordinate while the high-order word contains the y coordinate.

</dd> </dl>

## Return value

Type: **LRESULT**

If an application processes this message, it should return zero.

## Remarks

The parameters are given in screen coordinates for overlapped and pop-up windows and in parent-client coordinates for child windows.

The following example demonstrates how to obtain the position from the *lParam* parameter.


```
xPos = (int)(short) LOWORD(lParam);   // horizontal position 
yPos = (int)(short) HIWORD(lParam);   // vertical position 
```



You can also use the [**MAKEPOINTS**](https://msdn.microsoft.com/en-us/library/Dd145043(v=VS.85).aspx) macro to convert the *lParam* parameter to a [**POINTS**](https://msdn.microsoft.com/en-us/library/Dd162808(v=VS.85).aspx) structure.

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

[**HIWORD**](https://msdn.microsoft.com/en-us/library/ms632657(v=VS.85).aspx)
</dt> <dt>

[**LOWORD**](https://msdn.microsoft.com/en-us/library/ms632659(v=VS.85).aspx)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**MAKEPOINTS**](https://msdn.microsoft.com/en-us/library/Dd145043(v=VS.85).aspx)
</dt> <dt>

[**POINTS**](https://msdn.microsoft.com/en-us/library/Dd162808(v=VS.85).aspx)
</dt> </dl>

 

 




