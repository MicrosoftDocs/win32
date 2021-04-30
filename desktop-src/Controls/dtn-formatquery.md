---
title: DTN_FORMATQUERY notification code (Commctrl.h)
description: Sent by a date and time picker (DTP) control to retrieve the maximum allowable size of the string that will be displayed in a callback field. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 0f00086a-0ab8-4f6f-9c3e-6e77008aa088
keywords:
- DTN_FORMATQUERY notification code Windows Controls
topic_type:
- apiref
api_name:
- DTN_FORMATQUERY
- DTN_FORMATQUERYA
- DTN_FORMATQUERYW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DTN\_FORMATQUERY notification code

Sent by a date and time picker (DTP) control to retrieve the maximum allowable size of the string that will be displayed in a callback field. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
DTN_FORMATQUERY

    lpDTFormatQuery = (LPNMDATETIMEFORMATQUERY) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMDATETIMEFORMATQUERY**](/windows/win32/api/commctrl/ns-commctrl-nmdatetimeformatquerya) structure containing information about the callback field. The structure contains a substring that defines a callback field and receives the maximum allowable size of the string that will be displayed in the callback field.

</dd> </dl>

## Return value

The owner of the control must calculate the maximum possible width of the text that will be displayed in the callback field, set the **szMax** member of the [**NMDATETIMEFORMATQUERY**](/windows/win32/api/commctrl/ns-commctrl-nmdatetimeformatquerya) structure, and return zero.

## Remarks

Handling this notification code prepares the control to adjust for the maximum size of the string that will be displayed in a particular callback field. This enables the control to properly display output at all times, reducing flicker within the control's display. (For additional information about callback fields, see [Callback fields](date-and-time-picker-controls.md).)

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **DTN\_FORMATQUERYW** (Unicode) and **DTN\_FORMATQUERYA** (ANSI)<br/>           |



 

 





