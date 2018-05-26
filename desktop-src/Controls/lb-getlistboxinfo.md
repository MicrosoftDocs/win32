---
title: LB\_GETLISTBOXINFO message
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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

This message is equivalent to [**GetListBoxInfo**](/windows/win32/Winuser/nf-winuser-getlistboxinfo?branch=master).

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**GetListBoxInfo**](/windows/win32/Winuser/nf-winuser-getlistboxinfo?branch=master)
</dt> </dl>

 

 





