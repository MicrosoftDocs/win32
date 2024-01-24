---
title: LB_SETCURSEL message (Winuser.h)
description: Selects a string and scrolls it into view, if necessary. When the new string is selected, the list box removes the highlight from the previously selected string.
ms.assetid: 28d81f9d-a926-400c-8803-dcdb0e8f193d
keywords:
- LB_SETCURSEL message Windows Controls
topic_type:
- apiref
api_name:
- LB_SETCURSEL
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LB\_SETCURSEL message

Selects a string and scrolls it into view, if necessary. When the new string is selected, the list box removes the highlight from the previously selected string.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the zero-based index of the string that is selected. If this parameter is -1, the list box is set to have no selection.

Windows 95/Windows 98/Windows Millennium Edition (Windows Me) : The *wParam* parameter is limited to 16-bit values. This means list boxes cannot contain more than 32,767 items. Although the number of items is restricted, the total size in bytes of the items in a list box is limited only by available memory.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

If an error occurs, the return value is LB\_ERR. If the *wParam* parameter is -1, the return value is LB\_ERR even though no error occurred.

## Remarks

Use this message only with single-selection list boxes. You cannot use it to set or remove a selection in a multiple-selection list box.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**LB\_GETCURSEL**](lb-getcursel.md)
</dt> </dl>

 

 





