---
title: LB_SELITEMRANGE message (Winuser.h)
description: Selects or deselects one or more consecutive items in a multiple-selection list box.
ms.assetid: 817d62df-98a3-40b3-8d62-86bf07ad797f
keywords:
- LB_SELITEMRANGE message Windows Controls
topic_type:
- apiref
api_name:
- LB_SELITEMRANGE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LB\_SELITEMRANGE message

Selects or deselects one or more consecutive items in a multiple-selection list box.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

**TRUE** to select the range of items, or **FALSE** to deselect it.

</dd> <dt>

*lParam* 
</dt> <dd>

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) specifies the zero-based index of the first item to select. The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) specifies the zero-based index of the last item to select.

</dd> </dl>

## Return value

If an error occurs, the return value is LB\_ERR.

## Remarks

Use this message only with multiple-selection list boxes.

This message can select a range only within the first 65,536 items.

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

[**LB\_SELITEMRANGEEX**](lb-selitemrangeex.md)
</dt> <dt>

[**LB\_SETSEL**](lb-setsel.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**MAKELPARAM**](/windows/desktop/api/winuser/nf-winuser-makelparam)
</dt> </dl>

 

