---
title: WM\_NCMOUSEHOVER message
description: Posted to a window when the cursor hovers over the nonclient area of the window for the period of time specified in a prior call to TrackMouseEvent.
ms.assetid: ca1afdc2-7884-445e-b9b7-4d7dd5dcea38
keywords:
- WM_NCMOUSEHOVER message Keyboard and Mouse Input
topic_type:
- apiref
api_name:
- WM_NCMOUSEHOVER
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WM\_NCMOUSEHOVER message

Posted to a window when the cursor hovers over the nonclient area of the window for the period of time specified in a prior call to [**TrackMouseEvent**](/windows/win32/Winuser/nf-winuser-trackmouseevent?branch=master).

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633573) function.


```C++
#define WM_NCMOUSEHOVER                 0x02A0
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

Hover tracking stops when this message is generated. The application must call [**TrackMouseEvent**](/windows/win32/Winuser/nf-winuser-trackmouseevent?branch=master) again if it requires further tracking of mouse hover behavior.

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

[**TrackMouseEvent**](/windows/win32/Winuser/nf-winuser-trackmouseevent?branch=master)
</dt> <dt>

[**TRACKMOUSEEVENT**](/windows/win32/Winuser/nf-winuser-trackmouseevent?branch=master)
</dt> <dt>

[**WM\_NCHITTEST**](wm-nchittest.md)
</dt> <dt>

[**WM\_MOUSEHOVER**](wm-mousehover.md)
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

 

 





