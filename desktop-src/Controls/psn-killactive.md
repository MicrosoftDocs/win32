---
title: PSN_KILLACTIVE notification code (Prsht.h)
description: Notifies a page that it is about to lose activation either because another page is being activated or the user has clicked the OK button. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 470cd6ff-73ad-451a-a861-4d3324a8a8db
keywords:
- PSN_KILLACTIVE notification code Windows Controls
topic_type:
- apiref
api_name:
- PSN_KILLACTIVE
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PSN\_KILLACTIVE notification code

Notifies a page that it is about to lose activation either because another page is being activated or the user has clicked the OK button. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
PSN_KILLACTIVE 

    lppsn = (LPPSHNOTIFY) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**PSHNOTIFY**](/windows/desktop/api/Prsht/ns-prsht-pshnotify) structure that contains information about the notification code. This structure contains an [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-nmhdr) structure as its first member, **hdr**. The **hwndFrom** member of this **NMHDR** structure contains the handle to the property sheet. The **lParam** member of the **PSHNOTIFY** structure does not contain any information.

</dd> </dl>

## Return value

Returns **TRUE** to prevent the page from losing the activation, or **FALSE** to allow it.

## Remarks

An application handles this notification code to validate the information the user has entered.

> [!Note]  
> The property sheet is in the process of manipulating the list of pages when the PSN\_KILLACTIVE notification code is sent. Do not attempt to add, remove, or insert pages while handling this notification code. Doing so will have unpredictable results.

 

To set a return value, the dialog box procedure for the page must call the [**SetWindowLong**](/windows/desktop/api/winuser/nf-winuser-setwindowlonga) function with a DWL\_MSGRESULT value set to the return value. The dialog box procedure must return **TRUE**.

If the dialog box procedure sets DWL\_MSGRESULT to **TRUE**, it should display a message box to explain the problem to the user.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



 

