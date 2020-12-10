---
title: LB_INSERTSTRING message (Winuser.h)
description: Inserts a string or item data into a list box. Unlike the LB\_ADDSTRING message, the LB\_INSERTSTRING message does not cause a list with the LBS\_SORT style to be sorted.
ms.assetid: dfaa742d-2f42-4485-aed5-cda8ca9ba66c
keywords:
- LB_INSERTSTRING message Windows Controls
topic_type:
- apiref
api_name:
- LB_INSERTSTRING
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LB\_INSERTSTRING message

Inserts a string or item data into a list box. Unlike the [**LB\_ADDSTRING**](lb-addstring.md) message, the **LB\_INSERTSTRING** message does not cause a list with the [**LBS\_SORT**](list-box-styles.md) style to be sorted.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The zero-based index of the position at which to insert the string. If this parameter is -1, the string is added to the end of the list.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to the null-terminated string to be inserted. If the list box has an owner-drawn style but not the [**LBS\_HASSTRINGS**](list-box-styles.md) style, this parameter is stored as item data instead of a string. You can send the [**LB\_GETITEMDATA**](lb-getitemdata.md) and [**LB\_SETITEMDATA**](lb-setitemdata.md) messages to retrieve or modify the item data.

</dd> </dl>

## Return value

The return value is the index of the position at which the string was inserted. If an error occurs, the return value is LB\_ERR. If there is insufficient space to store the new string, the return value is LB\_ERRSPACE.

## Remarks

The [**LB\_INITSTORAGE**](lb-initstorage.md) message helps speed up the initialization of list boxes that have a large number of items (more than 100). It reserves the specified amount of memory so that subsequent **LB\_INSERTSTRING** messages take the shortest possible time. You can use estimates for the *wParam* and *lParam* parameters. If you overestimate, the extra memory is allocated; if you underestimate, the normal allocation is used for items that exceed the requested amount.

If the list box has [**WS\_HSCROLL**](/windows/desktop/winmsg/window-styles) style and you insert a string wider than the list box, send an [**LB\_SETHORIZONTALEXTENT**](lb-sethorizontalextent.md) message to ensure the horizontal scroll bar appears.

For an ANSI application, the system converts the text in a list box to Unicode using CP\_ACP. This can cause problems. For example, accented Roman characters in a non-Unicode list box in Japanese Windows will come out garbled. To fix this, either compile the application as Unicode or use an owner-drawn list box.

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

[**LB\_ADDSTRING**](lb-addstring.md)
</dt> <dt>

[**LB\_SELECTSTRING**](lb-selectstring.md)
</dt> <dt>

[**LB\_SETHORIZONTALEXTENT**](lb-sethorizontalextent.md)
</dt> </dl>

 

