---
title: EM_GETTABLEPARMS message (Richedit.h)
description: Retrieves the table parameters for a table row and the cell parameters for the specified number of cells.
ms.assetid: 36ADA41B-735B-4D6E-92B1-33260C71DF73
keywords:
- EM_GETTABLEPARMS message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETTABLEPARMS
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_GETTABLEPARMS message

Retrieves the table parameters for a table row and the cell parameters for the specified number of cells.


```C++
#define EM_GETTABLEPARMS       (WM_USER + 265)
```



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



| Return code                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_FAIL** </dt> </dl>        | Changes cannot be made. This can occur if the control is a plain-text or single-line control, or if the insertion point is inside a math object. It also occurs if tables are disabled if the [**EM\_SETEDITSTYLEEX**](em-seteditstyleex.md) message sets the **SES\_EX\_NOTABLE** value. <br/>                                                                                                                                                                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>   | The *wParam* or *lParam* is NULL or points to an invalid structure. The **cbRow** member of the [**TABLEROWPARMS**](/windows/desktop/api/Richedit/ns-richedit-tablerowparms) structure must equal `sizeof(TABLEROWPARMS)` or sizeof(TABLEROWPARMS)   2\*sizeof(long). The latter value is the size of the RichEdit 4.1 **TABLEROWPARMS** structure. The **cbCell** member of the **TABLEROWPARMS** structure must equal `sizeof(TABLECELLPARMS)`. The query character position must be at a table row delimiter. |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl> | Insufficient memory is available.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                               |



 

## Remarks

This message gets the table parameters for the row at the character position specified by the **cpStartRow** member of the [**TABLEROWPARMS**](/windows/desktop/api/Richedit/ns-richedit-tablerowparms) structure, and the number of cells specified by the **cCells** member of the [**TABLECELLPARMS**](/windows/desktop/api/Richedit/ns-richedit-tablecellparms) structure.

The character position specified by the **cpStartRow** member of the [**TABLEROWPARMS**](/windows/desktop/api/Richedit/ns-richedit-tablerowparms) structure should be at the start of the table row, or at the end delimiter of the table row. If **cpStartRow** is set to  1, the character position is given by the current selection. In this case, position the selection at the end of the row (between the cell mark and the end delimiter of the table row), or select the row.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_SETTABLEPARMS**](em-settableparms.md)
</dt> </dl>

 

 





