---
title: WM\_POINTERROUTEDAWAY message
description: Occurs on the process receiving input when the pointer input is routed to another process.AddContentWithCrossProcessChaining).
ms.assetid: '06F8152C-0DA0-4820-835E-07AD35B24310'
keywords: ["WM_POINTERROUTEDAWAY message Input Messages and Notifications"]
topic_type:
- apiref
api_name:
- WM_POINTERROUTEDAWAY
api_location:
- Winuser.h
api_type:
- HeaderDef
---

# WM\_POINTERROUTEDAWAY message

Occurs on the process receiving input when the pointer input is routed to another process.

Sent when pointer input transitions from one process to another across content configured for cross-process chaining ([**AddContentWithCrossProcessChaining**](https://msdn.microsoft.com/library/windows/desktop/mt622455)).

This message is sent to the process currently receiving pointer input.


```C++
#define WM_POINTERROUTEDAWAY       0x0252
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

This message is not sent with either a [**WM\_POINTERUP**](wm-pointerup.md) message or a [**WM\_POINTERCAPTURECHANGED**](wm-pointercapturechanged.md) message.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Messages](messages.md)
</dt> <dt>

[**WM\_POINTERROUTEDTO**](wm-pointerroutedto.md)
</dt> </dl>

 

 





