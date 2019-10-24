---
Description: Posted to the installing thread's message queue when a timer expires. The message is posted by the GetMessage or PeekMessage function.
ms.assetid: 419e3f05-35ec-4e48-b24d-ab98df687b20
title: WM_TIMER message
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_TIMER message

Posted to the installing thread's message queue when a timer expires. The message is posted by the [**GetMessage**](https://msdn.microsoft.com/en-us/library/ms644936(v=VS.85).aspx) or [**PeekMessage**](https://msdn.microsoft.com/en-us/library/ms644943(v=VS.85).aspx) function.


```C++
#define WM_TIMER                        0x0113
```



## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

The timer identifier.

</dd> <dt>

*lParam* \[in\]
</dt> <dd>

A pointer to an application-defined callback function that was passed to the [**SetTimer**](https://msdn.microsoft.com/en-us/library/ms644906(v=VS.85).aspx) function when the timer was installed.

</dd> </dl>

## Return value

Type: **LRESULT**

An application should return zero if it processes this message.

## Remarks

You can process the message by providing a **WM\_TIMER** case in the window procedure. Otherwise, [**DispatchMessage**](https://msdn.microsoft.com/en-us/library/ms644934(v=VS.85).aspx) will call the [*TimerProc*](https://msdn.microsoft.com/en-us/library/ms644907(v=VS.85).aspx) callback function specified in the call to the [**SetTimer**](https://msdn.microsoft.com/en-us/library/ms644906(v=VS.85).aspx) function used to install the timer.

The **WM\_TIMER** message is a low-priority message. The [**GetMessage**](https://msdn.microsoft.com/en-us/library/ms644936(v=VS.85).aspx) and [**PeekMessage**](https://msdn.microsoft.com/en-us/library/ms644943(v=VS.85).aspx) functions post this message only when no other higher-priority messages are in the thread's message queue.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**GetMessage**](https://msdn.microsoft.com/en-us/library/ms644936(v=VS.85).aspx)
</dt> <dt>

[**PeekMessage**](https://msdn.microsoft.com/en-us/library/ms644943(v=VS.85).aspx)
</dt> <dt>

[**SetTimer**](https://msdn.microsoft.com/en-us/library/ms644906(v=VS.85).aspx)
</dt> <dt>

[**TimerProc**](https://msdn.microsoft.com/en-us/library/ms644907(v=VS.85).aspx)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Timers](timers.md)
</dt> </dl>

 

 




