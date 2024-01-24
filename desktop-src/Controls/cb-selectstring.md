---
title: CB_SELECTSTRING message (Winuser.h)
description: Searches the list of a combo box for an item that begins with the characters in a specified string. If a matching item is found, it is selected and copied to the edit control.
ms.assetid: c08dff72-7e44-40ed-8b64-513359292829
keywords:
- CB_SELECTSTRING message Windows Controls
topic_type:
- apiref
api_name:
- CB_SELECTSTRING
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_SELECTSTRING message

Searches the list of a combo box for an item that begins with the characters in a specified string. If a matching item is found, it is selected and copied to the edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The zero-based index of the item preceding the first item to be searched. When the search reaches the bottom of the list, it continues from the top of the list back to the item specified by the *wParam* parameter. If *wParam* is -1, the entire list is searched from the beginning.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to the null-terminated string that contains the characters for which to search. The search is not case sensitive, so this string can contain any combination of uppercase and lowercase letters.

</dd> </dl>

## Return value

If the string is found, the return value is the index of the selected item. If the search is unsuccessful, the return value is CB\_ERR and the current selection is not changed.

## Remarks

A string is selected only if the characters from the starting point match the characters in the prefix string.

If you create the combo box with an owner-drawn style but without the [**CBS\_HASSTRINGS**](combo-box-styles.md) style, what the **CB\_SELECTSTRING** message does depends on whether you use the [**CBS\_SORT**](combo-box-styles.md) style. If the **CBS\_SORT** style is used, the system sends [**WM\_COMPAREITEM**](wm-compareitem.md) messages to the owner of the combo box to determine which item matches the specified string. If you do not use the **CBS\_SORT** style, **CB\_SELECTSTRING** attempts to match the **DWORD** value against the value of the *lParam* parameter.

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

[**CB\_FINDSTRINGEXACT**](cb-findstringexact.md)
</dt> <dt>

[**CB\_SETCURSEL**](cb-setcursel.md)
</dt> <dt>

[**WM\_COMPAREITEM**](wm-compareitem.md)
</dt> </dl>

 

 





