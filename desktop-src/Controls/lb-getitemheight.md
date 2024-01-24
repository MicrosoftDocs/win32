---
title: LB_GETITEMHEIGHT message (Winuser.h)
description: Gets the height of items in a list box.
ms.assetid: ee96fce6-babd-4581-ac0e-2eb955fe543b
keywords:
- LB_GETITEMHEIGHT message Windows Controls
topic_type:
- apiref
api_name:
- LB_GETITEMHEIGHT
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LB\_GETITEMHEIGHT message

Gets the height of items in a list box.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The zero-based index of the list box item. This index is used only if the list box has the [**LBS\_OWNERDRAWVARIABLE**](list-box-styles.md) style; otherwise, it must be zero.

Windows 95/Windows 98/Windows Millennium Edition (Windows Me): The *wParam* parameter is limited to 16-bit values. This means list boxes cannot contain more than 32,767 items. Although the number of items is restricted, the total size in bytes of the items in a list box is limited only by available memory.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

The return value is the height, in pixels, of each item in the list box. The return value is the height of the item specified by the *wParam* parameter if the list box has the [**LBS\_OWNERDRAWVARIABLE**](list-box-styles.md) style. The return value is LB\_ERR if an error occurs.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**LB\_SETITEMHEIGHT**](lb-setitemheight.md)
</dt> </dl>

 

 





