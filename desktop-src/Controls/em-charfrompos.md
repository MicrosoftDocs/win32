---
title: EM_CHARFROMPOS message (Winuser.h)
description: Gets information about the character closest to a specified point in the client area of an edit control. You can send this message to either an edit control or a rich edit control.
ms.assetid: fe9f96f2-5b3c-4039-befd-5e9a456ba32d
keywords:
- EM_CHARFROMPOS message Windows Controls
topic_type:
- apiref
api_name:
- EM_CHARFROMPOS
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_CHARFROMPOS message

Gets information about the character closest to a specified point in the client area of an edit control. You can send this message to either an edit control or a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

The coordinates of a point in the control's client area. The coordinates are in screen units and are relative to the upper-left corner of the control's client area.

**Rich edit controls:** A pointer to a [**POINTL**](/previous-versions//dd162807(v=vs.85)) structure that contains the horizontal and vertical coordinates.

**Edit controls:** The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) contains the horizontal coordinate. The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) contains the vertical coordinate.

</dd> </dl>

## Return value

**Rich edit controls:** The return value specifies the zero-based character index of the character nearest the specified point. The return value indicates the last character in the edit control if the specified point is beyond the last character in the control.

**Edit controls:** The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) specifies the zero-based index of the character nearest the specified point. This index is relative to the beginning of the control, not the beginning of the line. If the specified point is beyond the last character in the edit control, the return value indicates the last character in the control. The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) specifies the zero-based index of the line that contains the character. For single-line edit controls, this value is zero. The index indicates the line delimiter if the specified point is beyond the last visible character in a line.

## Remarks

**Rich Edit:** Supported in Microsoft Rich Edit 1.0 and later. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

If a point is passed to **EM\_CHARFROMPOS** as the *lParam* and the point is outside the bounds of the edit control, then the *lResult* is (65535, 65535).

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

[**EM\_POSFROMCHAR**](em-posfromchar.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**MAKELPARAM**](/windows/desktop/api/winuser/nf-winuser-makelparam)
</dt> <dt>

[**POINTL**](/previous-versions//dd162807(v=vs.85))
</dt> </dl>

 

