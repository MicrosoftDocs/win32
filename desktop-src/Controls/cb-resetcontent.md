---
title: CB_RESETCONTENT message (Winuser.h)
description: Removes all items from the list box and edit control of a combo box.
ms.assetid: 55203c34-87ca-46e9-a914-a480d43ccadd
keywords:
- CB_RESETCONTENT message Windows Controls
topic_type:
- apiref
api_name:
- CB_RESETCONTENT
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_RESETCONTENT message

Removes all items from the list box and edit control of a combo box.

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

This message always returns CB\_OKAY.

## Remarks

If you create the combo box with an owner-drawn style but without the [**CBS\_HASSTRINGS**](combo-box-styles.md) style, the owner of the combo box receives a [**WM\_DELETEITEM**](wm-deleteitem.md) message for each item in the combo box.

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

[**CB\_DELETESTRING**](cb-deletestring.md)
</dt> <dt>

[**WM\_DELETEITEM**](wm-deleteitem.md)
</dt> </dl>

 

 





