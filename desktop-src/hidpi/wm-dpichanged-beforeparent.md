---
title: WM_DPICHANGED_BEFOREPARENT message (Winuser.h)
description: For Per Monitor v2 top-level windows, this message is sent to all HWNDs in the child HWDN tree of the window that is undergoing a DPI change. | WM_DPICHANGED_BEFOREPARENT message (Winuser.h)
ms.assetid: EC8CC313-565F-451F-AE18-66F3B63303CE
keywords:
- WM_DPICHANGED_BEFOREPARENT message High DPI
topic_type:
- apiref
api_name:
- WM_DPICHANGED_BEFOREPARENT
api_location:
- winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_DPICHANGED\_BEFOREPARENT message

For [Per Monitor v2](dpi-awareness-context.md) top-level windows, this message is sent to all HWNDs in the child HWDN tree of the window that is undergoing a DPI change. This message occurs before the top-level window receives [**WM\_DPICHANGED**](wm-dpichanged.md), and traverses the child tree from the bottom up.


```C++
#define WM_DPICHANGED_BEFOREPARENT       0x02E2
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

[**WM\_DPICHANGED\_AFTERPARENT**](wm-dpichanged-afterparent.md)
</dt> </dl>

 

