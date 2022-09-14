---
title: TTN_SHOW notification code (Commctrl.h)
description: Notifies the owner window that a tooltip control is about to be displayed. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: ddfd18cd-0681-4e4a-b258-873f98da7479
keywords:
- TTN_SHOW notification code Windows Controls
topic_type:
- apiref
api_name:
- TTN_SHOW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TTN\_SHOW notification code

Notifies the owner window that a tooltip control is about to be displayed. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TTN_SHOW

    pnmh = (LPNMHDR) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-nmhdr) structure.

</dd> </dl>

## Return value

[Version 4.70](common-control-versions.md). To display the tooltip in its default location, return zero. To customize the tooltip position, reposition the tooltip window with the [**SetWindowPos**](/windows/desktop/api/winuser/nf-winuser-setwindowpos) function and return **TRUE**.

> [!Note]  
> For versions earlier than 4.70, there is no return value.

 

## Remarks

A tooltip window rectangle is somewhat larger than its text display rectangle, and its origin is offset up and to the left. If you need to accurately position the text display rectangle of a tooltip, the [**TTM\_ADJUSTRECT**](ttm-adjustrect.md) message converts a text display rectangle into the corresponding tooltip window rectangle and vice versa.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

