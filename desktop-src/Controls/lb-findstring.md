---
title: LB_FINDSTRING message (Winuser.h)
description: Finds the first string in a list box that begins with the specified string.
ms.assetid: 1b7f25a7-0892-4d12-b3e3-21180d9ddfb1
keywords:
- LB_FINDSTRING message Windows Controls
topic_type:
- apiref
api_name:
- LB_FINDSTRING
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LB\_FINDSTRING message

Finds the first string in a list box that begins with the specified string.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The zero-based index of the item before the first item to be searched. When the search reaches the bottom of the list box, it continues searching from the top of the list box back to the item specified by the *wParam* parameter. If *wParam* is -1, the entire list box is searched from the beginning.

Windows 95/Windows 98/Windows Millennium Edition (Windows Me) : The *wParam* parameter is limited to 16-bit values. This means list boxes cannot contain more than 32,767 items. Although the number of items is restricted, the total size in bytes of the items in a list box is limited only by available memory.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to the null-terminated string that contains the string for which to search. The search is case independent, so this string can contain any combination of uppercase and lowercase letters.

</dd> </dl>

## Return value

The return value is the index of the matching item, or LB\_ERR if the search was unsuccessful.

## Remarks

If the list box has the owner-drawn style but not the [**LBS\_HASSTRINGS**](list-box-styles.md) style, the action taken by **LB\_FINDSTRING** depends on whether the [**LBS\_SORT**](list-box-styles.md) style is used. If **LBS\_SORT** is used, the system sends [**WM\_COMPAREITEM**](wm-compareitem.md) messages to the list box owner to determine which item matches the specified string. Otherwise, **LB\_FINDSTRING** attempts to find an item that has a long value (supplied as the *lParam* parameter of the [**LB\_ADDSTRING**](lb-addstring.md) or [**LB\_INSERTSTRING**](lb-insertstring.md) message) that matches the *lParam* parameter.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**LB\_FINDSTRINGEXACT**](lb-findstringexact.md)
</dt> </dl>

 

 





