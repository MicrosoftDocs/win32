---
description: The GetFrameLength function returns the length of the frame.
ms.assetid: 30be1f5c-9b13-42ad-944a-92b1aee8a6bc
title: GetFrameLength function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetFrameLength
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# GetFrameLength function

The **GetFrameLength** function returns the length of the frame.

## Syntax


```C++
DWORD WINAPI GetFrameLength(
  _In_ HFRAME hFrame
);
```



## Parameters

<dl> <dt>

*hFrame* \[in\]
</dt> <dd>

Handle to a frame.

</dd> </dl>

## Return value

If the function is successful, the return value is the length of the frame   in bytes.

If the function is unsuccessful, the return value is zero.

## Remarks

[*Experts*](e.md) and [*parsers*](p.md) can call the **GetFrameLength** function.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




