---
title: DTN_FORMAT notification code (Commctrl.h)
description: Sent by a date and time picker (DTP) control to request text to be displayed in a callback field. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: ce0ee230-638e-425f-9f34-c379342cea93
keywords:
- DTN_FORMAT notification code Windows Controls
topic_type:
- apiref
api_name:
- DTN_FORMAT
- DTN_FORMATA
- DTN_FORMATW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DTN\_FORMAT notification code

Sent by a date and time picker (DTP) control to request text to be displayed in a callback field. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
DTN_FORMAT

    lpNMFormat = (LPNMDATETIMEFORMAT) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMDATETIMEFORMAT**](/windows/win32/api/commctrl/ns-commctrl-nmdatetimeformata) structure containing information regarding this instance of the notification code. The structure contains the substring that defines the callback field and receives the formatted string that the control will display.

</dd> </dl>

## Return value

The owner of the control must return zero.

## Remarks

Handling this notification code allows the owner of the control to provide a custom string that the control will display. (For additional information about callback fields, see [Callback fields](date-and-time-picker-controls.md).)

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **DTN\_FORMATW** (Unicode) and **DTN\_FORMATA** (ANSI)<br/>                     |



 

 





