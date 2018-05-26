---
title: CB\_SETTOPINDEX message
description: An application sends the CB\_SETTOPINDEX message to ensure that a particular item is visible in the list box of a combo box.
ms.assetid: 2be78f17-848f-435a-9c2c-df6108ee7d9e
keywords:
- CB_SETTOPINDEX message Windows Controls
topic_type:
- apiref
api_name:
- CB_SETTOPINDEX
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

# CB\_SETTOPINDEX message

An application sends the **CB\_SETTOPINDEX** message to ensure that a particular item is visible in the list box of a combo box. The system scrolls the list box contents so that either the specified item appears at the top of the list box or the maximum scroll range has been reached.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the zero-based index of the list item.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

If the message is successful, the return value is zero.

If the message fails, the return value is CB\_ERR.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**CB\_GETTOPINDEX**](cb-gettopindex.md)
</dt> </dl>

 

 





