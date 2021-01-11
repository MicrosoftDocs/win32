---
description: The Register export function must be implemented in all parser DLLs. The implementation of Register creates and fills-in a property database for a protocol. Network Monitor uses the database to determine which properties the protocol supports.
ms.assetid: b8a2752d-30a6-48f2-90b3-b1430ae983d2
title: Register Parser callback function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Register
api_type:
- UserDefined
api_location:
- Netmon.h
---

# Register Parser callback function

The **Register** export function must be implemented in all parser DLLs. The implementation of **Register** creates and fills-in a [*property database*](p.md) for a protocol. Network Monitor uses the database to determine which properties the protocol supports.

## Syntax


```C++
VOID Register(
  _In_ HPROTOCOL hProtocol
);
```



## Parameters

<dl> <dt>

*hProtocol* \[in\]
</dt> <dd>

The handle of the protocol that Network Monitor provides when calling **Register**. The *hProtocol* handle is needed when calling export helper functions.

</dd> </dl>

## Return value

None.

## Remarks

Network Monitor starts calling the **Register** function as soon as a capture is loaded. Network Monitor calls the **Register** function for each protocol it can identify. The [CreateProtocol](createprotocol.md) function passes a pointer to the **Register** function.

The implementation of **Register** includes calls to the following functions.

-   A call to the [CreatePropertyDatabase](createpropertydatabase.md) and [AddProperty](/previous-versions/bb251873(v=msdn.10)) functions to create a database of all the properties that the protocol supports.
-   A call to the [CreateHandoffTable](createhandofftable.md) function is required if the protocol uses a [*handoff set*](h.md).

If the parser DLL contains multiple parsers, and the parser can detect more than one protocol, you must implement a **Register** function for each protocol.



| For Information on                                        | See                                                    |
|-----------------------------------------------------------|--------------------------------------------------------|
| What parsers are, and how they work with Network Monitor. | [Parsers](parsers.md)                                 |
| Which entry points are included in the parser DLL.        | [Parser DLL Architecture](parser-dll-architecture.md) |
| How to implement **Register**  includes an example.       | [Implementing Register](implementing-register.md)     |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[AddProperty](/previous-versions/bb251873(v=msdn.10))
</dt> <dt>

[CreateHandoffTable](createhandofftable.md)
</dt> <dt>

[CreatePropertyDatabase](createpropertydatabase.md)
</dt> <dt>

[CreateProtocol](createprotocol.md)
</dt> </dl>

 

