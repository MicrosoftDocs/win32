---
title: EM_SETRECTNP message (Winuser.h)
description: EM_SETRECTNP message - Sets the formatting rectangle of a multiline edit control.
ms.assetid: 1ab497ca-023f-4c26-b92d-b441a0d7b90c
keywords:
- EM_SETRECTNP message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETRECTNP
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETRECTNP message

Sets the [formatting rectangle](about-edit-controls.md) of a multiline edit control. The **EM\_SETRECTNP** message is identical to the [**EM\_SETRECT**](em-setrect.md) message, except that **EM\_SETRECTNP** does *not* redraw the edit control window.

The formatting rectangle is the limiting rectangle into which the control draws the text. The limiting rectangle is independent of the size of the edit control window.

This message is processed only by multiline edit controls. You can send this message to either an edit control or a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

**Rich Edit 3.0 and later:** Indicates whether the new rectangle contains absolute or relative coordinates. A value of zero indicates absolute coordinates. A value of 1 indicates offsets relative to the current formatting rectangle. (The offsets can be positive or negative.)

**Edit controls:** This parameter is not used and must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**RECT**](/windows/win32/api/windef/ns-windef-rect) structure that specifies the new dimensions of the rectangle. If this parameter is **NULL**, the formatting rectangle is set to its default values.

</dd> </dl>

## Return value

This message does not return a value.

## Remarks

**Rich Edit:** Supported in Microsoft Rich Edit 3.0 and later. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

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

[**EM\_SETRECT**](em-setrect.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**RECT**](/windows/win32/api/windef/ns-windef-rect)
</dt> </dl>

 

