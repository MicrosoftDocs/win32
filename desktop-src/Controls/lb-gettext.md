---
title: LB_GETTEXT message (Winuser.h)
description: Gets a string from a list box.
ms.assetid: 6bf7ec3b-237b-4668-9493-40c098a32428
keywords:
- LB_GETTEXT message Windows Controls
topic_type:
- apiref
api_name:
- LB_GETTEXT
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LB\_GETTEXT message

Gets a string from a list box.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The zero-based index of the string to retrieve.

Windows 95/Windows 98/Windows Millennium Edition (Windows Me) : The *wParam* parameter is limited to 16-bit values. This means list boxes cannot contain more than 32,767 items. Although the number of items is restricted, the total size in bytes of the items in a list box is limited only by available memory.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to the buffer that will receive the string; it is type **LPTSTR** which is subsequently cast to an **LPARAM**. The buffer must have sufficient space for the string and a terminating null character. An [**LB\_GETTEXTLEN**](lb-gettextlen.md) message can be sent before the **LB\_GETTEXT** message to retrieve the length, in **TCHAR**s, of the string.

</dd> </dl>

## Return value

The return value is the length of the string, in **TCHAR**s, excluding the terminating null character. If *wParam* does not specify a valid index, the return value is LB\_ERR.

## Remarks

If the list box has an owner-drawn style but not the [**LBS\_HASSTRINGS**](list-box-styles.md) style, the buffer pointed to by the *lParam* parameter receives the value associated with the item (the item data).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**LB\_GETTEXTLEN**](lb-gettextlen.md)
</dt> </dl>

 

 





