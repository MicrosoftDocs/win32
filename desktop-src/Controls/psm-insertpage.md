---
title: PSM_INSERTPAGE message (Prsht.h)
description: Inserts a new page into an existing property sheet. The page can be inserted either at a specified index or after a specified page. You can send this message explicitly or by using the PropSheet\_InsertPage macro.
ms.assetid: 69d55e68-510d-45f1-93d6-ce2bf5dfdb6d
keywords:
- PSM_INSERTPAGE message Windows Controls
topic_type:
- apiref
api_name:
- PSM_INSERTPAGE
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PSM\_INSERTPAGE message

Inserts a new page into an existing property sheet. The page can be inserted either at a specified index or after a specified page. You can send this message explicitly or by using the [**PropSheet\_InsertPage**](/windows/desktop/api/Prsht/nf-prsht-propsheet_insertpage) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Where the page is to be inserted. Set this parameter to **NULL** to make the new page the first page. To specify where the new page is to be inserted, you can either pass an index or an existing page's HPROPSHEETPAGE handle.



| Value                                                                                                                                             | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt></dt> <dt>index</dt> </dl>            | If the *wParam* parameter is less than MAXUSHORT (the largest unsigned short integer), the *wParam* specifies the zero-based index for the new page. For example, to make the inserted page the third page on the property sheet, set *wParam* to 2. To make it the first page, set *wParam* to 0. If *wParam* has a value greater than the number of pages and less than MAXUSHORT, the page will be appended.<br/> |
| <dl> <dt></dt> <dt>hpageInsertAfter</dt> </dl> | If you set the *wParam* parameter to an existing page's HPROPSHEETPAGE handle, the new page will be inserted after it.<br/>                                                                                                                                                                                                                                                                                          |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Handle to the page to be inserted. The page must first be created by a call to the [**CreatePropertySheetPage**](/windows/desktop/api/Prsht/nf-prsht-createpropertysheetpagea) function.

</dd> </dl>

## Return value

Returns a nonzero value if the page was successfully inserted, or zero otherwise.

## Remarks

The pages after the insertion point are shifted to the right to accommodate the new page.

The property sheet is not resized to fit the new page. Do not make the new page larger than the property sheet's largest page.

A number of messages and one function call occur while the property sheet is manipulating the list of pages. While this action is taking place, attempting to modify the list of pages will have unpredictable results. Accordingly, you should not use the PSM\_INSERTPAGE message in your implementation of [*PropSheetPageProc*](/windows/win32/api/prsht/nc-prsht-lpfnpspcallbacka) or while handling the following notifications and Windows messages.

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

You can add or remove pages in response to these notifications, provided that you return (via DWL\_MSGRESULT) a nonzero value to specify the desired new page. Note, however, that if you insert a page that is located before the current page (that has a smaller index than the current page), [PSN\_KILLACTIVE](psn-killactive.md) might be sent to the wrong page.

> [!Note]  
> This message is not supported when using the Aero wizard style ([**PSH\_AEROWIZARD**](/windows/desktop/api/Prsht/ns-prsht-propsheetheadera_v2)).

 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



 

