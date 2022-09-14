---
title: LB_DELETESTRING message (Winuser.h)
description: Deletes a string in a list box.
ms.assetid: 3f360e07-b70d-4bfc-89d4-18d3b18b0fcf
keywords:
- LB_DELETESTRING message Windows Controls
topic_type:
- apiref
api_name:
- LB_DELETESTRING
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LB\_DELETESTRING message

Deletes a string in a list box.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The zero-based index of the string to be deleted.

Windows 95/Windows 98/Windows Millennium Edition (Windows Me) : The *wParam* parameter is limited to 16-bit values. This means list boxes cannot contain more than 32,767 items. Although the number of items is restricted, the total size in bytes of the items in a list box is limited only by available memory.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

The return value is a count of the strings remaining in the list. The return value is LB\_ERR if the *wParam* parameter specifies an index greater than the number of items in the list.

## Remarks

If an application creates the list box with an owner-drawn style but without the [**LBS\_HASSTRINGS**](list-box-styles.md) style, the system sends a [**WM\_DELETEITEM**](wm-deleteitem.md) message to the owner of the list box so the application can free any additional data associated with the item.

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

[**WM\_DELETEITEM**](wm-deleteitem.md)
</dt> </dl>

 

 





