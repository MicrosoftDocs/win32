---
title: RB_SIZETORECT message (Commctrl.h)
description: Attempts to find the best layout of the bands for the given rectangle.
ms.assetid: c6242b54-bd65-489b-b417-9680cc39b64a
keywords:
- RB_SIZETORECT message Windows Controls
topic_type:
- apiref
api_name:
- RB_SIZETORECT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# RB\_SIZETORECT message

Attempts to find the best layout of the bands for the given rectangle.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**RECT**](/previous-versions//dd162897(v=vs.85)) structure that specifies the rectangle to which the rebar control should be sized.

</dd> </dl>

## Return value

Returns nonzero if a layout change occurred, or zero otherwise.

## Remarks

The rebar bands will be arranged and wrapped as necessary to fit the rectangle. Bands that have the RBBS\_VARIABLEHEIGHT style will be resized as evenly as possible to fit the rectangle. The height of a horizontal rebar or the width of a vertical rebar may change, depending on the new layout.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

