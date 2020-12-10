---
title: SB_GETRECT message (Commctrl.h)
description: Retrieves the bounding rectangle of a part in a status window.
ms.assetid: 76b8d470-07ae-440b-9bf5-7875b80b0168
keywords:
- SB_GETRECT message Windows Controls
topic_type:
- apiref
api_name:
- SB_GETRECT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# SB\_GETRECT message

Retrieves the bounding rectangle of a part in a status window.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Zero-based index of the part whose bounding rectangle is to be retrieved.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**RECT**](/previous-versions//dd162897(v=vs.85)) structure that receives the bounding rectangle.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

