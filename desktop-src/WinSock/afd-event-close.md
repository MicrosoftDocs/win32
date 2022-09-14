---
description: Winsock network tracing event for socket close operation.
ms.assetid: C59B2B51-288A-46C9-B390-26A18DB0C2FB
title: AFD_EVENT_CLOSE event
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- AFD_EVENT_CLOSE
api_type:
- NA
api_location: 
---

# AFD\_EVENT\_CLOSE event

The **AFD\_EVENT\_CLOSE** event is a Winsock network tracing event for socket close operation.


```C++
const EVENT_DESCRIPTOR AFD_EVENT_CLOSE = {0x3e9, 0x0, 0x10, 0x4, 0xf, 0x3e9, 0x8000000000000004};
```



## Parameters

<dl> <dt>

*EnterExit* 
</dt> <dd>

Information on this event.

The following table lists the possible values for the *EnterExit* parameter:



| Value                                                                        | Meaning                                                                                              |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | The start of a Winsock request.<br/>                                                           |
| <dl> <dt>1</dt> </dl> | The Winsock request completed.<br/>                                                            |
| <dl> <dt>2</dt> </dl> | The Winsock AFD driver took an internal action (aborting a connection, for example).<br/>      |
| <dl> <dt>3</dt> </dl> | The TCP/IP driver caused this event to occur. This usually indicates a data notification.<br/> |
| <dl> <dt>4</dt> </dl> | The Winsock AFD driver caused this event to occur (setting a socket option, for example).<br/> |



 

</dd> <dt>

*Location* 
</dt> <dd>

A private field used internally.

</dd> <dt>

*Process* 
</dt> <dd>

The [EPROCESS](/windows-hardware/drivers/kernel/eprocess) address of the process that owns the related socket. This is an opaque structure that serves as the process object for a process. For more information, see the Windows Driver Kit documentation for the [EPROCESS](/windows-hardware/drivers/kernel/eprocess) structure.

</dd> <dt>

*Endpoint* 
</dt> <dd>

The AFD\_ENDPOINT address of the socket.

</dd> <dt>

*Status* 
</dt> <dd>

The NTSTATUS code for the operation.

</dd> </dl>

## Remarks

The **AFD\_EVENT\_CLOSE** event is traced for a Winsock network operation to close a socket. The channel for this event is Winsock-AFD. The level for this event is informational.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Control of Winsock Tracing](control-of-winsock-tracing.md)
</dt> <dt>

[**EVENT\_DESCRIPTOR**](/windows/desktop/api/evntprov/ns-evntprov-event_descriptor)
</dt> <dt>

[Winsock Tracing](winsock-tracing.md)
</dt> <dt>

[Winsock Tracing Levels](winsock-tracing-levels.md)
</dt> <dt>

[Winsock Catalog Change Tracing Details](winsock-layered-service-provider-tracing-event-details.md)
</dt> </dl>

 

