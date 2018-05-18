---
Description: 'Specifies a socket descriptor used by send and receive requests with the Winsock registered I/O extensions.'
ms.assetid: '50E9516C-6078-4466-A593-3F29E4783740'
title: 'RIO\_RQ'
---

# RIO\_RQ

The **RIO\_RQ** typedef specifies a socket descriptor used by send and receive requests with the Winsock registered I/O extensions.


```C++
typedef struct RIO_RQ_t* RIO_RQ, **PRIO_RQ;
```



<dl> <dt>

**RIO\_RQ**
</dt> <dd>

A data type that specifies a socket descriptor used by send and receive requests.

</dd> </dl>

## Remarks

The Winsock registered I/O extensions operate primarily on a **RIO\_RQ** object rather than a socket. An application obtains a **RIO\_RQ** for an existing socket using the [**RIOCreateRequestQueue**](riocreaterequestqueue.md) function. The input socket must have been created by calling the [**WSASocket**](wsasocket-2.md) function with the **WSA\_FLAG\_RIO** flag set in the *dwFlags* parameter.

After obtaining a **RIO\_RQ** object, the underlying socket descriptor remains valid. An application may continue to use the underlying socket to set and query socket options, issue IOCTLs and ultimately close the socket.

> [!Note]  
> For purposes of efficiency, access to the completion queues ([**RIO\_CQ**](riocqueue.md) structs) and request queues (**RIO\_RQ** structs) are not protected by synchronization primitives. If you need to access a completion or request queue from multiple threads, access should be coordinated by a critical section, slim reader write lock or similar mechanism. This locking is not needed for access by a single thread. Different threads can access separate requests/completion queues without locks. The need for synchronization occurs only when multiple threads try to access the same queue. Synchronization is also required if multiple threads issue sends and receives on the same socket because the send and receive operations use the socket’s request queue.

 

The [**RIO\_RQ**](riocqueue.md) typedef is defined in the *Mswsockdef.h* header file which is automatically included in the *Mswsock.h* header file. The *Mswsockdef.h* header file should never be used directly.

## Requirements



|                                     |                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                        |
| Header<br/>                   | <dl> <dt>Mswsockdef.h (include Mswsock.h)</dt> </dl> |



## See also

<dl> <dt>

[**RIOCreateRequestQueue**](riocreaterequestqueue.md)
</dt> <dt>

[**RIOReceive**](rioreceive.md)
</dt> <dt>

[**RIOReceiveEx**](rioreceiveex.md)
</dt> <dt>

[**RIOResizeRequestQueue**](rioresizerequestqueue.md)
</dt> <dt>

[**RIOSend**](riosend.md)
</dt> <dt>

[**RIOSendEx**](riosendex.md)
</dt> <dt>

[**WSASocket**](wsasocket-2.md)
</dt> </dl>

 

 




