---
title: LB_GETCARETINDEX message (Winuser.h)
description: Retrieves the index of the item that has the focus in a multiple-selection list box. The item may or may not be selected.
ms.assetid: 'vs|controls|~\controls\listboxes\listboxreference\listboxmessages\lb_getcaretindex.htm'
keywords:
- LB_GETCARETINDEX message Windows Controls
topic_type:
- apiref
api_name:
- LB_GETCARETINDEX
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
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



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**LB\_SETCARETINDEX**](lb-setcaretindex.md)
</dt> </dl>

 

 





