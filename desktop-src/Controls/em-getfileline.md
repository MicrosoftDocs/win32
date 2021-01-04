---
title: EM_GETFILELINE message (CommCtrl.h)
description: Copies a line of text from an edit control, independently of how lines are displayed on the screen, and places it in a specified buffer.
ms.assetid: ff56d2c6-5013-46c6-90d8-ee2bdc9074b1
keywords:
- EM_GETFILELINE message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETLINE
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 10/19/2018
---

# EM_GETFILELINE message (CommCtrl.h)

Copies a line of text from an edit control, independently of how lines are displayed on the screen, and places it in a specified buffer.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The zero-based index of the line to retrieve from a multiline edit control. A value of zero specifies the topmost line. This parameter is ignored by a single-line edit control.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to the buffer that receives a copy of the line. Before sending the message, set the first word of this buffer to the size, in **TCHAR**s, of the buffer. For ANSI text, this is the number of bytes; for Unicode text, this is the number of characters. The size in the first word is overwritten by the copied line.

</dd> </dl>

## Return value

The return value is the number of **TCHAR**s copied. The return value is zero if the line number specified by the *wParam* parameter is greater than the number of lines in the edit control.

## Remarks

The copied line does not contain a terminating null character.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, 1809 \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2019 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>CommCtrl.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**EM\_FILELINELENGTH**](em-filelinelength.md)
</dt> <dt>

[**Edit\_GetFileLine**](/windows/win32/api/commctrl/nf-commctrl-edit_getfileline)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**WM\_GETTEXT**](/windows/desktop/winmsg/wm-gettext)
</dt> </dl>

 

