---
title: EM_SHOWSCROLLBAR message (Richedit.h)
description: Shows or hides one of the scroll bars in the host window of a rich edit control.
ms.assetid: 0a6ec010-4870-4faf-9dc2-1da961dc8194
keywords:
- EM_SHOWSCROLLBAR message Windows Controls
topic_type:
- apiref
api_name:
- EM_SHOWSCROLLBAR
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SHOWSCROLLBAR message

Shows or hides one of the scroll bars in the host window of a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Identifies which scroll bar to display: horizontal or vertical. This parameter must be **SB\_VERT** or **SB\_HORZ**.

</dd> <dt>

*lParam* 
</dt> <dd>

Specifies whether to show the scroll bar or hide it. Specify **TRUE** to show the scroll bar and **FALSE** to hide it.

</dd> </dl>

## Return value

This message does not return a value.

## Remarks

This method is only valid when the control is in-place active. Calls made while the control is inactive may fail.

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

[**EM\_GETSCROLLPOS**](em-getscrollpos.md)
</dt> <dt>

[**EM\_SETSCROLLPOS**](em-setscrollpos.md)
</dt> </dl>

 

 





