---
title: LB_GETITEMRECT message (Winuser.h)
description: Gets the dimensions of the rectangle that bounds a list box item as it is currently displayed in the list box.
ms.assetid: 84f94bc9-f7a4-4c2d-8c35-1bd291082af9
keywords:
- LB_GETITEMRECT message Windows Controls
topic_type:
- apiref
api_name:
- LB_GETITEMRECT
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LB\_GETITEMRECT message

Gets the dimensions of the rectangle that bounds a list box item as it is currently displayed in the list box.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The zero-based index of the item.

Windows 95/Windows 98/Windows Millennium Edition (Windows Me) : The *wParam* parameter is limited to 16-bit values. This means list boxes cannot contain more than 32,767 items. Although the number of items is restricted, the total size in bytes of the items in a list box is limited only by available memory.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**RECT**](/windows/win32/api/windef/ns-windef-rect) structure that will receive the client coordinates for the item in the list box.

</dd> </dl>

## Return value

If an error occurs, the return value is LB\_ERR.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**RECT**](/windows/win32/api/windef/ns-windef-rect)
</dt> </dl>

 

