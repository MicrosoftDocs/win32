---
title: BCN_DROPDOWN notification code (Winuser.h)
description: Sent when the user clicks a drop down arrow on a button. The parent window of the control receives this notification code in the form of a WM\_NOTIFY message.
ms.assetid: 61503b8d-193e-4855-b9eb-35c0dc636c02
keywords:
- BCN_DROPDOWN notification code Windows Controls
topic_type:
- apiref
api_name:
- BCN_DROPDOWN
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# BCN\_DROPDOWN notification code

Sent when the user clicks a drop down arrow on a button. The parent window of the control receives this notification code in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
BCN_DROPDOWN
        
    pnmdropdown = (NMBCDROPDOWN*) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**NMBCDROPDOWN**](/windows/win32/api/commctrl/ns-commctrl-nmbcdropdown) structure. The **rcButton** member is set to describe the drop-down area.

</dd> </dl>

## Return value

No return value.

## Remarks

The notification receiver casts **LPARAM** to retrieve the [**NMBCDROPDOWN**](/windows/win32/api/commctrl/ns-commctrl-nmbcdropdown) structure. **WPARAM** contains the ID of the control that sends this message. The button control must have a drop-down button style.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



 

 





