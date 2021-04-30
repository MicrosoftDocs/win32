---
title: DTN_USERSTRING notification code (Commctrl.h)
description: Sent by a date and time picker (DTP) control when a user finishes editing a string in the control.
ms.assetid: a5b13582-323b-4804-912c-a988d902547d
keywords:
- DTN_USERSTRING notification code Windows Controls
topic_type:
- apiref
api_name:
- DTN_USERSTRING
- DTN_USERSTRINGA
- DTN_USERSTRINGW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DTN\_USERSTRING notification code

Sent by a date and time picker (DTP) control when a user finishes editing a string in the control. This notification code is only sent by DTP controls that are set to the [**DTS\_APPCANPARSE**](date-and-time-picker-control-styles.md) style. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
DTN_USERSTRING

    lpDTstring = (LPNMDATETIMESTRING) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMDATETIMESTRING**](/windows/win32/api/commctrl/ns-commctrl-nmdatetimestringa) structure that contains information about the instance of the notification code.

</dd> </dl>

## Return value

The owner of the control must return zero.

## Remarks

Handling this notification code allows the owner to provide custom responses to strings entered into the control by the user. The owner must be prepared to parse the input string and take action if necessary.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **DTN\_USERSTRINGW** (Unicode) and **DTN\_USERSTRINGA** (ANSI)<br/>             |



 

 





