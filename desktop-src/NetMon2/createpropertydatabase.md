---
description: The CreatePropertyDatabase function creates a property database that stores the properties of a protocol.
ms.assetid: 0a3be6ae-d7ce-4315-b4f2-b46bcfa25b69
title: CreatePropertyDatabase function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CreatePropertyDatabase
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# CreatePropertyDatabase function

The **CreatePropertyDatabase** function creates a property database that stores the properties of a protocol.

## Syntax


```C++
DWORD WINAPI CreatePropertyDatabase(
  _In_ HPROTOCOL hProtocol,
  _In_ DWORD     nProperties
);
```



## Parameters

<dl> <dt>

*hProtocol* \[in\]
</dt> <dd>

Handle of the protocol that is associated with the database. When Network Monitor calls the [Register](register-parser.md) function, Network Monitor passes the protocol handle to the parser DLL.

</dd> <dt>

*nProperties* \[in\]
</dt> <dd>

Number of properties stored in the database. Set this parameter to the number of properties that the protocol supports.

</dd> </dl>

## Return value

If the function is successful, the return value is NMERR\_SUCCESS.

If the function is unsuccessful, the return value is an error code.



| Return code                                                                                             | Description                                                                    |
|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_INTERNAL\_ERROR**</dt> </dl>   | An internal error has occurred.<br/>                                     |
| <dl> <dt>**NMERR\_INVALID\_HPOTOCOL**</dt> </dl> | The handle to the protocol specified in *hProtocol* is invalid.<br/>     |
| <dl> <dt>**NMERR\_OUT\_OF\_MEMORY**</dt> </dl>   | Network Monitor does not have enough memory to create the database.<br/> |



 

## Remarks

The **CreatePropertyDatabase** function should be called only when implementing the [Register](register-parser.md) function. The parser uses **CreatePropertyDatabase** to create a property database that describes the properties of a protocol. Network Monitor uses the database to interpret the information within the protocol.

The **CreatePropertyDatabase** function allocates the structures that Network Monitor needs to maintain a property database.

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

[Register](register-parser.md)
</dt> </dl>

 

 




