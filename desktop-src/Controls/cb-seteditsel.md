---
title: CB_SETEDITSEL message (Winuser.h)
description: An application sends a CB\_SETEDITSEL message to select characters in the edit control of a combo box.
ms.assetid: 25a07341-a21c-42a9-a220-62650997757b
keywords:
- CB_SETEDITSEL message Windows Controls
topic_type:
- apiref
api_name:
- CB_SETEDITSEL
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_SETEDITSEL message

An application sends a **CB\_SETEDITSEL** message to select characters in the edit control of a combo box.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* \[in\]
</dt> <dd>

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) of *lParam* specifies the starting position. If the **LOWORD** is -1, the selection, if any, is removed.

The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) of *lParam* specifies the ending position. If the **HIWORD** is -1, all text from the starting position to the last character in the edit control is selected.

</dd> </dl>

## Return value

If the message succeeds, the return value is **TRUE**. If the message is sent to a combo box with the [**CBS\_DROPDOWNLIST**](combo-box-styles.md) style, it is CB\_ERR.

## Remarks

The positions are zero-based. The first character of the edit control is in the zero position. The first character after the last selected character is in the ending position. For example, to select the first four characters of the edit control, use a starting position of 0 and an ending position of 4.

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

[**CB\_GETEDITSEL**](cb-geteditsel.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**MAKELPARAM**](/windows/desktop/api/winuser/nf-winuser-makelparam)
</dt> </dl>

 

