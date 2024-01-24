---
title: HDN_DROPDOWN notification code (Commctrl.h)
description: Sent by a header control to its parent when the drop-down arrow on the header control is clicked. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: cacf5cb9-0593-42ff-868d-b098481f565f
keywords:
- HDN_DROPDOWN notification code Windows Controls
topic_type:
- apiref
api_name:
- HDN_DROPDOWN
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# HDN\_DROPDOWN notification code

Sent by a header control to its parent when the drop-down arrow on the header control is clicked. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
HDN_DROPDOWN
        
    pNMHeader = (LPNMHEADER) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMHEADER**](/windows/win32/api/commctrl/ns-commctrl-nmheadera) structure that contains information on the header control.

</dd> </dl>

## Return value

No return value.

## Remarks

The example in the Syntax section shows how the notification receiver casts **LPARAM** to retrieve the [**NMHEADER**](/windows/win32/api/commctrl/ns-commctrl-nmheadera) structure. **WPARAM** contains the ID of the control that sends this message.

This message is sent only if style HDF\_SPLITBUTTON is set on the header item.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





