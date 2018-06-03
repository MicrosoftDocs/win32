---
Description: Specifies a completion queue descriptor used for I/O completion notification by send and receive requests with the Winsock registered I/O extensions.
ms.assetid: 9196F8AF-3C48-445D-B2D5-E22A99759D92
title: RIO\_CQ
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RIO\_CQ

The **RIO\_CQ** typedef specifies a completion queue descriptor used for I/O completion notification by send and receive requests with the Winsock registered I/O extensions.


```C++
typedef struct RIO_CQ_t* RIO_CQ, **PRIO_CQ;
```



<dl> <dt>

**RIO\_CQ**
</dt> <dd>

A data type that specifies a completion queue descriptor used for I/O completion notification by send and receive requests.

</dd> </dl>

## Remarks

The **RIO\_CQ** object is used for I/O completion notification of send and receive networking requests by the Winsock registered I/O extensions.

An application can use the [**RIONotify**](/windows/desktop/api/Mswsock/nc-mswsock-lpfn_rionotify) function to request notification when a **RIO\_CQ** completion queue is not empty. An application can also poll the status at any time of a **RIO\_CQ** completion queue in a non-blocking way using the [**RIODequeueCompletion**](/windows/desktop/api/Mswsock/nc-mswsock-lpfn_riodequeuecompletion) function.

The **RIO\_CQ** object is created using the [**RIOCreateCompletionQueue**](/windows/desktop/api/Mswsock/nc-mswsock-lpfn_riocreatecompletionqueue) function. At creation time, the application must specify the size of the queue, which determines how many completion entries it can hold. When an application calls the [**RIOCreateRequestQueue**](/windows/desktop/api/Mswsock/nc-mswsock-lpfn_riocreaterequestqueue) function to obtain a [**RIO\_RQ**](riorqueue.md) handle, the application must specify a **RIO\_CQ** handle for send completions and a **RIO\_CQ** handle for receive completions. These handles may be identical when the same queue should be used for send and receive completion. The **RIOCreateRequestQueue** function also requires a maximum number of outstanding send and receive operations, which are charged against the capacity of the associated completion queue or queues. If the queues do not have sufficient capacity remaining, the **RIOCreateRequestQueue** call will fail with [WSAENOBUFS](https://www.bing.com/search?q=WSAENOBUFS).

The notification behavior for a completion queue is set when the **RIO\_CQ** is created.

For a completion queue that uses an event, the **Type** member of the [**RIO\_NOTIFICATION\_COMPLETION**](/windows/desktop/api/Mswsock/ns-mswsock-_rio_notification_completion) structure is set to **RIO\_EVENT\_COMPLETION**. The **Event.EventHandle** member should contain the handle for an event created by the [**WSACreateEvent**](/windows/desktop/api/Winsock2/nf-winsock2-wsacreateevent) or [**CreateEvent**](https://msdn.microsoft.com/windows/desktop/1f6d946e-c74c-4599-ac3d-b709216a0900) function. To receive the [**RIONotify**](/windows/desktop/api/Mswsock/nc-mswsock-lpfn_rionotify) completion, the application should wait on the specified event handle using [**WSAWaitForMultipleEvents**](/windows/desktop/api/Winsock2/nf-winsock2-wsawaitformultipleevents) or a similar wait routine. If the application plans to reset and reuse the event, the application can reduce overhead by setting the **Event.NotifyReset** member to a non-zero value. This causes the event to be automatically reset by the **RIONotify** function when the notification occurs. This mitigates the need to call the [**WSAResetEvent**](/windows/desktop/api/Winsock2/nf-winsock2-wsaresetevent) function to reset the event between calls to the **RIONotify** function.

For a completion queue that uses an I/O completion port, the **Type** member of the [**RIO\_NOTIFICATION\_COMPLETION**](/windows/desktop/api/Mswsock/ns-mswsock-_rio_notification_completion) structure is set to **RIO\_IOCP\_COMPLETION**. The **Iocp.IocpHandle** member should contain the handle for an I/O completion port created by the [**CreateIoCompletionPort**](https://msdn.microsoft.com/windows/desktop/40cb47fc-7b15-47f6-bee2-2611d4686053) function. To receive the [**RIONotify**](/windows/desktop/api/Mswsock/nc-mswsock-lpfn_rionotify) completion, the application should call the [**GetQueuedCompletionStatus**](https://msdn.microsoft.com/windows/desktop/8121a38b-0fe1-43b8-aed6-4b85af1feba9) or [**GetQueuedCompletionStatusEx**](https://msdn.microsoft.com/windows/desktop/3996c02c-562c-4697-a091-e241ad54b239) function. The application should provide a dedicated [**OVERLAPPED**](https://msdn.microsoft.com/windows/desktop/5037f6b9-e316-483b-a8e2-b58d2587ebd9) object for the completion queue, and it may also use the **Iocp.CompletionKey** member to distinguish **RIONotify** requests on the completion queue from other I/O completions including **RIONotify** completions for other completion queues.

> [!Note]  
> For purposes of efficiency, access to the completion queues (**RIO\_CQ** structs) and request queues ([**RIO\_RQ**](riorqueue.md) structs) are not protected by synchronization primitives. If you need to access a completion or request queue from multiple threads, access should be coordinated by a critical section, slim reader write lock or similar mechanism. This locking is not needed for access by a single thread. Different threads can access separate requests/completion queues without locks. The need for synchronization occurs only when multiple threads try to access the same queue. Synchronization is also required if multiple threads issue sends and receives on the same socket because the send and receive operations use the socket’s request queue.

 

If multiple threads attempt to access the same **RIO\_CQ** using [**RIODequeueCompletion**](/windows/desktop/api/Mswsock/nc-mswsock-lpfn_riodequeuecompletion), access must be coordinated by a critical section, slim reader writer lock , or similar mutual exclusion mechanism. If the completion queues are not shared, mutual exclusion is not required.

When a completion queue is no longer needed, an application can close it using the [**RIOCloseCompletionQueue**](/windows/desktop/api/Mswsock/nc-mswsock-lpfn_rioclosecompletionqueue) function.

The **RIO\_CQ** typedef is defined in the *Mswsockdef.h* header file which is automatically included in the *Mswsock.h* header file. The *Mswsockdef.h* header file should never be used directly.

## Thread Safety

If multiple threads attempt to access the same **RIO\_CQ** using [**RIODequeueCompletion**](/windows/desktop/api/Mswsock/nc-mswsock-lpfn_riodequeuecompletion), access must be coordinated by a critical section, slim reader writer lock , or similar mutual exclusion mechanism. If the completion queues are not shared, mutual exclusion is not required.

## Requirements



|                                     |                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                        |
| Header<br/>                   | <dl> <dt>Mswsockdef.h (include Mswsock.h)</dt> </dl> |



## See also

<dl> <dt>

[**CreateIoCompletionPort**](https://msdn.microsoft.com/windows/desktop/40cb47fc-7b15-47f6-bee2-2611d4686053)
</dt> <dt>

[**CreateEvent**](https://msdn.microsoft.com/windows/desktop/1f6d946e-c74c-4599-ac3d-b709216a0900)
</dt> <dt>

[**GetQueuedCompletionStatus**](https://msdn.microsoft.com/windows/desktop/8121a38b-0fe1-43b8-aed6-4b85af1feba9)
</dt> <dt>

[**GetQueuedCompletionStatusEx**](https://msdn.microsoft.com/windows/desktop/3996c02c-562c-4697-a091-e241ad54b239)
</dt> <dt>

[**OVERLAPPED**](https://msdn.microsoft.com/windows/desktop/5037f6b9-e316-483b-a8e2-b58d2587ebd9)
</dt> <dt>

[**RIO\_NOTIFICATION\_COMPLETION**](/windows/desktop/api/Mswsock/ns-mswsock-_rio_notification_completion)
</dt> <dt>

[**RIO\_NOTIFICATION\_COMPLETION\_TYPE**](/windows/desktop/api/Mswsock/ne-mswsock-_rio_notification_completion_type)
</dt> <dt>

[**RIO\_RQ**](riorqueue.md)
</dt> <dt>

[**RIOCloseCompletionQueue**](/windows/desktop/api/Mswsock/nc-mswsock-lpfn_rioclosecompletionqueue)
</dt> <dt>

[**RIOCreateCompletionQueue**](/windows/desktop/api/Mswsock/nc-mswsock-lpfn_riocreatecompletionqueue)
</dt> <dt>

[**RIOCreateRequestQueue**](/windows/desktop/api/Mswsock/nc-mswsock-lpfn_riocreaterequestqueue)
</dt> <dt>

[**RIODequeueCompletion**](/windows/desktop/api/Mswsock/nc-mswsock-lpfn_riodequeuecompletion)
</dt> <dt>

[**RIONotify**](/windows/desktop/api/Mswsock/nc-mswsock-lpfn_rionotify)
</dt> <dt>

[**WSACreateEvent**](/windows/desktop/api/Winsock2/nf-winsock2-wsacreateevent)
</dt> <dt>

[**WSAResetEvent**](/windows/desktop/api/Winsock2/nf-winsock2-wsaresetevent)
</dt> <dt>

[**WSAWaitForMultipleEvents**](/windows/desktop/api/Winsock2/nf-winsock2-wsawaitformultipleevents)
</dt> </dl>

 

 




