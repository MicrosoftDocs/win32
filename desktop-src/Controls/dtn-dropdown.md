---
title: DTN_DROPDOWN notification code (Commctrl.h)
description: Sent by a date and time picker (DTP) control when the user activates the drop-down month calendar. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 6f20fa87-2223-4876-b77d-2c684685bf10
keywords:
- DTN_DROPDOWN notification code Windows Controls
topic_type:
- apiref
api_name:
- DTN_DROPDOWN
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DTN\_DROPDOWN notification code

Sent by a date and time picker (DTP) control when the user activates the drop-down month calendar. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
DTN_DROPDOWN

    lpNmhdr = (LPNMHDR)lParam;
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

One task that your notification handler may need to perform is to customize the dropdown month-calendar control. For instance, if you do not want "Go To Today," you need to set the control's [**MCS\_NOTODAY**](month-calendar-control-styles.md)  style. To retrieve a handle to the month-calendar control, send the DTP control a [**DTM\_GETMONTHCAL**](dtm-getmonthcal.md) message. You can then use this handle and [**SetWindowLong**](/windows/desktop/api/winuser/nf-winuser-setwindowlonga) to set the desired month-calendar style.

DTP controls do not maintain a static child month calendar control. The DTP control creates a new month calendar control before sending this notification code. Additionally, the DTP control destroys the child control when it is not active (visible). So your application must not rely on a static window handle to the control's child month calendar.

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

[DTN\_CLOSEUP](dtn-closeup.md)
</dt> <dt>

[**DTM\_GETMONTHCAL**](dtm-getmonthcal.md)
</dt> </dl>

 

