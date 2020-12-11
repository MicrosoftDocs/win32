---
title: LB_SETANCHORINDEX message (Winuser.h)
description: Sets the anchor item \ 8212;that is, the item from which a multiple selection starts. A multiple selection spans all items from the anchor item to the caret item.
ms.assetid: 'vs|controls|~\controls\listboxes\listboxreference\listboxmessages\lb_setanchorindex.htm'
keywords:
- LB_SETANCHORINDEX message Windows Controls
topic_type:
- apiref
api_name:
- LB_SETANCHORINDEX
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LB\_SETANCHORINDEX message

Sets the anchor item that is, the item from which a multiple selection starts. A multiple selection spans all items from the anchor item to the caret item.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the index of the new anchor item.

Windows 95/Windows 98/Windows Millennium Edition (Windows Me) : The *wParam* parameter is limited to 16-bit values. This means list boxes cannot contain more than 32,767 items. Although the number of items is restricted, the total size in bytes of the items in a list box is limited only by available memory.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

If the message succeeds, the return value is zero.

If the message fails, the return value is LB\_ERR.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**LB\_GETANCHORINDEX**](lb-getanchorindex.md)
</dt> </dl>

 

 





