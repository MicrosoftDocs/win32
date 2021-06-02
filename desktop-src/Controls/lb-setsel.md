---
title: LB_SETSEL message (Winuser.h)
description: Selects an item in a multiple-selection list box and, if necessary, scrolls the item into view.
ms.assetid: 643783f2-0e00-4b79-b957-47938bb9f8da
keywords:
- LB_SETSEL message Windows Controls
topic_type:
- apiref
api_name:
- LB_SETSEL
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LB\_SETSEL message

Selects an item in a multiple-selection list box and, if necessary, scrolls the item into view.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies how to set the selection. If this parameter is **TRUE**, the item is selected and highlighted; if it is **FALSE**, the highlight is removed and the item is no longer selected.

</dd> <dt>

*lParam* 
</dt> <dd>

Specifies the zero-based index of the item to set. If this parameter is -1, the selection is added to or removed from all items, depending on the value of *wParam*, and no scrolling occurs.

</dd> </dl>

## Return value

If an error occurs, the return value is LB\_ERR.

## Remarks

Use this message only with multiple-selection list boxes.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**LB\_GETSEL**](lb-getsel.md)
</dt> <dt>

[**LB\_SELITEMRANGE**](lb-selitemrange.md)
</dt> </dl>

 

 





