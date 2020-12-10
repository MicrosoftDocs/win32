---
title: LB_GETCURSEL message (Winuser.h)
description: Gets the index of the currently selected item, if any, in a single-selection list box.
ms.assetid: 39ab7f77-6c8e-45a4-aad4-47eba0a11a11
keywords:
- LB_GETCURSEL message Windows Controls
topic_type:
- apiref
api_name:
- LB_GETCURSEL
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LB\_GETCURSEL message

Gets the index of the currently selected item, if any, in a single-selection list box.

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

In a single-selection list box, the return value is the zero-based index of the currently selected item. If there is no selection, the return value is LB\_ERR.

## Remarks

To retrieve the indexes of the selected items in a multiple-selection list box, use the [**LB\_GETSELITEMS**](lb-getselitems.md) message. To determine whether the item that has the focus rectangle in a multiple selection list box is selected, use the [**LB\_GETSEL**](lb-getsel.md) message.

If sent to a multiple-selection list box, **LB\_GETCURSEL** returns the index of the item that has the focus rectangle. If no items are selected, it returns zero.

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

[**LB\_GETCARETINDEX**](lb-getcaretindex.md)
</dt> <dt>

[**LB\_GETSEL**](lb-getsel.md)
</dt> <dt>

[**LB\_GETSELITEMS**](lb-getselitems.md)
</dt> <dt>

[**LB\_SETCURSEL**](lb-setcursel.md)
</dt> </dl>

 

 





