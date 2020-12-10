---
title: EM_GETSEL message (Winuser.h)
description: Gets the starting and ending character positions (in TCHARs) of the current selection in an edit control. You can send this message to either an edit control or a rich edit control.
ms.assetid: cf12aaea-cfa7-4804-ae34-fd0992332288
keywords:
- EM_GETSEL message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETSEL
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_GETSEL message

Gets the starting and ending character positions (in **TCHAR**s) of the current selection in an edit control. You can send this message to either an edit control or a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A pointer to a **DWORD** value that receives the starting position of the selection. This parameter can be **NULL**.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a **DWORD** value that receives the position of the first unselected character after the end of the selection. This parameter can be **NULL**.

</dd> </dl>

## Return value

The return value is a zero-based value with the starting position of the selection in the [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) and the position of the first **TCHAR** after the last selected **TCHAR** in the [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)). If either of these values exceeds 65,535, the return value is -1.

It is better to use the values returned in *wParam* and *lParam* because they are full 32-bit values.

## Remarks

If there is no selection, the starting and ending values are both the position of the caret.

**Rich edit controls:** You can also use the [**EM\_EXGETSEL**](em-exgetsel.md) message to retrieve the same information. **EM\_EXGETSEL** also returns starting and ending character positions as 32-bit values.

**Rich Edit:** Supported in Microsoft Rich Edit 1.0 and later. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

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

[**EM\_EXGETSEL**](em-exgetsel.md)
</dt> <dt>

[**EM\_SETSEL**](em-setsel.md)
</dt> </dl>

 

