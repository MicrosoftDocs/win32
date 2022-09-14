---
title: LB_GETLISTBOXINFO message (Winuser.h)
description: Gets the number of items per column in a specified list box.
ms.assetid: 925bebd9-2563-4892-a7d7-73d4ef012b42
keywords:
- LB_GETLISTBOXINFO message Windows Controls
topic_type:
- apiref
api_name:
- LB_GETLISTBOXINFO
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LB\_GETLISTBOXINFO message

Gets the number of items per column in a specified list box.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> </dl>

## Return value

The return value is the number of items per column.

## Remarks

This message is equivalent to [**GetListBoxInfo**](/windows/desktop/api/Winuser/nf-winuser-getlistboxinfo).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**GetListBoxInfo**](/windows/desktop/api/Winuser/nf-winuser-getlistboxinfo)
</dt> </dl>

 

 





