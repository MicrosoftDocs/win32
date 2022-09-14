---
description: The GetProtocolFromTable function returns a handle to a protocol&\#8212;based on a given handoff table and value.
ms.assetid: 34b07079-0b20-40d8-a529-4179ecc68ebf
title: GetProtocolFromTable function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetProtocolFromTable
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# GetProtocolFromTable function

The **GetProtocolFromTable** function returns a handle to a protocol based on a given handoff table and value.

## Syntax


```C++
HPROTOCOL WINAPI GetProtocolFromTable(
  _In_  LPHANDOFFTABLE hTable,
  _In_  DWORD          ItemToFind,
  _Out_ PDWORD_PTR     lpInstData
);
```



## Parameters

<dl> <dt>

*hTable* \[in\]
</dt> <dd>

Handle to a handoff table.

</dd> <dt>

*ItemToFind* \[in\]
</dt> <dd>

Value used to locate the protocol in a handoff table. The value must be available in the protocol data.

</dd> <dt>

*lpInstData* \[out\]
</dt> <dd>

If available in the handoff table, instance data for the next protocol. Instance data cannot be longer than a DWORD\_PTR in length.

</dd> </dl>

## Return value

If the function is successful, the return value is a protocol handle.

If the function is unsuccessful, the return value is **NULL**.

## Remarks

When implementing the [RecognizeFrame](recognizeframe.md) export function, the **GetProtocolFromTable** function is used to obtain a handle to the next protocol. The **GetProtocolFromTable** function is called to retrieve a handle from the next protocol if the protocol identifies which protocol follows.

**Instance data**

Instance data can be any data that is less than or equal to a DWORD\_PTR in length, or a pointer to data, such as raw frame data, that does not need to be allocated by or freed by the parser.

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

[RecognizeFrame](recognizeframe.md)
</dt> </dl>

 

 




