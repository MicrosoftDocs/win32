---
title: EM_GETTEXTEX message (Richedit.h)
description: Gets the text from a rich edit control.
ms.assetid: 46431563-fde1-4407-ab7a-b2248c0e12b8
keywords:
- EM_GETTEXTEX message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETTEXTEX
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_GETTEXTEX message

Gets the text from a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Pointer to a [**GETTEXTEX**](/windows/desktop/api/Richedit/ns-richedit-gettextex) structure, which indicates how to translate the text before putting it into the output buffer.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to the buffer to receive the text. The size of this buffer, in bytes, is specified by the **cb** member of the [**GETTEXTEX**](/windows/desktop/api/Richedit/ns-richedit-gettextex) structure. Use the [**EM\_GETTEXTLENGTHEX**](em-gettextlengthex.md) message to get the required size of the buffer.

</dd> </dl>

## Return value

The return value is the number of **TCHAR**s copied into the output buffer, including the null terminator.

## Remarks

If the size of the output buffer is less than the size of the text in the control, the edit control will copy text from its beginning and place it in the buffer until the buffer is full. A terminating null character will still be placed at the end of the buffer.

If ANSI text is requested, **EM\_GETTEXTEX** uses the [**WideCharToMultiByte**](/windows/desktop/api/stringapiset/nf-stringapiset-widechartomultibyte) function to translate the Unicode characters to ANSI. It allows you to go from Unicode to ANSI using a particular code page. The [**GETTEXTEX**](/windows/desktop/api/Richedit/ns-richedit-gettextex) structure contains members (**lpDefaultChar** and **lpUsedDefChar**) that are used in the translation from Unicode to ANSI.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**EM\_SETTEXTEX**](em-settextex.md)
</dt> <dt>

[**GETTEXTEX**](/windows/desktop/api/Richedit/ns-richedit-gettextex)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**WideCharToMultiByte**](/windows/desktop/api/stringapiset/nf-stringapiset-widechartomultibyte)
</dt> <dt>

[**WM\_SETTEXT**](/windows/desktop/winmsg/wm-settext)
</dt> </dl>

 

