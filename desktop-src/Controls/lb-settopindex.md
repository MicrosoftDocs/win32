---
title: LB_SETTOPINDEX message (Winuser.h)
description: Ensures that the specified item in a list box is visible.
ms.assetid: 'vs|controls|~\controls\listboxes\listboxreference\listboxmessages\lb_settopindex.htm'
keywords:
- LB_SETTOPINDEX message Windows Controls
topic_type:
- apiref
api_name:
- LB_SETTOPINDEX
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LB\_SETTOPINDEX message

Ensures that the specified item in a list box is visible.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The zero-based index of the item in the list box.

Windows 95/Windows 98/Windows Millennium Edition (Windows Me) : The *wParam* parameter is limited to 16-bit values. This means list boxes cannot contain more than 32,767 items. Although the number of items is restricted, the total size in bytes of the items in a list box is limited only by available memory.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

If an error occurs, the return value is LB\_ERR.

## Remarks

The system scrolls the list box contents so that either the specified item appears at the top of the list box or the maximum scroll range has been reached.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**LB\_GETTOPINDEX**](lb-gettopindex.md)
</dt> </dl>

 

 





