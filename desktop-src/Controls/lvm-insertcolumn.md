---
title: LVM_INSERTCOLUMN message (Commctrl.h)
description: Inserts a new column in a list-view control. You can send this message explicitly or by using the ListView\_InsertColumn macro.
ms.assetid: 1326e38e-bb45-4d0d-b5bc-ec684b3b92ef
keywords:
- LVM_INSERTCOLUMN message Windows Controls
topic_type:
- apiref
api_name:
- LVM_INSERTCOLUMN
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_INSERTCOLUMN message

Inserts a new column in a list-view control. You can send this message explicitly or by using the [**ListView\_InsertColumn**](/windows/desktop/api/Commctrl/nf-commctrl-listview_insertcolumn) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Index of the new column.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**LVCOLUMN**](/windows/win32/api/commctrl/ns-commctrl-lvcolumna) structure that contains the attributes of the new column.

</dd> </dl>

## Return value

Returns the index of the new column if successful, or -1 otherwise.

## Remarks

Columns are visible only in report (details) view.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





