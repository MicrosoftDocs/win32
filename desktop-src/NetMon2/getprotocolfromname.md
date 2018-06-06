---
Description: The GetProtocolFromName function returns a handle to a protocol of a given name.
ms.assetid: 18f5a9a7-4245-479d-a0da-2ede362a60b8
title: GetProtocolFromName function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetProtocolFromName function

The **GetProtocolFromName** function returns a handle to a protocol of a given name.

## Syntax


```C++
HPROTOCOL WINAPI GetProtocolFromName(
  _In_ LPSTR ProtocolName
);
```



## Parameters

<dl> <dt>

*ProtocolName* \[in\]
</dt> <dd>

Protocol name (for example, IP).

</dd> </dl>

## Return value

If the function is successful, the return value is a protocol handle.

If the function is unsuccessful, the return value is **NULL**.

## Remarks

[*Experts*](e.md#-netmon-expert-gly) and [*parsers*](p.md#-netmon-parser-gly) can call the **GetProtocolFromName** function.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




