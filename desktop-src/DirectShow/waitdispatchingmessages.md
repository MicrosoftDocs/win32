---
description: The WaitDispatchingMessages function waits for an object to be signaled, while dispatching window messages.
ms.assetid: d15f6736-d141-47a3-b767-fbf774982fb4
title: WaitDispatchingMessages function (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WaitDispatchingMessages
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# WaitDispatchingMessages function

The `WaitDispatchingMessages` function waits for an object to be signaled, while dispatching window messages.

## Syntax


```C++
DWORD WINAPI WaitDispatchingMessages(
   HANDLE hObject,
   DWORD  dwWait,
   HWND   hwnd = NULL,
   UINT   uMsg = 0,
   HANDLE hEvent = NULL
);
```



## Parameters

<dl> <dt>

*hObject* 
</dt> <dd>

Handle of the object to wait for.

</dd> <dt>

*dwWait* 
</dt> <dd>

Time-out interval, in milliseconds.

</dd> <dt>

*hwnd* 
</dt> <dd>

Optional handle to a window.

</dd> <dt>

*uMsg* 
</dt> <dd>

Optional window message, specifying a message to dispatch.

</dd> <dt>

*hEvent* 
</dt> <dd>

Optional handle to an event to wait for.

</dd> </dl>

## Return value

Returns the value from the **WaitForMultipleObjects** function.

## Remarks

If an object owns a window, it should dispatch window messages while waiting. This function enables the object to wait for an event, semaphore, or other mutual exclusion object while dispatching messages.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Miscellaneous Helper Functions](miscellaneous-helper-functions.md)
</dt> </dl>

 

 




