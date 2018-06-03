---
title: WM\_MOUSELEAVE message
description: Posted to a window when the cursor leaves the client area of the window specified in a prior call to TrackMouseEvent.
ms.assetid: b23d24ff-531a-4b6d-8848-f82ac5568995
keywords:
- WM_MOUSELEAVE message Keyboard and Mouse Input
topic_type:
- apiref
api_name:
- WM_MOUSELEAVE
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

# WM\_MOUSELEAVE message

Posted to a window when the cursor leaves the client area of the window specified in a prior call to [**TrackMouseEvent**](/windows/desktop/api/Winuser/nf-winuser-trackmouseevent).

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633573) function.


```C++
#define WM_MOUSELEAVE                   0x02A3
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used and must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used and must be zero.

</dd> </dl>

## Return value

If an application processes this message, it should return zero.

## Remarks

All tracking requested by [**TrackMouseEvent**](/windows/desktop/api/Winuser/nf-winuser-trackmouseevent) is canceled when this message is generated. The application must call **TrackMouseEvent** when the mouse reenters its window if it requires further tracking of mouse hover behavior.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**GetCapture**](/windows/desktop/api/Winuser/nf-winuser-getcapture)
</dt> <dt>

[**SetCapture**](/windows/desktop/api/Winuser/nf-winuser-setcapture)
</dt> <dt>

[**TrackMouseEvent**](/windows/desktop/api/Winuser/nf-winuser-trackmouseevent)
</dt> <dt>

[**TRACKMOUSEEVENT**](/windows/desktop/api/Winuser/nf-winuser-trackmouseevent)
</dt> <dt>

[**WM\_NCMOUSELEAVE**](wm-ncmouseleave.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Mouse Input](mouse-input.md)
</dt> </dl>

 

 





