---
title: LVM_GETFOOTERRECT message (Commctrl.h)
description: Retrieves the coordinates of the footer for a list-view control. Send this message explicitly or by using the ListView\_GetFooterRect macro.
ms.assetid: f8816f35-c1d2-4072-81d3-0a9a3df53d64
keywords:
- LVM_GETFOOTERRECT message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETFOOTERRECT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETFOOTERRECT message

Retrieves the coordinates of the footer for a list-view control. Send this message explicitly or by using the [**ListView\_GetFooterRect**](/windows/desktop/api/Commctrl/nf-commctrl-listview_getfooterrect) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used. Must be 0.

</dd> <dt>

*lParam* \[in, out\]
</dt> <dd>

A pointer to a [**RECT**](/previous-versions//dd162897(v=vs.85)) structure to receive the coordinates. The calling process is responsible for allocating this structure. The coordinates received are expressed as client coordinates.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

