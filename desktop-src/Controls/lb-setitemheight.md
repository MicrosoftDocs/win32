---
title: LB_SETITEMHEIGHT message (Winuser.h)
description: Sets the height, in pixels, of items in a list box. If the list box has the LBS\_OWNERDRAWVARIABLE style, this message sets the height of the item specified by the wParam parameter. Otherwise, this message sets the height of all items in the list box.
ms.assetid: 3ac8e935-6de8-465f-a525-1f493b06ee7c
keywords:
- LB_SETITEMHEIGHT message Windows Controls
topic_type:
- apiref
api_name:
- LB_SETITEMHEIGHT
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LB\_SETITEMHEIGHT message

Sets the height, in pixels, of items in a list box. If the list box has the [**LBS\_OWNERDRAWVARIABLE**](list-box-styles.md) style, this message sets the height of the item specified by the *wParam* parameter. Otherwise, this message sets the height of all items in the list box.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the zero-based index of the item in the list box. Use this parameter only if the list box has the [**LBS\_OWNERDRAWVARIABLE**](list-box-styles.md) style; otherwise, set it to zero.

Windows 95/Windows 98/Windows Millennium Edition (Windows Me) : The *wParam* parameter is limited to 16-bit values. This means list boxes cannot contain more than 32,767 items. Although the number of items is restricted, the total size in bytes of the items in a list box is limited only by available memory.

</dd> <dt>

*lParam* 
</dt> <dd>

Specifies the height, in pixels, of the item. The maximum height is 255 pixels.

</dd> </dl>

## Return value

If the index or height is invalid, the return value is LB\_ERR.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**LB\_GETITEMHEIGHT**](lb-getitemheight.md)
</dt> </dl>

 

 





