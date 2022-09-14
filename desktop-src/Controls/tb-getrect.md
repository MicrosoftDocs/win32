---
title: TB_GETRECT message (Commctrl.h)
description: Retrieves the bounding rectangle for a specified toolbar button.
ms.assetid: a93885eb-7eb7-4434-ad51-80fb30d3bfa1
keywords:
- TB_GETRECT message Windows Controls
topic_type:
- apiref
api_name:
- TB_GETRECT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_GETRECT message

Retrieves the bounding rectangle for a specified toolbar button.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Command identifier of the button.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**RECT**](/previous-versions//dd162897(v=vs.85)) structure that will receive the bounding rectangle information.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Remarks

This message does not retrieve the bounding rectangle for buttons whose state is set to the [**TBSTATE\_HIDDEN**](toolbar-button-states.md) value.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

