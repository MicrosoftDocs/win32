---
title: WM\_POINTERROUTEDTO message
description: Sent when ongoing pointer input, for an existing pointer ID, transitions from one process to another across content configured for cross-process chaining (AddContentWithCrossProcessChaining).
ms.assetid: 163E2C31-4E29-4CBA-B079-1963D4762D7B
keywords:
- WM_POINTERROUTEDTO message Input Messages and Notifications
topic_type:
- apiref
api_name:
- WM_POINTERROUTEDTO
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WM\_POINTERROUTEDTO message

Sent when ongoing pointer input, for an existing pointer ID, transitions from one process to another across content configured for cross-process chaining ([**AddContentWithCrossProcessChaining**](https://msdn.microsoft.com/library/windows/desktop/mt622455)).

This message is sent to the process not currently receiving pointer input.


```C++
#define WM_POINTERROUTEDTO       0x0251
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

## Remarks

This message is not sent when a [**WM\_POINTERDOWN**](wm-pointerdown.md) message is posted for a new pointer ID on a different process.

A [**WM\_POINTERDOWN**](wm-pointerdown.md) message is not sent if a **WM\_POINTERROUTEDTO** message is posted first.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Messages](messages.md)
</dt> <dt>

[**WM\_POINTERROUTEDAWAY**](wm-pointerroutedaway.md)
</dt> </dl>

 

 





