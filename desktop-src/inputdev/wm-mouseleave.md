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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WM\_MOUSELEAVE message

Posted to a window when the cursor leaves the client area of the window specified in a prior call to [**TrackMouseEvent**](/windows/win32/Winuser/nf-winuser-trackmouseevent?branch=master).

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

All tracking requested by [**TrackMouseEvent**](/windows/win32/Winuser/nf-winuser-trackmouseevent?branch=master) is canceled when this message is generated. The application must call **TrackMouseEvent** when the mouse reenters its window if it requires further tracking of mouse hover behavior.

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

[**GetCapture**](/windows/win32/Winuser/nf-winuser-getcapture?branch=master)
</dt> <dt>

[**SetCapture**](/windows/win32/Winuser/nf-winuser-setcapture?branch=master)
</dt> <dt>

[**TrackMouseEvent**](/windows/win32/Winuser/nf-winuser-trackmouseevent?branch=master)
</dt> <dt>

[**TRACKMOUSEEVENT**](/windows/win32/Winuser/nf-winuser-trackmouseevent?branch=master)
</dt> <dt>

[**WM\_NCMOUSELEAVE**](wm-ncmouseleave.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Mouse Input](mouse-input.md)
</dt> </dl>

 

 





