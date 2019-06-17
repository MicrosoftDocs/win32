---
title: WM_NCMOUSEHOVER message
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
ms.topic: article
ms.date: 05/31/2018
---

# WM\_NCMOUSEHOVER message

Posted to a window when the cursor hovers over the nonclient area of the window for the period of time specified in a prior call to [**TrackMouseEvent**](https://msdn.microsoft.com/en-us/library/ms646265(v=VS.85).aspx).

A window receives this message through its [**WindowProc**](https://docs.microsoft.com/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.


```C++
#define WM_NCMOUSEHOVER                 0x02A0
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The hit-test value returned by the [**DefWindowProc**](https://docs.microsoft.com/windows/desktop/api/winuser/nf-winuser-defwindowproca) function as a result of processing the [**WM\_NCHITTEST**](wm-nchittest.md) message. For a list of hit-test values, see **WM\_NCHITTEST**.

</dd> <dt>

*lParam* 
</dt> <dd>

A [**POINTS**](https://docs.microsoft.com/previous-versions//dd162808(v=vs.85)) structure that contains the x- and y-coordinates of the cursor. The coordinates are relative to the upper-left corner of the screen.

</dd> </dl>

## Return value

If an application processes this message, it should return zero.

## Remarks

Hover tracking stops when this message is generated. The application must call [**TrackMouseEvent**](https://msdn.microsoft.com/en-us/library/ms646265(v=VS.85).aspx) again if it requires further tracking of mouse hover behavior.

You can also use the [**GET\_X\_LPARAM**](https://docs.microsoft.com/windows/desktop/api/windowsx/nf-windowsx-get_x_lparam) and [**GET\_Y\_LPARAM**](https://docs.microsoft.com/windows/desktop/api/windowsx/nf-windowsx-get_y_lparam) macros to extract the values of the x- and y- coordinates from *lParam*.


```
xPos = GET_X_LPARAM(lParam); 
yPos = GET_Y_LPARAM(lParam); 
```



> [!IMPORTANT]
> Do not use the [**LOWORD**](https://docs.microsoft.com/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) or [**HIWORD**](https://docs.microsoft.com/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) macros to extract the x- and y- coordinates of the cursor position because these macros return incorrect results on systems with multiple monitors. Systems with multiple monitors can have negative x- and y- coordinates, and **LOWORD** and **HIWORD** treat the coordinates as unsigned quantities.

 

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

[**DefWindowProc**](https://docs.microsoft.com/windows/desktop/api/winuser/nf-winuser-defwindowproca)
</dt> <dt>

[**GET\_X\_LPARAM**](https://docs.microsoft.com/windows/desktop/api/windowsx/nf-windowsx-get_x_lparam)
</dt> <dt>

[**GET\_Y\_LPARAM**](https://docs.microsoft.com/windows/desktop/api/windowsx/nf-windowsx-get_y_lparam)
</dt> <dt>

[**TrackMouseEvent**](https://msdn.microsoft.com/en-us/library/ms646265(v=VS.85).aspx)
</dt> <dt>

[**TRACKMOUSEEVENT**](https://msdn.microsoft.com/en-us/library/ms645604(v=VS.85).aspx)
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

[**MAKEPOINTS**](https://docs.microsoft.com/windows/desktop/api/wingdi/nf-wingdi-makepoints)
</dt> <dt>

[**POINTS**](https://docs.microsoft.com/previous-versions//dd162808(v=vs.85))
</dt> </dl>

 

 





