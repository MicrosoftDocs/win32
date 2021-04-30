---
title: LB_GETSELITEMS message (Winuser.h)
description: Fills a buffer with an array of integers that specify the item numbers of selected items in a multiple-selection list box.
ms.assetid: 95dd72ef-76a5-4188-b2c8-d4c5eb2f34e3
keywords:
- LB_GETSELITEMS message Windows Controls
topic_type:
- apiref
api_name:
- LB_GETSELITEMS
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LB\_GETSELITEMS message

Fills a buffer with an array of integers that specify the item numbers of selected items in a multiple-selection list box.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The maximum number of selected items whose item numbers are to be placed in the buffer.

Windows 95/Windows 98/Windows Millennium Edition (Windows Me) : The *wParam* parameter is limited to 16-bit values. This means list boxes cannot contain more than 32,767 items. Although the number of items is restricted, the total size in bytes of the items in a list box is limited only by available memory.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a buffer large enough for the number of integers specified by the *wParam* parameter.

</dd> </dl>

## Return value

The return value is the number of items placed in the buffer. If the list box is a single-selection list box, the return value is LB\_ERR.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**LB\_GETSELCOUNT**](lb-getselcount.md)
</dt> </dl>

 

 





