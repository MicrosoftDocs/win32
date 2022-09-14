---
title: CB_GETEXTENDEDUI message (Winuser.h)
description: Determines whether a combo box has the default user interface or the extended user interface.
ms.assetid: 4f5580e0-68b1-4584-bf79-561fb8222fe0
keywords:
- CB_GETEXTENDEDUI message Windows Controls
topic_type:
- apiref
api_name:
- CB_GETEXTENDEDUI
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_GETEXTENDEDUI message

Determines whether a combo box has the default user interface or the extended user interface.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used; must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used; must be zero.

</dd> </dl>

## Return value

If the combo box has the extended user interface, the return value is **TRUE**; otherwise, it is **FALSE**.

## Remarks

By default, the F4 key opens or closes the list and the DOWN ARROW changes the current selection. In a combo box with the extended user interface, the F4 key is disabled and pressing the DOWN ARROW key opens the drop-down list.

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

[**CB\_SETEXTENDEDUI**](cb-setextendedui.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Combo Box Features](combo-box-features.md)
</dt> </dl>

 

 





