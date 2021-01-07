---
description: Specifies a registered buffer descriptor used with the Winsock registered I/O extensions.
ms.assetid: 87D0A3F6-A44C-4D7F-B276-7FD5DC2DE7A3
title: RIO_BUFFERID (Mswsockdef.h)
ms.topic: reference
ms.date: 05/31/2018
---

# RIO\_BUFFERID

The **RIO\_BUFFERID** typedef specifies a registered buffer descriptor used with the Winsock registered I/O extensions.


```C++
typedef struct RIO_BUFFERID_t* RIO_BUFFERID, **PRIO_BUFFERID;
```



<dl> <dt>

**RIO\_BUFFERID**
</dt> <dd>

A data type that specifies a registered buffer descriptor used with send and receive requests.

</dd> </dl>

## Remarks

The Winsock registered I/O extensions operate primarily on registered buffers using **RIO\_BUFFERID** objects. An application obtains a **RIO\_BUFFERID** for an existing buffer using the [**RIORegisterBuffer**](/previous-versions/windows/desktop/legacy/hh437199(v=vs.85)) function. An application can release a registration using the [**RIODeregisterBuffer**](/windows/win32/api/mswsock/nc-mswsock-lpfn_rioderegisterbuffer) function.

When an existing buffer is registered as a **RIO\_BUFFERID** object using the [**RIORegisterBuffer**](/previous-versions/windows/desktop/legacy/hh437199(v=vs.85)) function, certain internal resources are allocated from physical memory, and the existing application buffer will be locked into physical memory. The [**RIODeregisterBuffer**](/windows/win32/api/mswsock/nc-mswsock-lpfn_rioderegisterbuffer) function is called to deregister the buffer, free these internal resources, and allow the buffer to be unlocked and released from physical memory.

Repeated registration and deregistration of application buffers using the Winsock registered I/O extensions may cause significant performance degradation. The following buffer management approaches should be considered when designing an application using the Winsock registered I/O extensions to minimize repeated registration and deregistration of application buffers:

-   • Maximize the reuse of buffers.
-   • Maintain a limited pool of unused registered buffers for use by the application.
-   • Maintain a limited pool of registered buffers and perform buffer copies between these registered buffers and other unregistered buffers.

The **RIO\_BUFFERID** typedef is defined in the *Mswsockdef.h* header file which is automatically included in the *Mswsock.h* header file. The *Mswsockdef.h* header file should never be used directly.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                        |
| Header<br/>                   | <dl> <dt>Mswsockdef.h (include Mswsock.h)</dt> </dl> |



## See also

<dl> <dt>

[**RIO\_BUF**](/windows/desktop/api/Mswsockdef/ns-mswsockdef-rio_buf)
</dt> <dt>

[**RIODeregisterBuffer**](/windows/win32/api/mswsock/nc-mswsock-lpfn_rioderegisterbuffer)
</dt> <dt>

[**RIOReceive**](/windows/win32/api/mswsock/nc-mswsock-lpfn_rioreceive)
</dt> <dt>

[**RIOReceiveEx**](/windows/win32/api/mswsock/nc-mswsock-lpfn_rioreceiveex)
</dt> <dt>

[**RIORegisterBuffer**](/previous-versions/windows/desktop/legacy/hh437199(v=vs.85))
</dt> <dt>

[**RIOSend**](/windows/win32/api/mswsock/nc-mswsock-lpfn_riosend)
</dt> <dt>

[**RIOSendEx**](/previous-versions/windows/desktop/legacy/hh437216(v=vs.85))
</dt> </dl>

 

 
