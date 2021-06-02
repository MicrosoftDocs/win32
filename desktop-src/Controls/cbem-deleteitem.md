---
title: CBEM_DELETEITEM message (Commctrl.h)
description: Removes an item from a ComboBoxEx control.
ms.assetid: 688cf388-54ba-4b45-88d7-628da49d8615
keywords:
- CBEM_DELETEITEM message Windows Controls
topic_type:
- apiref
api_name:
- CBEM_DELETEITEM
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CBEM\_DELETEITEM message

Removes an item from a ComboBoxEx control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The zero-based index of the item to be removed.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns an INT value that represents the number of items remaining in the control. If *iIndex* is invalid, the message returns CB\_ERR.

## Remarks

This message maps to the combo box control message [**CB\_DELETESTRING**](cb-deletestring.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





