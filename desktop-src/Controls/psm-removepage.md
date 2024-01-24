---
title: PSM_REMOVEPAGE message (Prsht.h)
description: Removes a page from a property sheet. You can send this message explicitly or by using the PropSheet\_RemovePage macro.
ms.assetid: 2f387e97-4db4-4ad5-8600-7325da674e33
keywords:
- PSM_REMOVEPAGE message Windows Controls
topic_type:
- apiref
api_name:
- PSM_REMOVEPAGE
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PSM\_REMOVEPAGE message

Removes a page from a property sheet. You can send this message explicitly or by using the [**PropSheet\_RemovePage**](/windows/desktop/api/Prsht/nf-prsht-propsheet_removepage) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Zero-based index of the page to be removed.

</dd> <dt>

*lParam* 
</dt> <dd>

The HPROPSHEETPAGE handle of the page to be removed.

</dd> </dl>

## Return value

No return value.

## Remarks

An application can specify the index or the handle, or both. If both are specified, *lParam* takes precedence.

Sending **PSM\_REMOVEPAGE** destroys the property sheet page that is being removed.

A number of messages and one function call occur while the property sheet is manipulating the list of pages. While this action is taking place, attempting to modify the list of pages will have unpredictable results. Accordingly, you should not use the **PSM\_REMOVEPAGE** message in your implementation of [*PropSheetPageProc*](/windows/win32/api/prsht/nc-prsht-lpfnpspcallbacka) or while handling the following notifications and Windows messages.

-   [PSN\_APPLY](psn-apply.md)
-   [PSN\_KILLACTIVE](psn-killactive.md)
-   [PSN\_RESET](psn-reset.md)
-   [PSN\_SETACTIVE](psn-setactive.md)
-   [**WM\_DESTROY**](/windows/desktop/winmsg/wm-destroy)
-   [**WM\_INITDIALOG**](/windows/desktop/dlgbox/wm-initdialog)

If you need to modify a property sheet page while you are handling one of these messages or while [*PropSheetPageProc*](/windows/win32/api/prsht/nc-prsht-lpfnpspcallbacka) is in operation, post yourself a private Windows message. Your application will not receive that message until after the property sheet manager has finished its tasks. Then you can modify the list of pages.

The following notifications are also affected by property sheet modification.

-   [PSN\_WIZBACK](psn-wizback.md)
-   [PSN\_WIZNEXT](psn-wiznext.md)

You can add or remove pages in response to these notifications, provided that you return (via DWL\_MSGRESULT) a nonzero value to specify the desired new page. Note, however, that if you remove a page that is located before the current page (that has a smaller index than the current page), [PSN\_KILLACTIVE](psn-killactive.md) might be sent to the wrong page.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



 

