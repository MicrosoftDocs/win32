---
title: PSN_TRANSLATEACCELERATOR notification code (Prsht.h)
description: Notifies a property sheet that a keyboard message has been received. It provides the page an opportunity to do private keyboard accelerator translation. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 04d67326-92f9-4b92-a27e-354815f3c1a8
keywords:
- PSN_TRANSLATEACCELERATOR notification code Windows Controls
topic_type:
- apiref
api_name:
- PSN_TRANSLATEACCELERATOR
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PSN\_TRANSLATEACCELERATOR notification code

Notifies a property sheet that a keyboard message has been received. It provides the page an opportunity to do private keyboard accelerator translation. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
PSN_TRANSLATEACCELERATOR 

    lppsn = (LPPSHNOTIFY) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**PSHNOTIFY**](/windows/desktop/api/Prsht/ns-prsht-pshnotify) structure that contains information about the notification code. This structure contains an [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-nmhdr) structure as its first member, **hdr**. The **hwndFrom** member of the **NMHDR** structure contains the handle to the property sheet. The **lParam** member of the **PSHNOTIFY** structure is a pointer to the message's [**MSG**](/windows/win32/api/winuser/ns-winuser-msg). It can be cast to an **LPMSG** type, to get access to the parameters of the message to be translated.

</dd> </dl>

## Return value

Returns PSNRET\_MESSAGEHANDLED to indicate that no further processing is necessary. Returns PSNRET\_NOERROR to request normal processing.

## Remarks

To set the return value, the dialog box procedure for the page must use the [**SetWindowLong**](/windows/desktop/api/winuser/nf-winuser-setwindowlonga) function with the DWL\_MSGRESULT value. The dialog box procedure must return **TRUE**.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



 

