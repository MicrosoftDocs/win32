---
title: DTM_GETIDEALSIZE message (Commctrl.h)
description: Gets the size needed to display the control without clipping. Send this message explicitly or by using the DateTime\_GetIdealSize macro.
ms.assetid: 15ec26a1-645b-4a96-af66-1031e1a46c6c
keywords:
- DTM_GETIDEALSIZE message Windows Controls
topic_type:
- apiref
api_name:
- DTM_GETIDEALSIZE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DTM\_GETIDEALSIZE message

Gets the size needed to display the control without clipping. Send this message explicitly or by using the [**DateTime\_GetIdealSize**](/windows/desktop/api/Commctrl/nf-commctrl-datetime_getidealsize) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used. Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**SIZE**](/previous-versions//dd145106(v=vs.85)) structure to receive the ideal size. The calling application is responsible for allocating this structure.

</dd> </dl>

## Return value

Returns **TRUE**.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

