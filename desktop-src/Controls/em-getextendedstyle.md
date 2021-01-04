---
title: EM_GETEXTENDEDSTYLE message (Commctrl.h)
description: Retrieves the extended style for an edit control. Send this message explicitly or by using the Edit\_GetExtendedStyle macro.
ms.assetid: 557f796e-c9d1-4ea1-b8a6-44ae0bed5ffc
keywords:
- EM_GETEXTENDEDSTYLE message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETEXTENDEDSTYLE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 10/19/2018
---

# EM_GETEXTENDEDSTYLE message (Commctrl.h)

Retrieves the extended style for a tree-view control. Send this message explicitly or by using the [**Edit\_GetExtendedStyle**](/windows/desktop/api/Commctrl/nf-commctrl-edit_getextendedstyle) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the value of extended style.For more information on styles, see [Edit Control Extended Styles](edit-control-window-extended-styles.md).

## Remarks

The extended styles for an edit control have nothing to do with the extended styles used with function [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) or function [**SetWindowLong**](/windows/desktop/api/winuser/nf-winuser-setwindowlonga).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1809 \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows Server 2019 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

