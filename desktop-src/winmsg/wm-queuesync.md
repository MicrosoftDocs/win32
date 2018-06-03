---
Description: Sent by a computer-based training (CBT) application to separate user-input messages from other messages sent through the WH\_JOURNALPLAYBACK procedure.
ms.assetid: 9ac265be-1fcc-476f-9dee-3e961340b5a1
title: WM\_QUEUESYNC message
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WM\_QUEUESYNC message

Sent by a computer-based training (CBT) application to separate user-input messages from other messages sent through the [**WH\_JOURNALPLAYBACK**](https://www.bing.com/search?q=**WH\_JOURNALPLAYBACK**) procedure.


```C++
#define WM_QUEUESYNC                    0x0023
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

Type: **void**

A CBT application should return zero if it processes this message.

## Remarks

Whenever a CBT application uses the [**WH\_JOURNALPLAYBACK**](https://www.bing.com/search?q=**WH\_JOURNALPLAYBACK**) procedure, the first and last messages are **WM\_QUEUESYNC**. This allows the CBT application to intercept and examine user-initiated messages without doing so for events that it sends.

If an application specifies a **NULL** window handle, the message is posted to the message queue of the active window.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[*JournalPlaybackProc*](https://www.bing.com/search?q=*JournalPlaybackProc*)
</dt> <dt>

[**SetWindowsHookEx**](/windows/desktop/api/Winuser/nf-winuser-setwindowshookexa)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Hooks](hooks.md)
</dt> </dl>

 

 




