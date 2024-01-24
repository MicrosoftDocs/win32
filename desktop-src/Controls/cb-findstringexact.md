---
title: CB_FINDSTRINGEXACT message (Winuser.h)
description: Finds the first list box string in a combo box that matches the string specified in the lParam parameter.
ms.assetid: 9065af9f-b18e-4fd5-a8cc-f780f8d0fb05
keywords:
- CB_FINDSTRINGEXACT message Windows Controls
topic_type:
- apiref
api_name:
- CB_FINDSTRINGEXACT
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_FINDSTRINGEXACT message

Finds the first list box string in a combo box that matches the string specified in the *lParam* parameter.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The zero-based index of the item preceding the first item to be searched. When the search reaches the bottom of the list box, it continues from the top of the list box back to the item specified by the *wParam* parameter. If *wParam* is -1, the entire list box is searched from the beginning.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to the null-terminated string for which to search. The search is not case sensitive, so this string can contain any combination of uppercase and lowercase letters.

</dd> </dl>

## Return value

The return value is the zero-based index of the matching item. If the search is unsuccessful, it is CB\_ERR.

## Remarks

This function is successful only if the specified string and a combo box item have the same length (except for the terminating null character) and the same characters.

If you create the combo box with an owner-drawn style but without the [**CBS\_HASSTRINGS**](combo-box-styles.md) style, the functionality of **CB\_FINDSTRINGEXACT** message depends on whether your application uses the [**CBS\_SORT**](combo-box-styles.md) style. If you use the **CBS\_SORT** style, [**WM\_COMPAREITEM**](wm-compareitem.md) messages are sent to the owner of the combo box to determine which item matches the specified string. If you do not use the **CBS\_SORT** style, the **CB\_FINDSTRINGEXACT** message searches for a list item that matches the value of the *lParam* parameter.

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

[**CB\_FINDSTRING**](cb-findstring.md)
</dt> <dt>

[**CB\_SELECTSTRING**](cb-selectstring.md)
</dt> <dt>

[**WM\_COMPAREITEM**](wm-compareitem.md)
</dt> </dl>

 

 





