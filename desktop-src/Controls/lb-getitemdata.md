---
title: LB_GETITEMDATA message (Winuser.h)
description: Gets the application-defined value associated with the specified list box item.
ms.assetid: 3a3f7fa5-ce04-4e95-86e1-5c7de796d1b6
keywords:
- LB_GETITEMDATA message Windows Controls
topic_type:
- apiref
api_name:
- LB_GETITEMDATA
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LB\_GETITEMDATA message

Gets the application-defined value associated with the specified list box item.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The index of the item.

Windows 95/Windows 98/Windows Millennium Edition (Windows Me) : The *wParam* parameter is limited to 16-bit values. This means list boxes cannot contain more than 32,767 items. Although the number of items is restricted, the total size in bytes of the items in a list box is limited only by available memory.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

The return value is the value associated with the item, or LB\_ERR if an error occurs. If the item is in an owner-drawn list box and was created without the [**LBS\_HASSTRINGS**](list-box-styles.md) style, this value was in the *lParam* parameter of the [**LB\_ADDSTRING**](lb-addstring.md) or [**LB\_INSERTSTRING**](lb-insertstring.md) message that added the item to the list box. Otherwise, it is the value in the *lParam* of the [**LB\_SETITEMDATA**](lb-setitemdata.md) message.

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

[**LB\_ADDSTRING**](lb-addstring.md)
</dt> <dt>

[**LB\_INSERTSTRING**](lb-insertstring.md)
</dt> <dt>

[**LB\_SETITEMDATA**](lb-setitemdata.md)
</dt> </dl>

 

 





