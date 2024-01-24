---
description: "Learn more about: EtwEventWrite function"
title: EtwEventWrite
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EtwEventWrite
api_type: 
- HeaderDef
api_location: 
- ntetw.h
---

# EtwEventWrite function

[The EtwEventWrite function and the structures that it returns are internal to the operating system and subject to change from one release of Windows to another.]

Writes a basic event to a session.

## Syntax

```C++
ULONG 
EVNTAPI
EtwEventWrite(
    __in REGHANDLE RegHandle,
    __in PCEVENT_DESCRIPTOR EventDescriptor,
    __in ULONG UserDataCount,
    __in_ecount_opt(UserDataCount) PEVENT_DATA_DESCRIPTOR UserData
    );
```

## Parameters

<dl> <dt>

*RegHandle*
</dt> <dd>

RegHandle for the provider.

</dd> <dt>

*EventDescriptor*
</dt> <dd>

Event descriptor of the event to log.

</dd> <dt>

*UserDataCount*
</dt> <dd>

Number of user data items.

</dd> <dt>

*UserData*
</dt> <dd>

Pointer to an array of user data items.

</dd> </dl>

## Return value

A Win32 error code.


## Remarks

The EtwEventWrite function and the structures that it returns are internal to the operating system and subject to change from one release of Windows to another. To maintain the compatibility of your application, it is better to use public functions instead.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | ntetw.h |

## See also

<dl> <dt>

[EventWrite](/windows/desktop/api/evntprov/nf-evntprov-eventwrite)
</dt> <dt>

[EventWriteEx](/windows/desktop/api/evntprov/nf-evntprov-eventwriteex)
</dt></dl>
