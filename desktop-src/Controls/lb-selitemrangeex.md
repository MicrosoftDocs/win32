---
title: LB_SELITEMRANGEEX message (Winuser.h)
description: Selects one or more consecutive items in a multiple-selection list box.
ms.assetid: aac85d72-43e2-4ab0-b9ee-c7a87e21d7a1
keywords:
- LB_SELITEMRANGEEX message Windows Controls
topic_type:
- apiref
api_name:
- LB_SELITEMRANGEEX
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LB\_SELITEMRANGEEX message

Selects one or more consecutive items in a multiple-selection list box.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the zero-based index of the first item to select.

Windows 95/Windows 98/Windows Millennium Edition (Windows Me) : The *wParam* parameter is limited to 16-bit values. This means list boxes cannot contain more than 32,767 items. Although the number of items is restricted, the total size in bytes of the items in a list box is limited only by available memory.

</dd> <dt>

*lParam* 
</dt> <dd>

Specifies the zero-based index of the last item to select.

</dd> </dl>

## Return value

If an error occurs, the return value is LB\_ERR.

## Remarks

If the *wParam* parameter is less than the *lParam* parameter, the specified range of items is selected. If *wParam* is greater than or equal to *lParam*, the range is removed from the specified range of items. To select only one item, select two items and then deselect the unwanted item.

Use this message only with multiple-selection list boxes.

This message can select a range only within the first 65,536 items.

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

[**LB\_SELITEMRANGE**](lb-selitemrange.md)
</dt> <dt>

[**LB\_SETSEL**](lb-setsel.md)
</dt> </dl>

 

 





