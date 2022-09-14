---
title: DTN_CLOSEUP notification code (Commctrl.h)
description: Sent by a date and time picker (DTP) control when the user closes the drop-down month calendar.
ms.assetid: 94ace714-55cc-4c59-8b87-8d0348b15f34
keywords:
- DTN_CLOSEUP notification code Windows Controls
topic_type:
- apiref
api_name:
- DTN_CLOSEUP
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DTN\_CLOSEUP notification code

Sent by a date and time picker (DTP) control when the user closes the drop-down month calendar. The month calendar is closed when the user chooses a date from the month calendar or clicks the drop-down arrow while the calendar is open. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
DTN_CLOSEUP

    lpNmhdr = (LPMNHDR)lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-nmhdr) structure that contains information about the notification.

</dd> </dl>

## Return value

The return value for this notification is not used.

## Remarks

DTP controls do not maintain a static child month calendar control. The DTP control destroys the child month calendar control prior to sending this notification code. So your application must not rely on a static window handle to the control's child month calendar.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[DTN\_DROPDOWN](dtn-dropdown.md)
</dt> <dt>

[**DTM\_GETMONTHCAL**](dtm-getmonthcal.md)
</dt> </dl>

 

 





