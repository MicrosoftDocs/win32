---
Description: 'The GetProtocolInfo function returns a pointer to a protocol information value.'
ms.assetid: '1ba47889-b2ed-47ba-94f9-1b781af6d01f'
title: GetProtocolInfo function
---

# GetProtocolInfo function

The **GetProtocolInfo** function returns a pointer to a protocol information value.

## Syntax


```C++
LPPROTOCOLINFO WINAPI GetProtocolInfo(
  _In_ HPROTOCOL hProtocol
);
```



## Parameters

<dl> <dt>

*hProtocol* \[in\]
</dt> <dd>

Handle to a protocol.

</dd> </dl>

## Return value

If the function is successful, the return value is a pointer to the protocol information value.

If the function is unsuccessful, the return value is **NULL**.

## Remarks

[*Experts*](e.md#-netmon-expert-gly) and [*parsers*](p.md#-netmon-parser-gly) can call the **GetProtocolInfo** function.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




