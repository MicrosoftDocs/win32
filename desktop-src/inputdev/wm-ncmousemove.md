---
title: WM_NCMOUSEMOVE message
description: Posted to a window when the cursor is moved within the nonclient area of the window. This message is posted to the window that contains the cursor. If a window has captured the mouse, this message is not posted.
ms.assetid: 49c7cde9-701c-4821-8d16-31ca3c016ed4
keywords:
- WM_NCMOUSEMOVE message Keyboard and Mouse Input
topic_type:
- apiref
api_name:
- WM_NCMOUSEMOVE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WM\_NCMOUSEMOVE message

Posted to a window when the cursor is moved within the nonclient area of the window. This message is posted to the window that contains the cursor. If a window has captured the mouse, this message is not posted.

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633573) function.


```C++
#define WM_NCMOUSEMOVE                  0x00A0
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The hit-test value returned by the [**DefWindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633572) function as a result of processing the [**WM\_NCHITTEST**](wm-nchittest.md) message. For a list of hit-test values, see **WM\_NCHITTEST**.

</dd> <dt>

*lParam* 
</dt> <dd>

A [**POINTS**](https://msdn.microsoft.com/library/windows/desktop/dd162808) structure that contains the x- and y-coordinates of the cursor. The coordinates are relative to the upper-left corner of the screen.

</dd> </dl>

## Return value

If an application processes this message, it should return zero.

## Remarks

If it is appropriate to do so, the system sends the [**WM\_SYSCOMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms646360) message to the window.

You can also use the [**GET\_X\_LPARAM**](https://msdn.microsoft.com/library/windows/desktop/ms632654) and [**GET\_Y\_LPARAM**](https://msdn.microsoft.com/library/windows/desktop/ms632655) macros to extract the values of the x- and y- coordinates from *lParam*.


```
xPos = GET_X_LPARAM(lParam); 
yPos = GET_Y_LPARAM(lParam); 
```



> \[!Important\]  
> Do not use the [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) or [**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657) macros to extract the x- and y- coordinates of the cursor position because these macros return incorrect results on systems with multiple monitors. Systems with multiple monitors can have negative x- and y- coordinates, and **LOWORD** and **HIWORD** treat the coordinates as unsigned quantities.

 

## Requirements



|                                     |                                                                                                           |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windowsx.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**DefWindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633572)
</dt> <dt>

[**GET\_X\_LPARAM**](https://msdn.microsoft.com/library/windows/desktop/ms632654)
</dt> <dt>

[**GET\_Y\_LPARAM**](https://msdn.microsoft.com/library/windows/desktop/ms632655)
</dt> <dt>

[**WM\_NCHITTEST**](wm-nchittest.md)
</dt> <dt>

[**WM\_SYSCOMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms646360)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Mouse Input](mouse-input.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**MAKEPOINTS**](https://msdn.microsoft.com/library/windows/desktop/dd145043)
</dt> <dt>

[**POINTS**](https://msdn.microsoft.com/library/windows/desktop/dd162808)
</dt> </dl>

 

 





