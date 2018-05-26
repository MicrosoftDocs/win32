---
title: WM\_POINTERROUTEDRELEASED message
description: Sent to all processes (configured for cross-process chaining through AddContentWithCrossProcessChaining and not currently handling pointer input) ever associated with a specific pointer ID, when a WM\_POINTERUP message is received on the current process.
ms.assetid: B031ED80-6F1B-42A7-B4E2-55934E2C456C
keywords:
- WM_POINTERROUTEDRELEASED message Input Messages and Notifications
topic_type:
- apiref
api_name:
- WM_POINTERROUTEDRELEASED
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

# WM\_POINTERROUTEDRELEASED message

Sent to all processes (configured for cross-process chaining through [**AddContentWithCrossProcessChaining**](https://msdn.microsoft.com/library/windows/desktop/mt622455) and not currently handling pointer input) ever associated with a specific pointer ID, when a [**WM\_POINTERUP**](wm-pointerup.md) message is received on the current process.


```C++
#define WM_POINTERROUTEDRELEASED       0x0253
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Unused.

</dd> <dt>

*lParam* 
</dt> <dd>

Unused.

</dd> </dl>

## Return value

NULL

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Messages](messages.md)
</dt> </dl>

 

 





