---
Description: The GetProtocolStartOffsetHandle function returns the frame offset of a given protocol.
ms.assetid: b1e3a03b-f211-4c2c-8810-9e220c40136b
title: GetProtocolStartOffsetHandle function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetProtocolStartOffsetHandle function

The **GetProtocolStartOffsetHandle** function returns the frame offset of a given protocol.

## Syntax


```C++
DWORD WINAPI GetProtocolStartOffsetHandle(
  _In_ HFRAME    hFrame,
  _In_ HPROTOCOL hProtocol
);
```



## Parameters

<dl> <dt>

*hFrame* \[in\]
</dt> <dd>

Handle to a frame.

</dd> <dt>

*hProtocol* \[in\]
</dt> <dd>

Handle to a protocol.

</dd> </dl>

## Return value

If the function is successful, the return value is the offset of the frame   measured in bytes.

If the function is unsuccessful, the return value is one (1).

## Remarks

[*Experts*](https://www.bing.com/search?q=*Experts*) and [*parsers*](https://www.bing.com/search?q=*parsers*) can call the **GetProtocolStartOffsetHandle** function.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




