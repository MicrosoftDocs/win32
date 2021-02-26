---
title: WM_DPICHANGED_AFTERPARENT message (Winuser.h)
description: For Per Monitor v2 top-level windows, this message is sent to all HWNDs in the child HWDN tree of the window that is undergoing a DPI change. | WM_DPICHANGED_AFTERPARENT message (Winuser.h)
ms.assetid: FEA1BF07-55B6-4584-ABD3-340515831E0A
keywords:
- WM_DPICHANGED_AFTERPARENT message High DPI
topic_type:
- apiref
api_name:
- WM_DPICHANGED_AFTERPARENT
api_location:
- winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_DPICHANGED\_AFTERPARENT message

For [Per Monitor v2](dpi-awareness-context.md) top-level windows, this message is sent to all HWNDs in the child HWDN tree of the window that is undergoing a DPI change. This message occurs after the top-level window receives [**WM\_DPICHANGED**](wm-dpichanged.md), and traverses the child tree from the top down.


```C++
#define WM_DPICHANGED_AFTERPARENT       0x02E3
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This value is unused and will be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

This value is unused and will be zero.

</dd> </dl>

## Return value

This value is unused and ignored by the system.

## Remarks

There is no default handling of this message in [DefWindowProc](/windows/win32/api/winuser/nf-winuser-defwindowproca).

This message is only sent when the top-level window has a DPI awareness context of PMv2.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703 \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Winuser.h</dt> </dl> |



## See also

<dl> <dt>

[**WM\_DPICHANGED**](wm-dpichanged.md)
</dt> <dt>

[**WM\_DPICHANGED\_BEFOREPARENT**](wm-dpichanged-beforeparent.md)
</dt> </dl>

 

