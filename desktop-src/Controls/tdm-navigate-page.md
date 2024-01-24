---
title: TDM_NAVIGATE_PAGE message (Commctrl.h)
description: Recreates a task dialog with new contents, simulating the functionality of a multi-page wizard.
ms.assetid: e0eefd08-e279-47db-97e9-7ca86b41e22f
keywords:
- TDM_NAVIGATE_PAGE message Windows Controls
topic_type:
- apiref
api_name:
- TDM_NAVIGATE_PAGE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TDM\_NAVIGATE\_PAGE message

Recreates a task dialog with new contents, simulating the functionality of a multi-page wizard.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

Not used. Must be zero.

</dd> <dt>

*lParam* \[in\]
</dt> <dd>

A pointer to a [**TASKDIALOGCONFIG**](/windows/desktop/api/Commctrl/ns-commctrl-taskdialogconfig) structure that describes the task dialog to create. The calling application must allocate this structure and set its members. The values of the members vary depending on the kind of page the user navigates to.

</dd> </dl>

## Return value

The return value is ignored.

## Remarks

To launch a wizard task dialog, use the [**TaskDialogIndirect**](/windows/desktop/api/Commctrl/nf-commctrl-taskdialogindirect) function. As the user navigates using the wizard, send this message to the task dialog to display the next page. A new task dialog (looks like a new page) is created with the elements specified in the structure pointed to by *lParam*. At creation, the entire contents of the dialog frame are destroyed and reconstructed. As a result, any state information held by controls (for example, a progress bar, expando button, or verification checkbox) in the dialog is lost.

The layout of the task dialog may fail and this may not be reflected in the return value. A return value of S\_OK reflects only that the task dialog received the message and attempted to process it. If the layout of the task dialog fails (the task dialog cannot be displayed), the dialog will close and an **HRESULT** code is returned at the registered callback function. For more information on the callback function syntax, see [*TaskDialogCallbackProc*](/windows/win32/api/commctrl/nc-commctrl-pftaskdialogcallback).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

