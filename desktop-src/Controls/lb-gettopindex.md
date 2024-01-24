---
title: LB_GETTOPINDEX message (Winuser.h)
description: Gets the index of the first visible item in a list box.
ms.assetid: 'vs|controls|~\controls\listboxes\listboxreference\listboxmessages\lb_gettopindex.htm'
keywords:
- LB_GETTOPINDEX message Windows Controls
topic_type:
- apiref
api_name:
- LB_GETTOPINDEX
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LB\_GETTOPINDEX message

Gets the index of the first visible item in a list box. Initially the item with index 0 is at the top of the list box, but if the list box contents have been scrolled another item may be at the top. The first visible item in a multiple-column list box is the top-left item.

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

The return value is the index of the first visible item in the list box.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**LB\_SETTOPINDEX**](lb-settopindex.md)
</dt> </dl>

 

 





