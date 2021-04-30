---
description: The DestroyPropertyDatabase function releases the resources used to create the protocol property database.
ms.assetid: a0d1c416-8b08-47ca-a88e-e70588574376
title: DestroyPropertyDatabase function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DestroyPropertyDatabase
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# DestroyPropertyDatabase function

The **DestroyPropertyDatabase** function releases the resources used to create the protocol [*property database*](p.md).

## Syntax


```C++
DWORD WINAPI DestroyPropertyDatabase(
  _In_ HPROTOCOL hProtocol
);
```



## Parameters

<dl> <dt>

*hProtocol* \[in\]
</dt> <dd>

Handle to the property database to be destroyed. The handle is passed to the parser DLL when Network Monitor calls the [Deregister](deregister.md) function.

</dd> </dl>

## Return value

If the function is successful, the return value is NMERR\_SUCCESS.

If the function is unsuccessful, the return value is an error code.



| Return code                                                                                              | Description                                |
|----------------------------------------------------------------------------------------------------------|--------------------------------------------|
| <dl> <dt>**NMERR\_INTERNAL\_ERROR**</dt> </dl>    | An internal error occurred. <br/>    |
| <dl> <dt>**NMERR\_INVALID\_HPROTOCOL**</dt> </dl> | Invalid handle in *hProtocol*. <br/> |



 

## Remarks

The **DestroyPropertyDatabase** function should be called only when implementing the [Deregister](deregister.md) export function for the protocol. For parser DLLs that support multiple protocols, the **DestroyPropertyDatabase** function is called for each implementation of **Deregister**.



| For information on                                        | See                                                    |
|-----------------------------------------------------------|--------------------------------------------------------|
| What parsers are, and how they work with Network Monitor. | [Parsers](parsers.md)                                 |
| Which entry points are included in the parser DLL.        | [Parser DLL Architecture](parser-dll-architecture.md) |
| How to implement **Deregister**  includes an example.     | [Implementing Deregister](implementing-deregister.md) |



 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



## See also

<dl> <dt>

[Deregister](deregister.md)
</dt> </dl>

 

 




