---
description: The DestroyProtocol function destroys the protocol that the CreateProtocol function creates.
ms.assetid: f7621c2a-1905-4748-b8e3-7b49f3f2bf03
title: DestroyProtocol function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DestroyProtocol
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# DestroyProtocol function

The **DestroyProtocol** function destroys the protocol that the **CreateProtocol** function creates.

## Syntax


```C++
VOID WINAPI DestroyProtocol(
  _In_ HPROTOCOL hProtocol
);
```



## Parameters

<dl> <dt>

*hProtocol* \[in\]
</dt> <dd>

Handle to the protocol to be destroyed.

</dd> </dl>

## Return value

None.

## Remarks

The parser DLL calls the **DestroyProtocol** function during its implementation of [DllMain](dllmain-parser.md). **DestroyProtocol** is called when the operating system is going to unload the DLL.



| For information on                                        | See                                                     |
|-----------------------------------------------------------|---------------------------------------------------------|
| What parsers are, and how they work with Network Monitor. | [Parsers](parsers.md)                                  |
| How to implement **DllMain** includes an example.         | [Implementing DllMain](implementing-dllmain-parser.md) |



 

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

[DllMain](dllmain-parser.md)
</dt> </dl>

 

 




