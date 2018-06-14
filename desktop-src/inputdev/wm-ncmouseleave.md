---
title: WM\_NCMOUSELEAVE message
description: Posted to a window when the cursor leaves the nonclient area of the window specified in a prior call to TrackMouseEvent.
ms.assetid: b3ada6db-93ce-45d7-b408-d08692328aeb
keywords:
- WM_NCMOUSELEAVE message Keyboard and Mouse Input
topic_type:
- apiref
api_name:
- WM_NCMOUSELEAVE
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

# WM\_NCMOUSELEAVE message

Posted to a window when the cursor leaves the nonclient area of the window specified in a prior call to [**TrackMouseEvent**](https://msdn.microsoft.com/en-us/library/ms646265(v=VS.85).aspx).

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633573) function.


```C++
#define WM_NCMOUSELEAVE                 0x02A2
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

All tracking requested by [**TrackMouseEvent**](https://msdn.microsoft.com/en-us/library/ms646265(v=VS.85).aspx) is canceled when this message is generated. The application must call **TrackMouseEvent** when the mouse reenters its window if it requires further tracking of mouse hover behavior.

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

[**TrackMouseEvent**](https://msdn.microsoft.com/en-us/library/ms646265(v=VS.85).aspx)
</dt> <dt>

[**TRACKMOUSEEVENT**](https://msdn.microsoft.com/en-us/library/ms645604(v=VS.85).aspx)
</dt> <dt>

[**WM\_SYSCOMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms646360)
</dt> <dt>

[**WM\_MOUSELEAVE**](wm-mouseleave.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Mouse Input](mouse-input.md)
</dt> </dl>

 

 





