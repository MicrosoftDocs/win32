---
title: LB_GETTEXTLEN message (Winuser.h)
description: Gets the length of a string in a list box.
ms.assetid: 866730bc-ffd4-42fd-9cea-5d326e129189
keywords:
- LB_GETTEXTLEN message Windows Controls
topic_type:
- apiref
api_name:
- LB_GETTEXTLEN
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LB\_GETTEXTLEN message

Gets the length of a string in a list box.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The zero-based index of the string.

Windows 95/Windows 98/Windows Millennium Edition (Windows Me) : The *wParam* parameter is limited to 16-bit values. This means list boxes cannot contain more than 32,767 items. Although the number of items is restricted, the total size in bytes of the items in a list box is limited only by available memory.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

The return value is the length of the string, in **TCHAR**s, excluding the terminating null character. Under certain conditions, this value may actually be greater than the length of the text. For more information, see the following Remarks section.

If the *wParam* parameter does not specify a valid index, the return value is LB\_ERR.

## Remarks

Under certain conditions, the return value is larger than the actual length of the text. This occurs with certain mixtures of ANSI and Unicode, and is due to the operating system allowing for the possible existence of double-byte character set (DBCS) characters within the text. The return value, however, will always be at least as large as the actual length of the text; you can thus always use it to guide buffer allocation. This behavior can occur when an application uses both ANSI functions and common dialogs, which use Unicode.

To obtain the exact length of the text, use the [**WM\_GETTEXT**](/windows/desktop/winmsg/wm-gettext), [**LB\_GETTEXT**](lb-gettext.md), or [**CB\_GETLBTEXT**](cb-getlbtext.md) messages, or the [**GetWindowText**](/windows/desktop/api/winuser/nf-winuser-getwindowtexta) function.

If the list box has an owner-drawn style, but not the [**LBS\_HASSTRINGS**](list-box-styles.md) style, the return value is always the size, in bytes, of a **DWORD**.

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

 

