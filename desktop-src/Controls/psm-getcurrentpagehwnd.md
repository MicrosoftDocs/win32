---
title: PSM_GETCURRENTPAGEHWND message
description: Retrieves a handle to the window of the current page of a property sheet. You can send this message explicitly or by using the PropSheet\_GetCurrentPageHwnd macro.
ms.assetid: 1f2d0af9-5853-48e7-b827-483be032b6ca
keywords:
- PSM_GETCURRENTPAGEHWND message Windows Controls
topic_type:
- apiref
api_name:
- PSM_GETCURRENTPAGEHWND
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PSM\_GETCURRENTPAGEHWND message

Retrieves a handle to the window of the current page of a property sheet. You can send this message explicitly or by using the [**PropSheet\_GetCurrentPageHwnd**](/windows/desktop/api/Prsht/nf-prsht-propsheet_getcurrentpagehwnd) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Must be zero.

</dd> </dl>

## Return value

Returns a handle to the window of the current property sheet page.

## Remarks

Use the **PSM\_GETCURRENTPAGEHWND** message with modeless property sheets to determine when to destroy the dialog box. When the user clicks the **OK** or **Cancel** button, **PSM\_GETCURRENTPAGEHWND** returns **NULL**, and you can then use the [**DestroyWindow**](https://msdn.microsoft.com/library/windows/desktop/ms632682) function to destroy the dialog box.

> [!Note]  
> This message is not supported when using the Aero wizard style ([**PSH\_AEROWIZARD**](/windows/desktop/api/Prsht/ns-prsht-_propsheetheadera_v2)).

 

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



## See also

<dl> <dt>

[**PropertySheet**](/windows/desktop/api/Prsht/nf-prsht-propertysheeta)
</dt> </dl>

 

 





