---
title: EM_SETTABLEPARMS message (Richedit.h)
description: Changes the parameters of rows in a table.
ms.assetid: 6CE9B8D1-68C9-4692-8454-24BC81E9038F
keywords:
- EM_SETTABLEPARMS message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETTABLEPARMS
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETTABLEPARMS message

Changes the parameters of rows in a table.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A pointer to a [**TABLEROWPARMS**](/windows/desktop/api/Richedit/ns-richedit-tablerowparms) structure.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**TABLECELLPARMS**](/windows/desktop/api/Richedit/ns-richedit-tablecellparms) structure.

</dd> </dl>

## Return value

Returns S\_OK if successful, or one of the following error codes.



| Return code                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_FAIL** </dt> </dl>        | Changes cannot be made. This can occur if the control is a plain-text or single-line control, or if the insertion point is inside a math object. It also occurs if tables are disabled, or if the [**EM\_SETEDITSTYLEEX**](em-seteditstyleex.md) message sets the **SES\_EX\_NOTABLE** value. <br/>                                                                                                                                                                                                                                                                              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>   | The *wParam* or *lParam* is NULL or points to an invalid structure. The **cCell** member of the [**TABLEROWPARMS**](/windows/desktop/api/Richedit/ns-richedit-tablerowparms) structure must be at least 1 and not more than 63. The **cbRow** member must equal `sizeof(TABLEROWPARMS)` or `sizeof(TABLEROWPARMS)   2*sizeof(long)`. The latter value is the size of the RichEdit 4.1 **TABLEROWPARMS** structure. The **cbCell** member of **TABLEROWPARMS** must equal `sizeof(TABLECELLPARMS)`. The insertion point must be at the start of a table or inside a table row, and the number of cells can only change by one. |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl> | Insufficient memory is available.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |



 

## Remarks

This message changes the parameters of the number of rows specified by the **cRow** member of the [**TABLEROWPARMS**](/windows/desktop/api/Richedit/ns-richedit-tablerowparms) structure, if the table has that many consecutive rows. If **cRow** is less than 0, the message iterates until the end of the table. If the new cell count differs from the current cell count by +1 or  1, it inserts or deletes the cell at the index specified by the **iCell** member of **TABLEROWPARMS**. The starting table row is identified by a character position. This position is specified by **cpStartRow** members with values that are greater than or equal to zero. The position should be inside the table row, but not inside a nested table, unless you want to change that table s parameters. If the **cpStartRow** member is  1, the character position is given by the current selection. For this, position the selection anywhere inside the table row, or select the row with the active end of the selection at the end of the table row.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_GETTABLEPARMS**](em-gettableparms.md)
</dt> </dl>

 

 





