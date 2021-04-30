---
title: IPN_FIELDCHANGED notification code (Commctrl.h)
description: Sent when the user changes a field in the control or moves from one field to another. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: f9ca6435-1715-458e-8d0e-475920ed75bd
keywords:
- IPN_FIELDCHANGED notification code Windows Controls
topic_type:
- apiref
api_name:
- IPN_FIELDCHANGED
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# IPN\_FIELDCHANGED notification code

Sent when the user changes a field in the control or moves from one field to another. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
IPN_FIELDCHANGED

    lpnmipa = (LPNMIPADDRESS) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMIPADDRESS**](/windows/win32/api/commctrl/ns-commctrl-nmipaddress) structure that contains information about the changed address. The **iValue** member of this structure will contain the entered value, even if it is out of the range of the field. You can modify this member to any value that is within the range for the field in response to this notification code.

</dd> </dl>

## Return value

The return value is ignored.

## Remarks

This notification code is not sent in response to a [**IPM\_SETADDRESS**](ipm-setaddress.md) message.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





