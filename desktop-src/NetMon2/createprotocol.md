---
description: The CreateProtocol function notifies Network Monitor that a specific protocol parser exists.
ms.assetid: 13ae261f-b1c0-4afc-b718-d64b3d4ec5ee
title: CreateProtocol function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CreateProtocol
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# CreateProtocol function

The **CreateProtocol** function notifies Network Monitor that a specific protocol parser exists.

## Syntax


```C++
HPROTOCOL WINAPI CreateProtocol(
  _In_ LPSTR         ProtocolName,
  _In_ LPENTRYPOINTS lpEntryPoints,
  _In_ DWORD         cbEntryPoints
);
```



## Parameters

<dl> <dt>

*ProtocolName* \[in\]
</dt> <dd>

Name of the protocol the parser will detect.

</dd> <dt>

*lpEntryPoints* \[in\]
</dt> <dd>

An [ENTRYPOINTS](entrypoints.md) structure that contains the remaining parser DLL entry points. See Remarks for a list of the export functions that each entry point references. Entry points must be provided in the order that the **ENTRYPOINTS** structure specifies.

</dd> <dt>

*cbEntryPoints* \[in\]
</dt> <dd>

The size of the **ENTRYPOINTS** structure. Network Monitor provides an ENTRYPOINTS\_SIZE macro that you can use to specify the size of the structure.

</dd> </dl>

## Return value

If the function is successful, the return value is a handle to the protocol.

If the function is unsuccessful, the return value is **NULL**.

## Remarks

The parser DLL calls **CreateProtocol** during its implementation of [DllMain](dllmain-parser.md). The **CreateProtocol** function is called when the operating system loads the parser DLL for the first time.

The entry points referenced in the *lpEntryPoints* parameter include pointers to the following export functions that must be provided in the order presented here.

-   [Register](register-parser.md)
-   [Deregister](deregister.md)
-   [RecognizeFrame](recognizeframe.md)
-   [AttachProperties](attachproperties.md)
-   [FormatProperties](formatproperties.md)



| For information on                                                                                 | See                                                     |
|----------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| What parsers are, and how they work with Network Monitor.                                          | [Parsers](parsers.md)                                  |
| How to implement **DllMain** includes an example of calling **CreateProtocol** within **DllMain**. | [Implementing DllMain](implementing-dllmain-parser.md) |



 

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

[DllMain](/windows/desktop/Dlls/dllmain)
</dt> </dl>

 

