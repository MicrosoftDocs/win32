---
title: CB_GETLBTEXT message (Winuser.h)
description: Gets a string from the list of a combo box.
ms.assetid: f84e302a-65bb-45c8-958b-1cb438fb5a7a
keywords:
- CB_GETLBTEXT message Windows Controls
topic_type:
- apiref
api_name:
- CB_GETLBTEXT
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_GETLBTEXT message

Gets a string from the list of a combo box.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The zero-based index of the string to retrieve.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to the buffer that receives the string. The buffer must have sufficient space for the string and a terminating null character. You can send a [**CB\_GETLBTEXTLEN**](cb-getlbtextlen.md) message prior to the **CB\_GETLBTEXT** message to retrieve the length, in **TCHAR**s, of the string. If it is an ANSI string this is the number of bytes, but if it is a Unicode string this is the number of characters.

</dd> </dl>

## Return value

The return value is the length of the string, in **TCHAR**s, excluding the terminating null character. If *wParam* does not specify a valid index, the return value is CB\_ERR.

## Remarks

**Security Warning:** Using this message incorrectly can compromise the security of your program. This message does not provide a way for you to know the size of the buffer. If you use this message, first call [**CB\_GETLBTEXTLEN**](cb-getlbtextlen.md) to get the number of characters that are required and then call the message to retrieve the string. You should review the [Security Considerations: Microsoft Windows Controls](sec-comctls.md) before continuing.

If you create the combo box with an owner-drawn style but without the [**CBS\_HASSTRINGS**](combo-box-styles.md) style, the buffer pointed to by *lParam* receives the data associated with the item.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**CB\_GETLBTEXTLEN**](cb-getlbtextlen.md)
</dt> </dl>

 

 





