---
title: LB_ADDSTRING message (Winuser.h)
description: Adds a string to a list box. If the list box does not have the LBS\_SORT style, the string is added to the end of the list. Otherwise, the string is inserted into the list and the list is sorted.
ms.assetid: 924d9232-6e38-49c3-aa3e-19efd46b01ba
keywords:
- LB_ADDSTRING message Windows Controls
topic_type:
- apiref
api_name:
- LB_ADDSTRING
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LB\_ADDSTRING message

Adds a string to a list box. If the list box does not have the [**LBS\_SORT**](list-box-styles.md) style, the string is added to the end of the list. Otherwise, the string is inserted into the list and the list is sorted.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to the null-terminated string that is to be added.

If the list box has an owner-drawn style but not the [**LBS\_HASSTRINGS**](list-box-styles.md) style, this parameter is stored as item data instead of a string. You can send the **LB\_GETITEMDATA** and **LB\_SETITEMDATA** messages to retrieve or modify the item data.

</dd> </dl>

## Return value

The return value is the zero-based index of the string in the list box. If an error occurs, the return value is LB\_ERR. If there is insufficient space to store the new string, the return value is LB\_ERRSPACE.

## Remarks

If the list box has an owner-drawn style and the [**LBS\_SORT**](list-box-styles.md) style, but not the [**LBS\_HASSTRINGS**](list-box-styles.md) style, the system sends the [**WM\_COMPAREITEM**](wm-compareitem.md) message one or more times to the owner of the list box to place the new item properly in the list box.

The [**LB\_INITSTORAGE**](lb-initstorage.md) message helps speed up the initialization of list boxes that have a large number of items (more than 100). It reserves the specified amount of memory so that subsequent **LB\_ADDSTRING** messages take the shortest possible time. You can use estimates for the *wParam* and *lParam* parameters. If you overestimate, the extra memory is allocated; if you underestimate, the normal allocation is used for items that exceed the requested amount.

If the list box has the [**WS\_HSCROLL**](/windows/desktop/winmsg/window-styles) style and you add a string wider than the list box, send an [**LB\_SETHORIZONTALEXTENT**](lb-sethorizontalextent.md) message to ensure the horizontal scroll bar appears.

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

[**LB\_DELETESTRING**](lb-deletestring.md)
</dt> <dt>

[**LB\_INSERTSTRING**](lb-insertstring.md)
</dt> <dt>

[**LB\_SELECTSTRING**](lb-selectstring.md)
</dt> <dt>

[**LB\_SETHORIZONTALEXTENT**](lb-sethorizontalextent.md)
</dt> <dt>

[**WM\_COMPAREITEM**](wm-compareitem.md)
</dt> </dl>

 

