---
title: PSM_SETCURSEL message (Prsht.h)
description: Activates the specified page in a property sheet. You can send this message explicitly or by using the PropSheet\_SetCurSel macro.
ms.assetid: 800aadde-cabc-424e-8e63-60fc7ce952d7
keywords:
- PSM_SETCURSEL message Windows Controls
topic_type:
- apiref
api_name:
- PSM_SETCURSEL
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PSM\_SETCURSEL message

Activates the specified page in a property sheet. You can send this message explicitly or by using the [**PropSheet\_SetCurSel**](/windows/desktop/api/Prsht/nf-prsht-propsheet_setcursel) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The zero-based index of the page. An application can specify the index or the handle or both. If both are specified, *lParam* takes precedence.

</dd> <dt>

*lParam* 
</dt> <dd>

The handle to the page to activate. An application can specify the index or the handle or both. If both are specified, *lParam* takes precedence.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

The window that is losing the activation receives the [PSN\_KILLACTIVE](psn-killactive.md) notification code, and the window that is gaining the activation receives the [PSN\_SETACTIVE](psn-setactive.md) notification code.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



 

 





