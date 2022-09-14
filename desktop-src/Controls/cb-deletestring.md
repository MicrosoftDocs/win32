---
title: CB_DELETESTRING message (Winuser.h)
description: Deletes a string in the list box of a combo box.
ms.assetid: 8d526796-04ef-4c01-94d6-fb50e6fef27b
keywords:
- CB_DELETESTRING message Windows Controls
topic_type:
- apiref
api_name:
- CB_DELETESTRING
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_DELETESTRING message

Deletes a string in the list box of a combo box.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The zero-based index of the string to delete.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

The return value is a count of the strings remaining in the list. If the *wParam* parameter specifies an index greater than the number of items in the list, the return value is CB\_ERR.

## Remarks

If you create the combo box with an owner-drawn style but without the [**CBS\_HASSTRINGS**](combo-box-styles.md) style, the system sends a [**WM\_DELETEITEM**](wm-deleteitem.md) message to the owner of the combo box so the application can free any additional data associated with the item.

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

[**CB\_RESETCONTENT**](cb-resetcontent.md)
</dt> <dt>

[**WM\_DELETEITEM**](wm-deleteitem.md)
</dt> </dl>

 

 





