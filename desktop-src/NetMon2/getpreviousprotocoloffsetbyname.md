---
description: The GetPreviousProtocolOffsetByName function returns the previous instance of a given protocol.
ms.assetid: 94f80776-564f-4089-9e3a-fdf38d9dfe8a
title: GetPreviousProtocolOffsetByName function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetPreviousProtocolOffsetByName
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# GetPreviousProtocolOffsetByName function

The **GetPreviousProtocolOffsetByName** function returns the previous instance of a given protocol.

## Syntax


```C++
DWORD WINAPI GetPreviousProtocolOffsetByName(
  _In_  HFRAME hFrame,
  _In_  DWORD  dwStartOffset,
  _In_  LPSTR  szProtocolName,
  _Out_ DWORD  *pdwPreviousOffset
);
```



## Parameters

<dl> <dt>

*hFrame* \[in\]
</dt> <dd>

Handle to the frame.

</dd> <dt>

*dwStartOffset* \[in\]
</dt> <dd>

Offset in the frame.

</dd> <dt>

*szProtocolName* \[in\]
</dt> <dd>

Name of the protocol you want to search for.

</dd> <dt>

*pdwPreviousOffset* \[out\]
</dt> <dd>

Pointer to a **DWORD** that contains the offset to the previous protocol (if the function succeeds).

</dd> </dl>

## Return value

If the function is successful, the return value is NMERR\_SUCCESS.

If the function is unsuccessful, the return value is NMERR\_PROTOCOL\_NOT\_FOUND.

## Remarks

[*Experts*](e.md) and [*parsers*](p.md) can call the **GetPreviousProtocolOffsetByName**.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




