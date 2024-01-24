---
title: CB_GETLBTEXTLEN message (Winuser.h)
description: Gets the length, in characters, of a string in the list of a combo box.
ms.assetid: f0fe0eef-f9db-4d9f-9a42-5bb2aeae30a0
keywords:
- CB_GETLBTEXTLEN message Windows Controls
topic_type:
- apiref
api_name:
- CB_GETLBTEXTLEN
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_GETLBTEXTLEN message

Gets the length, in characters, of a string in the list of a combo box.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The zero-based index of the string.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

The return value is the length of the string, in **TCHAR**s, excluding the terminating null character. If an ANSI string this is the number of bytes, and if it is a Unicode string this is the number of characters. Under certain conditions, this value may actually be greater than the length of the text. For more information, see the Remarks section.

If the *wParam* parameter does not specify a valid index, the return value is CB\_ERR.

## Remarks

Under certain conditions, the return value is larger than the actual length of the text. This occurs with certain mixtures of ANSI and Unicode, and is due to the operating system allowing for the possible existence of double-byte character set (DBCS) characters within the text. The return value, however, will always be at least as large as the actual length of the text; so you can always use it to guide buffer allocation. This behavior can occur when an application uses both ANSI functions and common dialogs, which use Unicode.

To obtain the exact length of the text, use the [**WM\_GETTEXT**](/windows/desktop/winmsg/wm-gettext), [**LB\_GETTEXT**](lb-gettext.md), or [**CB\_GETLBTEXT**](cb-getlbtext.md) messages, or the [**GetWindowText**](/windows/desktop/api/winuser/nf-winuser-getwindowtexta) function.

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

[**CB\_GETLBTEXT**](cb-getlbtext.md)
</dt> <dt>

[**LB\_GETTEXT**](lb-gettext.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**GetWindowText**](/windows/desktop/api/winuser/nf-winuser-getwindowtexta)
</dt> <dt>

[**WM\_GETTEXT**](/windows/desktop/winmsg/wm-gettext)
</dt> </dl>

 

