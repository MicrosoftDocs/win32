---
title: TDM_CLICK_BUTTON message (Commctrl.h)
description: Simulates the action of a button click in a task dialog.
ms.assetid: cc8a8252-3418-4a28-bfb7-11d6e3fee903
keywords:
- TDM_CLICK_BUTTON message Windows Controls
topic_type:
- apiref
api_name:
- TDM_CLICK_BUTTON
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TDM\_CLICK\_BUTTON message

Simulates the action of a button click in a task dialog.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

An **int** that specifies the ID of the button to be clicked.

</dd> <dt>

*lParam* \[in\]
</dt> <dd>

Must be zero.

</dd> </dl>

## Return value

The return value is ignored.

## Remarks

The button ID specified by *wParam* is sent to the [**TaskDialogCallbackProc**](/windows/win32/api/commctrl/nc-commctrl-pftaskdialogcallback) callback function as part of a [TDN\_BUTTON\_CLICKED](tdn-button-clicked.md) notification code. After the callback function returns, the task dialog is closed if S\_OK was returned from the callback function. If S\_FALSE was returned from the callback function, the task dialog remains active.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

