---
title: PSN_WIZFINISH notification code (Prsht.h)
description: Notifies a page that the user has clicked the Finish button in a wizard. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 8ef0a8a7-2d25-4969-9b8f-e42dcc1c8fb5
keywords:
- PSN_WIZFINISH notification code Windows Controls
topic_type:
- apiref
api_name:
- PSN_WIZFINISH
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PSN\_WIZFINISH notification code

Notifies a page that the user has clicked the **Finish** button in a wizard. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
PSN_WIZFINISH 

    lppsn = (LPPSHNOTIFY) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**PSHNOTIFY**](/windows/desktop/api/Prsht/ns-prsht-pshnotify) structure that contains information about the notification code. This structure contains an [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-nmhdr) structure as its first member, **hdr**. The **hwndFrom** member of this **NMHDR** structure contains the handle to the property sheet. The **lParam** member of the **PSHNOTIFY** structure does not contain any information.

</dd> </dl>

## Return value

-   Returns **TRUE** to prevent the wizard from finishing.
-   [Version 5.80.](common-control-versions.md) and later. Returns a window handle to prevent the wizard from finishing. The wizard will set the focus to that window. The window must be owned by the wizard page.
-   Returns **FALSE** to allow the wizard to finish.

## Remarks

To set the return value, the dialog box procedure for the page must use the [**SetWindowLong**](/windows/desktop/api/winuser/nf-winuser-setwindowlonga) function with the DWL\_MSGRESULT value, and the dialog box procedure must return **TRUE**.

[Version 5.80.](common-control-versions.md) If your application returns **TRUE** to prevent a wizard from finishing, it has no control over which window on the page receives focus. Applications that need to stop a wizard from finishing should normally do so by returning the handle of the window on the wizard page that is to receive focus.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



 

