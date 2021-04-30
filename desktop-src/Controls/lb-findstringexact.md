---
title: LB_FINDSTRINGEXACT message (Winuser.h)
description: Finds the first list box string that exactly matches the specified string, except that the search is not case sensitive.
ms.assetid: 9bfe21af-626d-4416-aa20-65c425bd99af
keywords:
- LB_FINDSTRINGEXACT message Windows Controls
topic_type:
- apiref
api_name:
- LB_FINDSTRINGEXACT
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LB\_FINDSTRINGEXACT message

Finds the first list box string that exactly matches the specified string, except that the search is not case sensitive.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The zero-based index of the item before the first item to be searched. When the search reaches the bottom of the list box, it continues searching from the top of the list box back to the item specified by the *wParam* parameter. If *wParam* is -1, the entire list box is searched from the beginning.

Windows 95/Windows 98/Windows Millennium Edition (Windows Me) : The *wParam* parameter is limited to 16-bit values. This means list boxes cannot contain more than 32,767 items. Although the number of items is restricted, the total size in bytes of the items in a list box is limited only by available memory.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to the null-terminated string for which to search. The search is not case sensitive, so this string can contain any combination of uppercase and lowercase letters.

</dd> </dl>

## Return value

The return value is the zero-based index of the matching item, or LB\_ERR if the search was unsuccessful.

## Remarks

This function is only successful if the specified string and a list box item have the same length (except for the null at the end of the specified string) and have exactly the same characters.

If the list box has the owner-drawn style but not the [**LBS\_HASSTRINGS**](list-box-styles.md) style, the action taken by **LB\_FINDSTRINGEXACT** depends on whether the [**LBS\_SORT**](list-box-styles.md) style is used. If **LBS\_SORT** is used, the system sends [**WM\_COMPAREITEM**](wm-compareitem.md) messages to the list box owner to determine which item matches the specified string. Otherwise, **LB\_FINDSTRINGEXACT** attempts to find an item that has a long value (supplied as the *lParam* parameter of the [**LB\_ADDSTRING**](lb-addstring.md) or [**LB\_INSERTSTRING**](lb-insertstring.md) message) that matches the *lParam* parameter.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**LB\_FINDSTRING**](lb-findstring.md)
</dt> </dl>

 

 





