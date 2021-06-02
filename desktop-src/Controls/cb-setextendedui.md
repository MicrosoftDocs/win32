---
title: CB_SETEXTENDEDUI message (Winuser.h)
description: An application sends a CB\_SETEXTENDEDUI message to select either the default UI or the extended UI for a combo box that has the CBS\_DROPDOWN or CBS\_DROPDOWNLIST style.
ms.assetid: c489e484-777e-4afa-996b-1ec3eb6552ab
keywords:
- CB_SETEXTENDEDUI message Windows Controls
topic_type:
- apiref
api_name:
- CB_SETEXTENDEDUI
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_SETEXTENDEDUI message

An application sends a **CB\_SETEXTENDEDUI** message to select either the default UI or the extended UI for a combo box that has the [**CBS\_DROPDOWN**](combo-box-styles.md) or [**CBS\_DROPDOWNLIST**](combo-box-styles.md) style.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A **BOOL** that specifies whether the combo box uses the extended UI (**TRUE**) or the default UI (**FALSE**).

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

If the operation succeeds, the return value is CB\_OKAY. If an error occurs, it is CB\_ERR.

## Remarks

By default, the F4 key opens or closes the list and the DOWN ARROW changes the current selection. In the extended UI, the F4 key is disabled and the DOWN ARROW key opens the drop-down list. The mouse wheel, which normally scrolls through the items in the list, has no effect when the extended UI is set.

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

[**CB\_GETEXTENDEDUI**](cb-getextendedui.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Combo Box Features](combo-box-features.md)
</dt> </dl>

 

 





