---
title: LB\_GETCARETINDEX message
description: Retrieves the index of the item that has the focus in a multiple-selection list box. The item may or may not be selected.
ms.assetid: '5e9e8a37-8aed-4cfd-9360-e0de6a9b2971'
keywords: ["LB_GETCARETINDEX message Windows Controls"]
topic_type:
- apiref
api_name:
- LB_GETCARETINDEX
api_location:
- Winuser.h
api_type:
- HeaderDef
---

# LB\_GETCARETINDEX message

Retrieves the index of the item that has the focus in a multiple-selection list box. The item may or may not be selected.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used; must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used; must be zero.

</dd> </dl>

## Return value

The return value is the zero-based index of the focused list box item, or 0 if no item has the focus.

## Remarks

This message can also be used to get the index of the item that is currently selected in a single-selection list box.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**LB\_SETCARETINDEX**](lb-setcaretindex.md)
</dt> </dl>

 

 





