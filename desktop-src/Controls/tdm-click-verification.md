---
title: TDM_CLICK_VERIFICATION message (Commctrl.h)
description: Simulates a click of the verification checkbox of a task dialog, if it exists.
ms.assetid: 1c6c135e-4e39-4f1a-88f4-5e9f7181a2dd
keywords:
- TDM_CLICK_VERIFICATION message Windows Controls
topic_type:
- apiref
api_name:
- TDM_CLICK_VERIFICATION
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TDM\_CLICK\_VERIFICATION message

Simulates a click of the verification checkbox of a task dialog, if it exists.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

**TRUE** to set the state of the checkbox to be checked; **FALSE** to set it to be unchecked.

</dd> <dt>

*lParam* \[in\]
</dt> <dd>

**TRUE** to set the keyboard focus to the checkbox; **FALSE** otherwise.

</dd> </dl>

## Return value

The return value is ignored.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





