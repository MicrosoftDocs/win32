---
title: PSN_WIZNEXT notification code (Prsht.h)
description: Notifies a page that the user has clicked the Next button in a wizard. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: ff5be154-f2d1-403d-8f22-8f6cacfb66b1
keywords:
- PSN_WIZNEXT notification code Windows Controls
topic_type:
- apiref
api_name:
- PSN_WIZNEXT
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PSN\_WIZNEXT notification code

Notifies a page that the user has clicked the **Next** button in a wizard. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
PSN_WIZNEXT 

    lppsn = (LPPSHNOTIFY) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**PSHNOTIFY**](/windows/desktop/api/Prsht/ns-prsht-pshnotify) structure that contains information about the notification code. This structure contains an [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-nmhdr) structure as its first member, **hdr**. The **hwndFrom** member of this **NMHDR** structure contains the handle to the property sheet. The **lParam** member of the **PSHNOTIFY** structure does not contain any information.

</dd> </dl>

## Return value

Return 0 to allow the wizard to go to the next page. Return -1 to prevent the wizard from changing pages. To display a particular page, return its dialog resource identifier. If the dialog was specified with the [**PSP\_DLGINDIRECT**](/windows/desktop/api/Prsht/ns-prsht-propsheetpagea_v2) flag, this notification returns the pointer to the dialog template.

## Remarks

To set the return value, the dialog box procedure for the page must call the [**SetWindowLong**](/windows/desktop/api/winuser/nf-winuser-setwindowlonga) function with the **DWL\_MSGRESULT** value and return **TRUE**. For example:

``` syntax
case PSN_WIZNEXT :
    SetWindowLong(hDlg, DWL_MSGRESULT, 0);
    break;

case PSN_WIZBACK :
    ...
```

> [!Note]  
> The property sheet is in the process of manipulating the list of pages when the PSN\_WIZNEXT notification code is sent. You can add, insert, or remove pages in response to these notification codes, but special care must be taken if you insert or remove pages before the current page.

 

If you insert or remove pages before the current page, you must return (through **DWL\_MSGRESULT**) a nonzero value to specify the desired new page. Note, however, that if you insert or remove a page that is located before the current page (that has a smaller index than the current page), [PSN\_KILLACTIVE](psn-killactive.md) might be sent to the wrong page.

For this reason, it is recommended that wizards that add and remove pages dynamically in response to PSN\_WIZNEXT and [PSN\_WIZBACK](psn-wizback.md) do so only to pages at the end of the list. If you want your wizard to remove pages accurately, keep the dynamic pages at the end of the list and jump back to permanent pages before deleting them.

For example, suppose a wizard consists of an introductory page, a series of dynamic pages, and a completion page, and you want to delete the dynamic pages when the user reaches the completion page.

1.  The wizard would begin with two pages, "Introduction" and "Completion." The user begins on the "Introduction" page.
    1.  Introduction (User is here)
    2.  Completion
2.  When the user navigates away from "Introduction," the wizard adds the dynamic pages and places the user at the first dynamic page by returning (through **DWL\_MSGRESULT**) the dialog identifier of the page "Dynamic 1." In this example, there are three dynamic pages.
    1.  Introduction
    2.  Completion
    3.  Dynamic 1 (User is here)
    4.  Dynamic 2
    5.  Dynamic 3
3.  After the user navigates through the dynamic pages to "Dynamic 3" and then navigates to the next page, the application should place the user at the page "Completion." Again, this is done by returning (through **DWL\_MSGRESULT**) the dialog identifier of the page "Completion."
    1.  Introduction
    2.  Completion (User is here)
    3.  Dynamic 1
    4.  Dynamic 2
    5.  Dynamic 3
4.  The application can then remove the three dynamic pages (numbered three through five) safely.
    1.  Introduction
    2.  Completion (User is here)

Note that this technique is necessary only if your wizard removes pages dynamically. If your wizard only adds pages dynamically, this process is not necessary.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



 

