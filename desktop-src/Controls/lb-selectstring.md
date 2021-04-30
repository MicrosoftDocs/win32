---
title: LB_SELECTSTRING message (Winuser.h)
description: Searches a list box for an item that begins with the characters in a specified string. If a matching item is found, the item is selected.
ms.assetid: fd443ade-665d-439a-8951-3d9fed50695b
keywords:
- LB_SELECTSTRING message Windows Controls
topic_type:
- apiref
api_name:
- LB_SELECTSTRING
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LB\_SELECTSTRING message

Searches a list box for an item that begins with the characters in a specified string. If a matching item is found, the item is selected.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The zero-based index of the item before the first item to be searched. When the search reaches the bottom of the list box, it continues from the top of the list box back to the item specified by the *wParam* parameter. If *wParam* is -1, the entire list box is searched from the beginning.

Windows 95/Windows 98/Windows Millennium Edition (Windows Me) : The *wParam* parameter is limited to 16-bit values. This means list boxes cannot contain more than 32,767 items. Although the number of items is restricted, the total size in bytes of the items in a list box is limited only by available memory.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to the null-terminated string that contains the prefix for which to search. The search is case independent, so this string can contain any combination of uppercase and lowercase letters.

</dd> </dl>

## Return value

If the search is successful, the return value is the index of the selected item. If the search is unsuccessful, the return value is LB\_ERR and the current selection is not changed.

## Remarks

The list box is scrolled, if necessary, to bring the selected item into view.

Do not use this message with a list box that has the [**LBS\_MULTIPLESEL**](list-box-styles.md) or the [**LBS\_EXTENDEDSEL**](list-box-styles.md) styles.

An item is selected only if its initial characters from the starting point match the characters in the string specified by the *lParam* parameter.

If the list box has the owner-drawn style but not the [**LBS\_HASSTRINGS**](list-box-styles.md) style, the action taken by **LB\_SELECTSTRING** depends on whether the [**LBS\_SORT**](list-box-styles.md) style is used. If **LBS\_SORT** is used, the system sends [**WM\_COMPAREITEM**](wm-compareitem.md) messages to the list box owner to determine which item matches the specified string. Otherwise, **LB\_SELECTSTRING** attempts to find an item that has a long value (supplied as the *lParam* parameter of the [**LB\_ADDSTRING**](lb-addstring.md) or [**LB\_INSERTSTRING**](lb-insertstring.md) message) that matches the *lParam* parameter.

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

[**LB\_FINDSTRING**](lb-findstring.md)
</dt> <dt>

[**LB\_INSERTSTRING**](lb-insertstring.md)
</dt> </dl>

 

 





