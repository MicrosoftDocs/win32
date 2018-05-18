---
Description: 'Sent after a window has been moved.'
ms.assetid: '552ddc26-fe63-449b-8c82-bb927a2c1c41'
title: 'WM\_MOVE message'
---

# WM\_MOVE message

Sent after a window has been moved.

A window receives this message through its [**WindowProc**](windowproc.md) function.


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



You can also use the [**MAKEPOINTS**](gdi.makepoints) macro to convert the *lParam* parameter to a [**POINTS**](gdi.points) structure.

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

[**HIWORD**](hiword.md)
</dt> <dt>

[**LOWORD**](loword.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**MAKEPOINTS**](gdi.makepoints)
</dt> <dt>

[**POINTS**](gdi.points)
</dt> </dl>

 

 




