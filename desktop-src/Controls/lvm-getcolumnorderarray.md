---
title: LVM_GETCOLUMNORDERARRAY message (Commctrl.h)
description: Gets the current left-to-right order of columns in a list-view control. You can send this message explicitly or use the ListView\_GetColumnOrderArray macro.
ms.assetid: d4636aa8-c61e-4467-abc7-eea897bf370e
keywords:
- LVM_GETCOLUMNORDERARRAY message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETCOLUMNORDERARRAY
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETCOLUMNORDERARRAY message

Gets the current left-to-right order of columns in a list-view control. You can send this message explicitly or use the [**ListView\_GetColumnOrderArray**](/windows/desktop/api/Commctrl/nf-commctrl-listview_getcolumnorderarray) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The number of columns in the list-view control.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to an array of integers that receives the index values of the columns in the list-view control. The array must be large enough to hold *wParam* elements.

</dd> </dl>

## Return value

If successful, returns nonzero, and the buffer at *lParam* receives the column index of each column in the control in the order they appear from left to right. Otherwise, the return value is zero.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





