---
title: BCM_SETSHIELD message (Commctrl.h)
description: Sets the elevation required state for a specified button or command link to display an elevated icon. Send this message explicitly or by using the Button\_SetElevationRequiredState macro.
ms.assetid: 2ce2a006-7136-415b-824b-46b282b100f4
keywords:
- BCM_SETSHIELD message Windows Controls
topic_type:
- apiref
api_name:
- BCM_SETSHIELD
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# BCM\_SETSHIELD message

Sets the elevation required state for a specified button or command link to display an elevated icon. Send this message explicitly or by using the [**Button\_SetElevationRequiredState**](/windows/desktop/api/Commctrl/nf-commctrl-button_setelevationrequiredstate) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* \[in\]
</dt> <dd>

A **BOOL** that is **TRUE** to draw an elevated icon, or **FALSE** otherwise.

</dd> </dl>

## Return value

Returns 1 if successful, or an error code otherwise.

## Remarks

An application must be manifested to use comctl32.dll version 6 to gain this functionality.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





