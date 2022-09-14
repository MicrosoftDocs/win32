---
title: CB_GETTOPINDEX message (Winuser.h)
description: An application sends the CB\_GETTOPINDEX message to retrieve the zero-based index of the first visible item in the list box portion of a combo box.
ms.assetid: 'vs|controls|~\controls\comboboxes\comboboxreference\comboboxmessages\cb_gettopindex.htm'
keywords:
- CB_GETTOPINDEX message Windows Controls
topic_type:
- apiref
api_name:
- CB_GETTOPINDEX
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_GETTOPINDEX message

An application sends the **CB\_GETTOPINDEX** message to retrieve the zero-based index of the first visible item in the list box portion of a combo box. Initially, the item with index 0 is at the top of the list box, but if the list box contents have been scrolled, another item may be at the top.

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

If the message is successful, the return value is the index of the first visible item in the list box of the combo box.

If the message fails, the return value is CB\_ERR.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**CB\_SETTOPINDEX**](cb-settopindex.md)
</dt> </dl>

 

 





