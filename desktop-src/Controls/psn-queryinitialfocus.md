---
title: PSN_QUERYINITIALFOCUS notification code (Prsht.h)
description: Sent by a property sheet to provide a property sheet page an opportunity to specify which dialog box control should receive the initial focus. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 29b5e598-75b2-4b6f-acdb-171b1f7a1850
keywords:
- PSN_QUERYINITIALFOCUS notification code Windows Controls
topic_type:
- apiref
api_name:
- PSN_QUERYINITIALFOCUS
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PSN\_QUERYINITIALFOCUS notification code

Sent by a property sheet to provide a property sheet page an opportunity to specify which dialog box control should receive the initial focus. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
PSN_QUERYINITIALFOCUS

    lppsn = (LPPSHNOTIFY) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**PSHNOTIFY**](/windows/desktop/api/Prsht/ns-prsht-pshnotify) structure. Cast the **lParam** member of this structure to an **HWND** type, to retrieve the handle of the control that will be given focus by default. The structure contains an [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-nmhdr) structure as its first member, **hdr**. The **hwndFrom** member of this **NMHDR** structure contains the handle to the property sheet.

</dd> </dl>

## Return value

To specify which control should receive focus, return the control's handle. Otherwise, return zero and focus will go to the default control. To set the return value, the dialog box procedure must call the [**SetWindowLong**](/windows/desktop/api/winuser/nf-winuser-setwindowlonga) function with a **DWL\_MSGRESULT** value and return **TRUE**.

## Remarks

An application must not call the [**SetFocus**](/windows/desktop/api/winuser/nf-winuser-setfocus) function while handling this notification code. Return the handle of the control that should receive focus, and the property sheet manager will handle the focus change.

The PSN\_QUERYINITIALFOCUS notification code is not sent if the property sheet manager determines that no control on the page should receive focus.

This code fragment implements a simple handler for PSN\_QUERYINITIALFOCUS. It requests that initial focus be given to the Location control (**IDC\_LOCATION**).

``` syntax
case PSN_QUERYINITIALFOCUS :
    SetWindowLong(hDlg,DWL_MSGRESULT, (LPARAM)GetDlgItem(hDlg, IDC_LOCATION));
    return TRUE;
...
```

> [!Note]  
> This notification code is not supported when using the Aero wizard style ([**PSH\_AEROWIZARD**](/windows/desktop/api/Prsht/ns-prsht-propsheetheadera_v2)).

 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



 

