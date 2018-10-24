---
title: BN_UNPUSHED notification code
description: Sent when the push state of a button is set to unpushed.
ms.assetid: 1ae7311d-f067-41fe-a117-e0c70d239e9d
keywords:
- BN_UNPUSHED notification code Windows Controls
topic_type:
- apiref
api_name:
- BN_UNPUSHED
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BN\_UNPUSHED notification code

Sent when the push state of a button is set to unpushed.

> [!Note]  
> This notification code is provided only for compatibility with 16-bit versions of Windows earlier than version 3.0. Applications should use the [**BS\_OWNERDRAW**](button-styles.md) button style and the [**DRAWITEMSTRUCT**](/windows/desktop/api/Winuser/ns-winuser-tagdrawitemstruct) structure for this task.

 

The parent window of the button receives this notification code through the [**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591) message.


```C++
BN_UNPUSHED

    WPARAM wParam;
    LPARAM lParam; 
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) contains the button's control identifier. The [**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657) specifies the notification code.

</dd> <dt>

*lParam* 
</dt> <dd>

A handle to the button.

</dd> </dl>

## Remarks

BN\_UNPUSHED is the same as the [BN\_UNHILITE](bn-unhilite.md) notification code.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[BN\_PUSHED](bn-pushed.md)
</dt> </dl>

 

 





