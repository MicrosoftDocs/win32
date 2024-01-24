---
title: HDN_ITEMCLICK notification code (Commctrl.h)
description: Notifies a header control's parent window that the user clicked the control. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 25ed0070-5891-4f36-9ae0-fc04e064401f
keywords:
- HDN_ITEMCLICK notification code Windows Controls
topic_type:
- apiref
api_name:
- HDN_ITEMCLICK
- HDN_ITEMCLICKA
- HDN_ITEMCLICKW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# HDN\_ITEMCLICK notification code

Notifies a header control's parent window that the user clicked the control. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
HDN_ITEMCLICK

    pNMHeader = (LPNMHEADER) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMHEADER**](/windows/win32/api/commctrl/ns-commctrl-nmheadera) structure that identifies the header control and specifies the index of the header item that was clicked and the mouse button used to click the item. The **pItem** member is set to **NULL**.

</dd> </dl>

## Return value

No return value.

## Remarks

A header control sends this notification code after the user releases the left mouse button.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **HDN\_ITEMCLICKW** (Unicode) and **HDN\_ITEMCLICKA** (ANSI)<br/>               |



 

 





