---
title: CB_FINDSTRING message (Winuser.h)
description: Searches the list box of a combo box for an item beginning with the characters in a specified string.
ms.assetid: 872a72d5-4d8e-41c7-ac6b-eeb571403623
keywords:
- CB_FINDSTRING message Windows Controls
topic_type:
- apiref
api_name:
- CB_FINDSTRING
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_FINDSTRING message

Searches the list box of a combo box for an item beginning with the characters in a specified string.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The zero-based index of the item preceding the first item to be searched. When the search reaches the bottom of the list box, it continues from the top of the list box back to the item specified by the *wParam* parameter. If *wParam* is  -1, the entire list box is searched from the beginning.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to the null-terminated string that contains the characters for which to search. The search is not case sensitive, so this string can contain any combination of uppercase and lowercase letters.

</dd> </dl>

## Return value

The return value is the zero-based index of the matching item. If the search is unsuccessful, it is CB\_ERR.

## Remarks

If you create the combo box with an owner-drawn style but without the [**CBS\_HASSTRINGS**](combo-box-styles.md) style, what the **CB\_FINDSTRING** message does depends on whether your application uses the [**CBS\_SORT**](combo-box-styles.md) style. If you use the **CBS\_SORT** style, [**WM\_COMPAREITEM**](wm-compareitem.md) messages are sent to the owner of the combo box to determine which item matches the specified string. If you do not use the **CBS\_SORT** style, the **CB\_FINDSTRING** message searches for a list item that matches the value of the *lParam* parameter.

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

[**CB\_FINDSTRINGEXACT**](cb-findstringexact.md)
</dt> <dt>

[**CB\_SELECTSTRING**](cb-selectstring.md)
</dt> <dt>

[**CB\_SETCURSEL**](cb-setcursel.md)
</dt> <dt>

[**WM\_COMPAREITEM**](wm-compareitem.md)
</dt> </dl>

 

 





