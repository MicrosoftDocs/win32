---
Description: Cancels a registered wait operation issued by the RegisterWaitForSingleObject function.
ms.assetid: ea700e55-fce7-46cd-bb96-0c129b429d46
title: UnregisterWaitEx function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# UnregisterWaitEx function

Cancels a registered wait operation issued by the [**RegisterWaitForSingleObject**](/windows/desktop/api/WinBase/nf-winbase-registerwaitforsingleobject) function.

## Syntax


```C++
BOOL WINAPI UnregisterWaitEx(
  _In_     HANDLE WaitHandle,
  _In_opt_ HANDLE CompletionEvent
);
```



## Parameters

<dl> <dt>

*WaitHandle* \[in\]
</dt> <dd>

The wait handle. This handle is returned by the [**RegisterWaitForSingleObject**](/windows/desktop/api/WinBase/nf-winbase-registerwaitforsingleobject) function.

</dd> <dt>

*CompletionEvent* \[in, optional\]
</dt> <dd>

A handle to the event object to be signaled when the wait operation has been unregistered. This parameter can be **NULL**.

If this parameter is **INVALID\_HANDLE\_VALUE**, the function waits for all callback functions to complete before returning.

If this parameter is **NULL**, the function marks the timer for deletion and returns immediately. However, most callers should wait for the callback function to complete so they can perform any needed cleanup.

If the caller provides this event and the function succeeds or the function fails with **ERROR\_IO\_PENDING**, do not close the event until it is signaled.

</dd> </dl>

## Return value

If the function succeeds, the return value is nonzero.

If the function fails, the return value is zero. To get extended error information, call [**GetLastError**](https://msdn.microsoft.com/windows/desktop/d852e148-985c-416f-a5a7-27b6914b45d4).

## Remarks

You cannot make a blocking call to **UnregisterWaitEx** from within a callback function for the same wait operation. Otherwise, the callback will be waiting for itself to finish. In general, a blocking call to **UnregisterWaitEx** creates a dependency between the current thread and the callback, so to make a blocking unregister call on another wait operation, you must ensure that the callback functions do not depend on one another and that the second wait operation does not also perform a blocking unregister call on the first operation.

Be careful when making a blocking **UnregisterWaitEx** call on a persistent thread. If the wait operation being unregistered was created with **WT\_EXECUTEINPERSISTENTTHREAD**, a deadlock may occur.

After making non-blocking call to **UnregisterWaitEx**, no new callback functions associated with *WaitHandle* can be queued. However, there may be pending callback functions already queued to worker threads.

Under some conditions, the function will fail with **ERROR\_IO\_PENDING** if *CompletionEvent* is **NULL**. This indicates that there are outstanding callback functions. Those callbacks either will execute or are in the middle of executing.

If *CompletionEvent* is a handle to an event provided by the caller, it is possible for the function to succeed, fail with **ERROR\_IO\_PENDING**, or fail with a different error code. If the function succeeds, or if the function fails with **ERROR\_IO\_PENDING**, the caller should always wait until the event is signaled to close the event. If the function fails with a different error code, it is not necessary to wait until the event is signaled to close the event.

**Windows XP:** If *CompletionEvent* is a handle to an event provided by the caller and the function fails with **ERROR\_IO\_PENDING**, the caller should wait until the event is signaled to close the event. This behavior changed starting with Windows Vista.

To compile an application that uses this function, define **\_WIN32\_WINNT** as 0x0500 or later. For more information, see [Using the Windows Headers](https://msdn.microsoft.com/windows/desktop/a4def563-8ddc-4630-ae8a-86c07cf98374).

## Requirements



|                                     |                                                                                                                                                                                                                                                                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                                                                                                                                                                                                                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                                                                                                                                                                                                                                                                           |
| Header<br/>                   | <dl> <dt>Threadpoollegacyapiset.h on Windows 8 and Windows Server 2012 (include Windows.h); </dt> <dt>WinBase.h on Windows 7, Windows Server 2008 R2, Windows Vista, Windows Server 2008, Windows XP and Windows Server 2003 (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Kernel32.lib</dt> </dl>                                                                                                                                                                                                                                                                        |
| DLL<br/>                      | <dl> <dt>Kernel32.dll</dt> </dl>                                                                                                                                                                                                                                                                        |



## See also

<dl> <dt>

[**RegisterWaitForSingleObject**](/windows/desktop/api/WinBase/nf-winbase-registerwaitforsingleobject)
</dt> <dt>

[Synchronization Functions](synchronization-functions.md)
</dt> <dt>

[Thread Pooling](https://msdn.microsoft.com/windows/desktop/a5e52080-35d4-47f5-9050-90889e3bf2f8)
</dt> </dl>

 

 




