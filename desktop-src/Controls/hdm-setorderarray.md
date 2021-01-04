---
title: HDM_SETORDERARRAY message (Commctrl.h)
description: Sets the left-to-right order of header items. You can send this message explicitly or use the Header\_SetOrderArray macro.
ms.assetid: 094c424f-10bd-484d-8236-937811b703a6
keywords:
- HDM_SETORDERARRAY message Windows Controls
topic_type:
- apiref
api_name:
- HDM_SETORDERARRAY
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# HDM\_SETORDERARRAY message

Sets the left-to-right order of header items. You can send this message explicitly or use the [**Header\_SetOrderArray**](/windows/desktop/api/Commctrl/nf-commctrl-header_setorderarray) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The size of the buffer at *lParam*, in elements. This value must equal the value returned by [**HDM\_GETITEMCOUNT**](hdm-getitemcount.md).

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to an array that specifies the order in which items should be displayed, from left to right. For example, if the contents of the array are {2,0,1}, the control displays item 2, item 0, and item 1, from left to right.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





